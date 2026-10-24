# Operations

This section describes how the WFMS is operated — one integrated system whose workflow domains carry distinct
operational requirements, under the common operating principle of maximal automation for high quality operations at
minimal human effort. It covers deployment, monitoring, incident response, automation and agents, service ownership,
and per-domain operational procedures.

## Operations Model: Maximal Automation

ePIC operates its production with a small team, so operational quality has to come from the system rather than from
staffing. The design target is high quality operations at minimal human effort: automation carries the routine work,
the system concentrates human attention on what needs it, and people make the decisions. Operations is the leading
driver of the production side of the WFMS — capabilities are built because they remove operational effort, and the
operational experience of running campaigns feeds directly back into the design. The automation exists to move operator
effort from routine submission and campaign mechanics to problems and steering.

The model has consistent consequences across the system. Every capability ships with its operational lifecycle designed
in: its service definition, restart behavior, health check, and cache or state management are part of the capability,
built alongside it. Attention is concentrated deliberately, through alarms, status indication, daily reports, and
assessments, so an operator reads what changed and what needs action rather than patrolling the system. And the
no-silent-failures precept described in Platform is an operations precept first: an error that surfaces immediately
with its diagnostics costs minutes, and an error that hides costs the effort the automation exists to save.

## Continuous Deployment and Releases

Fast development turnaround without loss of operational control is a stated requirement of the system. Development runs
on coordinated branches across the core repositories, and deployment is scripted and pulls from git, so the repository
is the single source of what runs. Deploys are small, frequent, and repeatable, reloading the web tier and its workers.

The credentialed operations agent is decoupled from routine deploys: the doer scripts it dispatches run fresh from the
deploy tree, so a script fix is live on the next dispatch, and the lightweight deploy that carries web and MCP changes
leaves the agent running. The full deploy restarts the agent on the new release.

The production application repository, swf-epicprod, deploys itself. A host-side timer polls canonical main every minute
and chooses no deploy, the lightweight deploy or the full deploy from the changed paths. It refuses unmerged or dirty
checkout code and stops on a database migration, which is deployed by hand on approval. Production is not registered
as a GitHub Actions runner; pull-request checks run on GitHub-hosted machines. The host publishes a
`deployment/swf-testbed` commit status on GitHub.
Contributors open a pull request, which reports the deploy its merge will trigger, and merge it themselves
([AUTODEPLOY.md](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/AUTODEPLOY.md)). This documentation follows the
same continuous practice, rebuilding on every push.

The production services presently share the testbed platform at BNL. Requirements for dedicated long-term hosting of
the production services have been developed, with provisioning planned for FY27.

## Monitoring and Incident Response

The monitoring posture is cached health, visible everywhere. The operations agent maintains a system status record of
the services production depends on; pages read the cached state rather than probing services on request, and the
production navigation carries a status indicator that turns red when the aggregate is red or stale, so infrastructure
trouble is visible at a glance on both the internal and external faces. Agents register and heartbeat to the monitor,
their logs land in the monitor database, and the alarm system carries the conditions that need action. Message-driven
services are health-checked by round trips over the message path they serve, since that is the path whose function
matters.

The PanDA platform alarm assesses held submit workers against both a count
and a share of the schedd's worker population: at least 10 held workers and
at least 10% by default, configured in SysConfig. Isolated holds remain in
worker diagnostics. The alarm clears when a new platform assessment falls
below either threshold, removing its entry from Production now.

Incident response is drill-down and bounded action. Diagnosis runs from the campaign task to the PanDA task, job,
queue, or site, with error summaries at each level and the complete payload log one click from the job page. An AI
assessment can be requested on the spot to summarize and interpret what the operator is looking at. Response actions —
retry, recovery, resubmission, priority changes — are the same catalog controls used in routine operation, executed
through the operations agent and recorded on the production record. Task actions are verified operations: each
request becomes a durable record that tracks the command from acceptance to the observed PanDA state change, and the
record names the requesting operator even though the command reaches PanDA under the system's credential.

