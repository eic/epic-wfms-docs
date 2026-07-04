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

The credentialed operations agent is deliberately decoupled from routine deploys: the doer scripts it dispatches run
fresh from the deploy tree, so a script fix is live on the next dispatch, while the agent process itself is restarted
only by deliberate operator action. This documentation follows the same continuous practice, rebuilding on every push.

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

Incident response is drill-down and bounded action. Diagnosis runs from the campaign task to the PanDA task, job,
queue, or site, with error summaries at each level and the complete payload log one click from the job page. An AI
assessment can be requested on the spot to summarize and interpret what the operator is looking at. Response actions —
retry, recovery, resubmission, priority changes — are the same catalog controls used in routine operation, executed
through the operations agent and recorded on the production record.

Incidents are as often data-side as processing-side. Transfer failures, storage pressure, log-upload contention, and
dataset integrity carry the same discipline: surfaced, diagnosed through the data management views, and resolved with
recorded actions.

## Automation and Agents

Always-on services follow one operational pattern: systemd-managed with automatic restart, burst-capped so a
persistently failing service lands in a visible failed state instead of flapping indefinitely, and with a deliberate
stop distinguished from a crash so supervision does not fight an operator's intent.

Autonomous supervision closes the loop. A scheduled supervisor keeps the credentialed agent a true singleton — a second
consumer on an anycast work queue would steal its requests — verifies liveness with a message round trip, restarts what
should be running, leaves alone what was deliberately stopped, and prunes reclaimable caches. Scheduled automation also
carries the routine sweeps: system status refresh, data lineage snapshots, request ingest, and daily reports. The
intended steady state is a system that tends itself, where routine failure modes self-heal and what cannot self-heal
surfaces as an alarm.

## Service Ownership

Every service runs under an identified account holding exactly the credentials it needs, registers itself in the
monitor, and carries its operational artifacts — service unit, environment, scheduled supervision — as part of its
definition. Ownership is human as well: each service has a responsible operator and an operations document recording
how it is run, restarted, and diagnosed, with the
[production operations runbook](https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_OPS.md) as the pattern. The runbook discipline
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
