---
hide:
  - toc
---

# Diagram Gallery

The system diagrams, collected from across the documentation. Each image links to the full-size SVG; the noted section carries the surrounding description.

### The ePIC Computing Model

In [Foundations](foundations.md) — the Echelon model: E0 detector and DAQ, the butterfly raw-data fan-out to the E1 host labs, E2 global facilities, and E3.

[![The ePIC computing model](diagrams/epic_computing_model.svg)](diagrams/epic_computing_model.svg)

### Lifecycles

In [Concepts](concepts.md) — the state machines of the campaign task (with PanDA tail retry and operator rerun controls), the campaign staging, and the tag lock.

[![Lifecycles](diagrams/lifecycles.svg)](diagrams/lifecycles.svg)

### The ePIC Workflow Management System

In [Architecture](architecture.md) — the platform anchor: workflow domains served by shared web/database, agent, AI, data and workflow management layers over the Echelon resources.

[![The ePIC Workflow Management System](diagrams/wfms_platform.svg)](diagrams/wfms_platform.svg)

### PanDA in ePIC

In [WFMS Platform](platform.md) — the deployed workload management infrastructure: the two fronts driving PanDA at BNL, identity, the ePIC monitor, and the growing resource landscape.

[![PanDA in ePIC](diagrams/panda_in_epic.svg)](diagrams/panda_in_epic.svg)

### ePIC AI Infrastructure Stack

In [WFMS Platform](platform.md) — ePIC services, the MCP instrumentation over them, and the AI services built on top.

[![ePIC AI infrastructure stack](diagrams/epic_ai_stack.svg)](diagrams/epic_ai_stack.svg)

### corun-ai — LLM Execution and Artifact Service

In [WFMS Platform](platform.md) — the corun-ai system: an interactive research site and the REST AI back end of the WFMS, sharing one execution machinery and artifact store.

[![corun-ai — LLM execution and artifact service](diagrams/corun_ai.svg)](diagrams/corun_ai.svg)

### LLM and Automated Services in epicprod

In [WFMS Platform](platform.md) — human-gated LLM assistance and credentialed automation.

[![LLM and automated services in epicprod](diagrams/epicprod_llm_ops_highlevel_tw.svg)](diagrams/epicprod_llm_ops_highlevel_tw.svg)

### E0-E1 Workflow Schematic

In [Streaming Workflows](streaming.md) — the E0-E1 interface: DAQ exit buffer, STF and TF streams to the E1 facilities, and the streaming workflow testbed scope.

[![E0-E1 workflow schematic](diagrams/E0-E1_workflow_schematic.svg)](diagrams/E0-E1_workflow_schematic.svg)

### Prompt Processing Workflow

In [Streaming Workflows](streaming.md) — full-sample processing of every STF as it arrives, from run signals through the filling run dataset to PanDA jobs at the E1s, with the conceptual decision box.

[![Prompt processing workflow](diagrams/prompt_processing_workflow.svg)](diagrams/prompt_processing_workflow.svg)

### Fast Processing Pipeline

In [Streaming Workflows](streaming.md) — the testbed fast-processing pipeline from simulated DAQ through TF slices to the standing worker pool.

[![Fast processing pipeline](diagrams/fast-processing-pipeline-v10.svg)](diagrams/fast-processing-pipeline-v10.svg)

### iDDS/PanDA/Harvester Detail

In [Streaming Workflows](streaming.md) — worker provisioning behind the fast-processing pool.

[![iDDS PanDA detail](diagrams/idds-panda-detail-v1.svg)](diagrams/idds-panda-detail-v1.svg)

### Testbed Agent Management

In [Streaming Workflows](streaming.md) — how testbed agents are configured, launched, and supervised: CLI and MCP control, the per-user agent manager, and supervisord.

[![Testbed agent management](diagrams/testbed_agent_management.svg)](diagrams/testbed_agent_management.svg)

### Testbed Multi-User Isolation

In [Streaming Workflows](streaming.md) — shared infrastructure with independent per-user operation: namespaces, per-user agent identity, and filtered views.

[![Testbed multi-user isolation](diagrams/testbed_multi_user.svg)](diagrams/testbed_multi_user.svg)

### epicprod — the ePIC Production System

In [Production System](production.md) — the production workflow stages, LLM services, and credentialed operations of epicprod.

[![epicprod production system](diagrams/epicprod_system.svg)](diagrams/epicprod_system.svg)

### ePIC Automated Production Workflow

In [Production System](production.md) — the production workflow and the task catalog staged by campaign lifecycle.

[![ePIC automated production workflow](diagrams/epicprod_task_catalog.svg)](diagrams/epicprod_task_catalog.svg)

### ePIC Production Dataflow

In [Production System](production.md) — job orchestration and the payload-handled science data path against JLab Rucio.

[![ePIC production dataflow](diagrams/epicprod_dataflow.svg)](diagrams/epicprod_dataflow.svg)

### LLM and Distributed Computing Services Integration — Detailed Architecture

In [Production System](production.md) — the detailed LLM operations architecture: SSE relay, LLM executors, credentialed agent, and artifact store.

[![Detailed epicprod LLM operations architecture](diagrams/epicprod_llm_ops_architecture.svg)](diagrams/epicprod_llm_ops_architecture.svg)

### The Validation Loop

In [Validation](validation.md) — availability, Hydra validation, AI assessment, record, and expert signoff between the WFMS and the ePIC validation program; proposal-stage interfaces dashed.

[![The validation loop](diagrams/validation_loop.svg)](diagrams/validation_loop.svg)

### The WFMS Timeline

In [Timeline](timeline.md) — the three-year plan and the decade arc to physics datataking.

[![The WFMS timeline](diagrams/wfms_timeline.svg)](diagrams/wfms_timeline.svg)

### Streaming Computing Planning — FY25–FY31

In [Timeline](timeline.md) — the joint DAQ, computing, and AI planning lanes, the context for the WFMS out-years.

[![Streaming computing planning FY25-FY31](diagrams/streaming_planning_fy.svg)](diagrams/streaming_planning_fy.svg)
