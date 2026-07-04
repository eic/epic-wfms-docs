# Production System

This section documents epicprod, the ePIC automated production system: request intake, physics configuration,
campaign management, PanDA execution, data products, LLM assessments and reports, and the human controls and
curation that steer it.

## epicprod Overview

epicprod is the automated production system running ePIC simulation and reconstruction campaigns. It carries a
production request from community submission through physics configuration, campaign preparation, PanDA execution, and
cataloged data products, with AI assistance and human control points along the whole path. The operating principle set
in Foundations, maximal automation with minimal operations effort, shapes each stage: the routine mechanics are
automated, and people make the decisions. The implementation lives in the
[swf-monitor repository](https://github.com/BNLNPPS/swf-monitor), whose documentation carries the design and
operational detail behind this section. The definitive current (June 2026) description of the system as deployed —
status, interface views, and near-term plans — is the S&C talk
[ePIC Production System: Status and Plans](https://docs.google.com/presentation/d/1Mhc5Isfq0dKOqYbf7fdFQvu7tM86gsKLYx542aYVL0U/edit).

[![epicprod production system](diagrams/epicprod_system.svg)](diagrams/epicprod_system.svg)

## Production Requests

Physics working groups and detector groups request production datasets through the collaboration's request form. PCS
mirrors each form response into a read-only questionnaire record, giving the collaboration a browsable view of all
requests and giving production records a single upstream reference for request provenance
([questionnaire design](https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_QUESTIONNAIRE.md)). The request
cycle follows the collaboration's monthly campaign rhythm: requests are coordinated through the physics working groups
and detector subsystem collaborations, validated by the production working group, and prioritized through the
collaboration's physics and technical coordination before the monthly production list is frozen for the campaign.

Triage turns submissions into structured production records. An operator links a response to one or more production
request records — one submission frequently spans several beam energies or Q² ranges — and composes each request from
PCS tags and a production configuration. A request is deliberately more abstract than an output: it specifies the
physics, beam energies, and kinematic range, and one request commonly leads to several produced datasets. Provenance is
by reference: a task resolves through its request to the originating submission, contact, and estimates without
duplicating them.

## Physics Configuration System (PCS)

PCS is the configuration layer of epicprod: the catalog of physics and processing definitions — tags, datasets,
sample variants, and production configs — from which production tasks are composed, with identity carried through
composed names. As the principal place where physicists meet the production system, it has its own section:
[Physics Configuration System](pcs.md).

## Campaign Management

Campaigns are time-ordered groupings of production tasks, named by year and month (25.10, 26.06). The production task
catalog is the instrument of campaign management: tasks composed from PCS configuration entities, carrying their full
parameter sets, staged by campaign lifecycle
([task catalog design](https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_TASK_CATALOG.md)).

Prepping campaigns are mutable: operators add new tasks and clones, adjust priorities, withdraw
entries, and move tasks from draft to ready under readiness checks. The current campaign is the live one: ready tasks
are submitted, and the catalog presents live status from PanDA and Rucio with diagnostic drill-down, analytics, and AI
monitoring. Past campaigns are a frozen archive with all task parameters preserved. Pre-PCS production has been
assimilated into past campaigns, making the catalog the complete ePIC production record.

[![epicprod task catalog](diagrams/epicprod_task_catalog.svg)](diagrams/epicprod_task_catalog.svg)

Each campaign carries a human-authored campaign narrative recording its goals, priorities, and evolution. The narrative
gives operators and LLMs a shared context: daily campaign reports and assessments reason against it, and it accumulates
the campaign's history as decisions are made.

## PanDA Execution

Task submission is a catalog action: the composed task specification is submitted through the production operations
agent to PanDA, and each physical submission attempt is recorded on the task as a PanDA task association. The
submission mechanics, task naming of retries, and the science-data constraint that has production payloads stage EVGEN
inputs from and register outputs to JLab Rucio are described in Platform.

Live execution state flows back to the catalog and the ePIC PanDA monitoring views: task and job status, error
summaries, queue and site state, and resource usage. Payload logs are retrievable on demand from the task pages.
Operators steer execution with retry, recovery, and priority controls, and the alarm system carries execution
conditions that need attention.

## Data Products

[![ePIC production dataflow](diagrams/epicprod_dataflow.svg)](diagrams/epicprod_dataflow.svg)

Produced data are cataloged as the primary product of the system. Outputs are registered in JLab Rucio under the
composed task name: RECO reconstruction outputs and the associated log datasets. The catalog
gathers this lineage onto the task record, linking expected and observed outputs with their Rucio identifiers, status,
and access references, so a physicist can go from a physics configuration to its data products in one place.

Third-party event-generation inputs are cataloged on the same footing. EVGEN datasets in JLab Rucio are swept into the
catalog and matched to the requests they serve, so a task's inputs and outputs are both visible beside the
configuration that consumes and produces them. On-the-fly event generation in the production payload is the planned
evolution of the input path, replacing staged inputs where generators support it, beginning with a Pythia8 proof of
concept.

## AI Assistance

AI assistance appears throughout the production pages as durable, attributed artifacts. Assessments evaluate tasks,
jobs, queues, and campaigns and are attached to the objects they assess. Comment threads on production objects carry
discussion between operators, and an LLM participates in the thread on request. Daily campaign reports analyze status
and progress against the campaign narrative. Each artifact records its model and prompt provenance and is open to
comment, following the Architecture rule that AI outputs become artifacts in the system.

The assistance is delivered through the corun-ai and wrangle-ai services described in Platform: a page action requests
the LLM operation, and the result is pushed to the requesting page the moment it completes. A production bot provides a
conversational channel to the same system state for questions and diagnostics in chat.

### Detailed epicprod LLM Operations Architecture

The architecture of the LLM operations path — the production pages, the LLM services, the credentialed operations
agent, and the notification return — is diagrammed below.

[![Detailed epicprod LLM operations architecture](diagrams/epicprod_llm_ops_architecture.svg)](diagrams/epicprod_llm_ops_architecture.svg)

## Human Controls and Curation

Canonical state changes by human hand. Lifecycle transitions — draft to ready, submission, lock, withdraw, retry and
recovery — are operator decisions exercised through catalog controls. Automation and AI may detect a condition, present
an interpretation, and surface the control that acts on it, and the human decides. Read access to the production pages
is open to the collaboration on both the internal and external faces; actions are gated by login and role, and
privileged execution stays behind the operations agent.

Curation is the human side of the automation bargain. Production experts maintain the campaign narratives, the curated
knowledge the LLMs reason from, and the priorities that steer the work; they review AI assessments and reports rather
than inherit them as fact. The system records these judgments — narratives, comments, decisions — so that the context
available to the next assessment, human or AI, keeps improving.
