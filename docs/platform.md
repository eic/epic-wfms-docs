# WFMS Platform

This section covers the specific technical platform used to build the ePIC WFMS across streaming, production, validation,
distributed analysis, calibration, distributed CI, and related workflow domains. With it we pass from technology
agnostic architecture to implementation specifics. It documents the concrete systems,
services, libraries, interfaces, and conventions used to realize the architecture described in the previous section.

The platform is developing through two active implementation fronts: the streaming workflow testbed and the epicprod production system. These
fronts have different near-term purposes, but they are deliberately based on the same substrate: PanDA and related
workflow services, Rucio and XRootD data handling, message-driven agents, a shared monitor/database service, REST and
MCP interfaces, browser-based operational pages, AI bot, and harnessed LLM AI services.

## Common Technical Platform

### Platform Role

The common platform is the concrete implementation layer beneath the WFMS workflow domains. It consists of the shared
technologies, code patterns, services, and operational conventions used by the current testbed and production systems.
Domain-specific sections describe how the platform is applied in each workflow domain.

### Production And Testbed Convergence

The production system and streaming workflow testbed exercise the same platform from different directions. Production
has immediate operational pressure: campaign definition, task creation, PanDA execution, data product accounting,
monitoring, human controls, and operations automation. The testbed exercises the datataking side: E0-E1-E2 streaming
processing, message-driven agents, fast processing, Rucio data handling, and prompt monitoring.

Several production components have testbed relevance. The Physics Configuration System provides a dynamic, editable,
composable catalog model for task creation. Rucio-based input ingest and PanDA submission are production needs today and
testbed needs for composed streaming-processing tasks. The task catalog's browsing, state, controls, and copy/edit
patterns can also support testbed namespaces, data challenges, and future streaming exercises.

The ePIC-specific monitor originated in the testbed and now supports both production and testbed development. Bot
interfaces, alarm handling, operations agents, MCP tools, and LLM-backed assessment services are shared capabilities
with different authorization and action policies by use case. Production does not expose general proactive workflow
actions through the general bot. The testbed may use more active bot or agent behavior where that is appropriate for
workflow experimentation.

corun-ai extends the platform with LLM-backed operations and durable document artifacts. Its production role begins with
assessments, comments, campaign narratives, and reports. Its testbed category is available for deeper analytics on
streaming workflow behavior as the testbed matures.

### Repository Organization

The `swf-*` repositories implement the current platform. `swf-testbed` is the umbrella repository for testbed
configuration, orchestration, and documentation. `swf-monitor` provides the Django web application, database-backed
monitoring, REST APIs, MCP server, production pages, and epicprod implementation. `swf-common-lib` provides shared
agent, messaging, logging, and Rucio helper code. Agent repositories such as `swf-daqsim-agent`, `swf-data-agent`,
`swf-processing-agent`, and `swf-fastmon-agent` implement specific testbed roles.

Cross-repository development is coordinated when a platform change spans repositories. Common code that is used by more
than one component belongs in `swf-common-lib`, not in copied local utilities.

## Web And Database Stack

### swf-monitor

`swf-monitor` is the central web and database application for the present platform. It serves both the testbed and
epicprod, with the historical name now covering more than monitoring. It provides browser pages, REST APIs, MCP tools,
message history, agent state, PanDA monitoring views, PCS, task catalogs, and LLM assessment integration.

### Database-Backed Operational State

The monitor database stores operational state that must be queried, filtered, linked, audited, or rendered. It stores
current state and history rather than only transient status. Testbed records include runs, agents, messages, files,
workflow executions, and fast monitoring state. Production records include requests, PCS entities, campaign tasks,
PanDA associations, operator state, cached system status, LLM artifact pointers, and production metadata.

Django models and migrations define the current schema. JSON fields are used where a record needs extensible metadata
without prematurely fixing every field as a column. Structured fields are used where filtering, linking, constraints, or
operator workflows require them.