Incidents are as often data-side as processing-side. Transfer failures, storage pressure, log-upload contention, and
dataset integrity carry the same discipline: surfaced, diagnosed through the data management views, and resolved with
recorded actions.

## Automation and Agents

Always-on services follow one operational pattern: systemd-managed with automatic restart, burst-capped so a
persistently failing service lands in a visible failed state instead of flapping indefinitely, and with a deliberate
stop distinguished from a crash so supervision does not fight an operator's intent.

Autonomous supervision closes the loop. A scheduled supervisor keeps the credentialed agent a true singleton — a second
consumer on an anycast work queue would steal its requests — verifies liveness with a message round trip, restarts what
should be running, leaves alone what was deliberately stopped, and prunes reclaimable caches. Scheduled automation
carries the routine sweeps as a nightly catalog synchronization run by the operations agent: request-form ingest,
catalog imports, association and assimilation of production submitted outside the catalog workflow, Rucio output and
input snapshots, and cache refreshes — each step recording its outcome and execution time in the production action
stream, whose freshness the alarm system watches. The
intended steady state is a system that tends itself, where routine failure modes self-heal and what cannot self-heal
surfaces as an alarm.

## Service Ownership

Every service runs under an identified account holding exactly the credentials it needs, registers itself in the
monitor, and carries its operational artifacts — service unit, environment, scheduled supervision — as part of its
definition. Ownership is human as well: each service has a responsible operator and an operations document recording
how it is run, restarted, and diagnosed, with the
[production operations runbook](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_OPS.md) as the pattern. The runbook discipline
is how operational knowledge moves from individuals into the system.

## Computing Use Case Specifics

Each workflow domain adds its own procedures on the common model. Production operations run on the monthly campaign
cadence: a campaign is prepared, with infrastructure changes addressed and new physics datasets incorporated, then run,
reviewed, and closed out, with the production working group meeting on the same rhythm. Within the campaign, operations
center on steering, submission and retry, data product accounting, and the daily review that reports and assessments
support, documented in the production runbook. Testbed and streaming operations manage the agent set, workflow runs, and the
user namespaces that isolate concurrent work, documented with the testbed. Validation and analysis are service
postures: keep the availability, notification, assessment, and data access paths running. Datataking operations, as
streaming matures toward production use, adds around-the-clock operation and control room integration, where the
latencies demand automated detection and response, and where the butterfly model's two-site symmetry sets the outage
posture: processing fails over to the peer host lab and replication restores symmetry on recovery. The operations model
described here is designed with that endpoint in mind.

## Production regulation

Task admission, job generation and pilot supply have separate controls and
separate evidence. The pressure front checks live JEDI enforcement before
relying on bounded job generation; Harvester keeps fresh demand and worker
counts to replenish pilots. The two OSG queues share one capacity estimate.
Historical running peaks provide a reference for work-depth calculations.
Lower current occupancy does not establish unused available capacity and
does not hold task admission.
Multi-job pilots reduce replacement demand but do not eliminate the cold
start requirement. Configuration clocks, fixed waiting limits, synchronization,
verification and the boundary between admission holds and task retry control
are recorded in the [22 October regulation audit and implementation report](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/REGULATION_AUDIT_2026-10-22.md).

For GREX's eight-pilot allocations, lifetime sizing uses the current job
duration distribution. The 22 October follow-up changed newly submitted
allocations from five to twelve hours, with approximately eight to nine
hours of successive-job intake and at least three hours reserved for the
final job. Each pilot receives time remaining to the same allocation
deadline. The longer useful phase is intended to reduce the fraction lost
while an allocation waits for its last job; it does not eliminate that tail.
Already submitted pilots retain their transferred code and configuration.
The implementation report distinguishes installed policy from measured
acceptance, start latency and utilization of the new cohort.
