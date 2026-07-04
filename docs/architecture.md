# Architecture

This section describes the overall WFMS design: common system infrastructure, data/control flow, human-in-the-loop
automation, and AI integration. It is the conceptual map of the system, sitting between the foundational requirements
and the specific implementation details.

## System Overview

The ePIC WFMS architecture is organized around a shared platform serving the multiple workflow domains described
in the previous section. The domains have varying operational requirements, but the architecture converges on common
services where practical, from workflow orchestration and data management through monitoring, human controls, and AI
assistance.

[![The ePIC Workflow Management System](diagrams/wfms_platform.svg)](diagrams/wfms_platform.svg)

The architecture is agent and service oriented, and prioritizes full access to system information at all detail
levels by operators, users and AI agents. Information management begins with a comprehensive, centralized back end database
capturing all system information and state. Persistent databases and document/artifact stores operating on a common
database service hold operational state and history, metadata, curated knowledge, assessments, comments, and reports.

Browser pages present operational views and controls, from high level
summaries to deep drill-down with full presentation of filterable metadata. Browser interfaces always capture all
state in the URL, for reproducibility, bookmarking and transparency.

REST APIs
support system workflow interrogation and control, service-to-service interaction, and automation.
MCP tools expose structured system context
to AI clients and bots, and, selectively and under controls, active functionality that AIs can exercise safely and reliably.

Agent services drawing on MCP and REST perform credentialed or long-running actions away from the web tier. They can be activated
in several ways: regular cron-like invocation, integration as discrete steps in a workflow, human triggered by natural language interaction
with a bot or LLM, or human triggered via web interface. Agents operate using no-latency messaging to/from an
asynchronous worker queue, accommodating the macroscopic times (seconds to minutes) that LLM and distributed service operations take to complete.

## Data and Control Flow

WFMS data flow begins with the data products and metadata produced by detector, simulation, reconstruction,
validation, and analysis workflows. In streaming workflows, the flow starts at the E0-E1 interface,
in data terms at the DAQ exit buffer, with time frame
and super time frame data driving registration, movement, monitoring, and prompt processing.

In production workflows,
the flow begins with community production requests leading (with human intervention) to corresponding physics configurations,
which are transformed into executable production tasks that produce the desired data products.

Control flows begin with humans or scheduled automated operations. System operators, production experts, validation experts,
and collaboration users interact through web interfaces, bots, REST clients, and analysis interfaces. These
points of interaction, at exposed surfaces such as web browsers and servers,
do not directly hold credentials to operate system services.
Credentialed operations are routed through designated agents
such as a production operations agent for interacting with distributed computing services, and LLM harness agents for
engaging AI assistance. This keeps privileged actions
secure, auditable, and bounded to only the appropriate exposure surface.

System state flows back through monitoring and notification channels. Services, agents, databases, logs, and
curated artifacts provide the state used by dashboards, diagnostics, AI assessments, campaign reports, and user-facing
overviews. Browser notification uses server-sent events where asynchronous work needs to report completion to an open
page.

## Human-in-the-Loop Automation

The architecture is based on maximal automation with explicit human control. AI-equipped automation should reduce routine operations
effort, expose system state, identify failures, present inferences and interpretations, and carry out approved bounded actions. It
does not remove the need for production experts, validation experts, and detector or physics domain experts to set
priorities, curate knowledge, approve operational changes, and interpret results. Agentic tools must incorporate appropriate
harnesses to assert controls and enforce predictable, responsible operation.

Human-in-the-loop operation appears at several levels:

- production requests and campaign scope are defined by people and structured by the system
- physics configuration systems encode production configurations in a form suitable for task generation and review
- production experts control task submission, retry, recovery, and campaign steering
- validation experts evaluate produced data and feed readiness decisions back into production
- AI assessments and reports support review, but do not replace operational responsibility; they inform actions leaving humans to drive them
- curated campaign narratives and comments provide context for later assessment and decision making

The architecture favors visible state, explicit control points, auditable actions, and fast feedback loops.

## AI Integration

AI services consume
structured WFMS context and produce assessments, comments, reports, summaries, and recommendations. Operational
authority remains with the relevant human and programmatic/deterministic service components. If and when confidence in
granting AI actionable functionality is established, the same programmatic action interfaces that humans operate can
be made available to AIs, e.g. through appropriate MCP tools.

The same architectural pattern applies beyond production. Streaming workflows, validation, calibration, distributed
CI, and analysis can all expose structured state through APIs and MCP tools. AI systems can then reason over current
and historical state, curated campaign knowledge, produced artifacts, validation outcomes, and operational logs. The
useful role of AI is to improve assessment, diagnosis, summarization, and ideation while keeping the WFMS state and
action paths explicit.

The architectural rule is that AI outputs become artifacts in the system. They should carry provenance, be attached to
the relevant production or workflow object, be open to human (and AI) comment where appropriate, and be available as context
for later reports or assessments. AI is very new, any application of it is an R&D exercise, and use of it must accordingly
accommodate correcting, qualifying or ignoring its products as appropriate, and trying and comparing different
models and approaches.