### Browser Page Implementation

Browser pages are implemented as server-rendered Django pages with targeted JavaScript for filtering, selection,
asynchronous actions, and notification. Page state that affects interpretation should be represented in the URL:
selected task, active tab, filters, sorting, and similar controls. This makes views bookmarkable, shareable, and usable
as stable references in operations discussions.

Pages that trigger long-running or credentialed work enqueue an agent request and return promptly. Completion is shown
from database state, cache state, or browser notification.

### Server-Sent Events

Server-Sent Events are the browser notification mechanism for asynchronous completion. swf-monitor consumes message-bus
events, persists relevant messages, and relays selected events to browsers through `/api/messages/stream/`. Production
uses the same pattern for operations-agent completion and corun-ai callback completion. SSE is a notification path, not
the source of truth; pages refresh database or REST state after receiving the notice.

## Workflow And Workload Management

### PanDA

PanDA is the distributed workload management system used for production execution and testbed workflow processing. It
turns task specifications into jobs, brokers work to sites, and records task and job state. epicprod uses PanDA for
campaign tasks. The testbed uses it as the execution substrate for prompt and streaming workflow prototypes.

PanDA task and job state is presented in swf-monitor through ePIC-specific task, job, queue, and system views. These
views supplement the generic BigPanDA monitor with production-specific task links, campaign context, payload-log access,
Rucio output views, and LLM assessments.

### JEDI

JEDI is the PanDA task definition and execution layer used for direct production task submission from PCS. PCS builds the
task specification, maps PCS fields into a JEDI `taskParamMap`, and queues the credentialed submission through the
production operations agent. The live epicprod path uses the PanDA client API for EVGEN production tasks and records each
physical submission attempt as a PanDA task association.

The JEDI integration also defines the distinction between logical campaign task identity and physical PanDA/Rucio attempt
names. The logical identity remains stable in PCS. Physical submissions may append `.tryN` so reruns and future site
racing have unique PanDA task names and output namespaces.

### iDDS

iDDS is part of the broader PanDA ecosystem for intelligent data delivery and workflow orchestration. It is relevant to
multi-stage and data-driven workflows where data availability, transformation, and workflow state must be coordinated
beyond simple task submission. The current documentation includes the iDDS/PanDA detail view as a candidate pattern for
future streaming and production workflow expansion.

### Workflow Descriptions

The testbed uses a layered workflow model. TOML holds human-editable configuration and parameters. Python/SimPy supports
execution and simulation patterns that need rapid iteration. Snakemake is the candidate layer for workflows where
dependency management is central, such as calibration or other multi-step orchestration.

## Data Management

### Rucio

Rucio is the distributed data management system used by the platform. In the testbed it manages run datasets, STF-file
registration, subscriptions, transfer rules, and RSE state. In production it records and exposes production data products,
EVGEN inputs, RECO/FULL outputs, and log datasets, subject to the production constraint described below.

Rucio DIDs, scopes, RSEs, rules, replicas, and metadata are operational objects, not only storage references.
Rucio-derived state is surfaced beside workflow state in monitor pages and task catalogs.

### XRootD And FTS

XRootD is the file access and transfer protocol used by the testbed and production paths. Rucio can drive movement
through FTS. Agents and doer scripts may also use XRootD directly for bounded operations such as payload-log retrieval
or testbed data movement. The testbed maps DAQ and E1 RSEs onto XRootD-accessible storage areas to emulate the E0-E1
dataflow.

### Production Science-Data Constraint

The production PanDA server is configured with one Rucio instance. The BNL PanDA server used for ePIC production uses BNL
Rucio, where PanDA records logs. ePIC production science data is held in JLab Rucio. As a result, production payloads
handle science-data movement and registration directly against JLab Rucio. PanDA does not resolve, transfer, or register
the science data on either the input or output side for the current production path.

This constraint does not prevent use of the common copytool pattern inside payload-side data handling. It does require
the platform to keep PanDA-managed logs and JLab-Rucio science outputs distinct in implementation and monitoring.

### Data Product Cataloging

Data products are cataloged as operational objects. Production campaign tasks link to expected and observed outputs,
including Rucio DIDs, output status, logs, and PanDA task associations. The testbed records run, STF, TF, and
workflow-stage metadata. Workflow state and data-product state should be inspectable together.

## Distributed Resources Integration

### Echelon-Aware Resource Model

Foundations defines the Echelon model. The platform expresses that model through workflow targets, data locations, site
state, queue state, and monitoring views. The same abstractions must accommodate present testbed emulation and future
facility-scale operation.

### PanDA Queues, Pilots, And Harvester

PanDA represents compute execution through sites and queues. Harvester and pilot infrastructure connect PanDA tasks to
the batch or facility execution layer. swf-monitor presents task, job, queue, site, resource usage, and harvester-worker
state so operators can diagnose failures at the level of the campaign task, PanDA task, job, queue, or site.

### Testbed Resource Emulation

The testbed emulates elements of the E0-E1-E2 workflow using local services and configured RSEs. DAQ buffer and E1 storage
roles can be represented by distinct RSEs and XRootD paths even when they are implemented on the same host during
development. This allows workflow and dataflow logic to be exercised before the physical facilities and final data paths
exist.

## Metadata And APIs

### REST APIs

REST APIs provide the programmatic interface for browser pages, scripts, agents, service-to-service calls, and
automation. Command-line clients and operational scripts should use REST endpoints rather than importing Django internals
or querying the database directly.

REST APIs should return structured errors, preserve stable identifiers, and represent the same state shown in the browser.
When write actions must work through the remote proxy, the endpoint shape must be proxy-safe: JSON response, no session
or CSRF dependence where the proxy cannot carry it, and no redirect as the action result.

### MCP Tools

MCP is the structured LLM-facing API for the platform. swf-monitor exposes MCP over a FastMCP ASGI worker separate from
the Django WSGI web site. Tools expose testbed state, production state, PanDA monitoring, PCS entities, LLM artifacts,
and selected bounded actions.

MCP tools should be designed as data access and bounded action primitives. Tool docstrings are operational metadata
because they are the primary text an LLM sees when deciding what to call. List tools should support filtering,
pagination, and stable returned identifiers. Tools that expose actions should route through the same service layer and
agent execution paths used by browser and REST actions.

### Metadata Conventions

The platform relies on stable identifiers: campaign task composed names, PanDA JEDI task IDs, PanDA job IDs, Rucio DIDs,
RSE names, agent names, workflow execution IDs, section slugs, and document artifact group IDs. JSON metadata should
identify source system, artifact type, subject reference, producing user or service, and relevant model or prompt
provenance for LLM-generated artifacts.

## Agents And Services

### BaseAgent

`BaseAgent` in `swf-common-lib` is the shared agent base. It provides STOMP/ActiveMQ integration, monitor registration,
heartbeats, namespace filtering, message dispatch, REST logging, and background execution support. Agents that inherit
from it are visible in the monitor and follow common message and status conventions.

`BaseAgent.run_in_background()` provides bounded background execution for handlers that call subprocesses, REST services,
Rucio, XRootD, or other potentially slow services. This keeps the receiver thread responsive to liveness and control
messages while work completes in a worker pool.

### ActiveMQ Artemis

ActiveMQ Artemis is the message broker. Topics provide broadcast event flow, while queues provide anycast work delivery.
Testbed workflow messages use broadcast topics for events such as run state and STF availability. Production operations
use an anycast control queue for single-consumer credentialed work. Destination names should include the explicit
`/topic/` or `/queue/` prefix.

Durable subscriptions are used with care because they create broker-side state and can accumulate messages if not
managed. Work queues and broadcast topics should be chosen according to delivery semantics rather than convenience.

### Testbed Agents

The testbed agent set models the streaming workflow. `swf-daqsim-agent` simulates DAQ state and STF generation.
`swf-data-agent` receives DAQ messages, creates run datasets, manages Rucio STF handling, and notifies processing and fast
monitoring. `swf-processing-agent` submits or manages PanDA processing tasks. `swf-fastmon-agent` consumes STF
availability, samples TF-level information, records metadata through REST, and publishes notification events for
real-time monitoring.

### Production Operations Agent

`epicprod_ops_agent` is the always-on credentialed executor for production. The web tier, REST endpoints, MCP tools,
bots, and scheduled jobs can request work, but privileged actions are performed by the agent. Current actions include
PanDA submission, payload-log retrieval, Rucio snapshot updates, and PanDA task operations.

The agent follows a handler plus doer pattern. The handler validates and queues work; the doer script performs the
credentialed operation as a subprocess. This keeps capabilities reusable from cron or operator scripts and keeps
privileged service logic outside the browser request.

### Bot Interfaces

The bot interface is a natural-language and chat-facing layer over MCP tools and selected REST-backed operations.
Production bot behavior must remain constrained: production does not support proactive workflow actions through the
general bot. A separate testbed bot or testbed-specific mode may support more active workflow experimentation.

### Alarms

The alarm system is a platform capability for surfacing actionable state. It applies naturally to production operations
and has direct relevance to testbed and eventual E0-E1 operations. Alarms should be derived from monitored state,
attached to the relevant object or service, and visible in both detailed and summary views.

### corun-ai And wrangle-ai

corun-ai provides LLM-backed operations and durable artifacts. For epicprod, swf-monitor supplies production context and
renders the production-facing pages, while corun-ai stores assessments, comments, campaign narratives, and reports.
swf-monitor records pointers to these artifacts rather than copying generated content into production records.

wrangle-ai is the rapid asynchronous worker substrate for bounded LLM operations such as comment replies or assessment
probes. For browser-triggered LLM operations, swf-monitor calls corun-ai REST, corun-ai creates and executes a work item,
and completion returns to swf-monitor through a callback that is converted into an SSE browser notification.

[![High-level epicprod LLM and distributed computing integration](diagrams/epicprod_llm_ops_highlevel_tw.svg)](diagrams/epicprod_llm_ops_highlevel_tw.svg)

## Authentication

### User Authentication

Browser access is authenticated according to deployment surface. The internal `pandaserver02` site uses BNL-facing
authentication. The external proxy at `epic-devcloud.org/prod` provides collaboration access through swf-remote and the
production URL prefix. Browser authorization must distinguish read-only access, production request actions, operator
actions, and privileged service execution.

### Service Authentication

Service credentials are held by the service that needs them, not by every caller. PanDA OIDC tokens, Rucio x509 proxies,
XRootD access credentials, and LLM service tokens belong in the appropriate agent or service environment.

### Credentialed Action Boundary

Privileged production actions route through `epicprod_ops_agent`. The web tier can read database state, read
world-readable cache artifacts, and enqueue work. It should not run PanDA clients, Rucio clients, or XRootD transfers
with production credentials. MCP follows the same rule: it is an LLM-facing API surface, not the credentialed executor.

### Remote Proxy Constraints

The external proxy is part of the production surface and must be treated as an implementation constraint. URLs intended
for external collaborators must work under `/prod/`. Write actions that need to pass through the proxy should use
proxy-safe REST patterns and JSON results. Browser pages should make remote limitations visible where a control is
available only on `pandaserver02`.

### TLS And Certificate Handling

BNL internal services use a private certificate chain. Platform scripts and agents use a combined trust bundle so both
BNL services and public HTTPS endpoints can be verified. Certificate and proxy configuration belongs in deployment
configuration and agent environments, not in browser code or source-controlled secrets.
