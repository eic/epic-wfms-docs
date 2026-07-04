# References

Collects reference documents, glossary terms, external links, API references, MCP references, diagrams, and requirements material.

## Diagrams

The system diagrams, collected from across the documentation. Each image links to the full-size SVG; the noted section carries the surrounding description.

### The ePIC Computing Model

In [Foundations](foundations.md) — the Echelon model: E0 detector and DAQ, the butterfly raw-data fan-out to the E1 host labs, E2 global facilities, and E3.

[![The ePIC computing model](diagrams/epic_computing_model.svg)](diagrams/epic_computing_model.svg)

### The ePIC Workflow Management System

In [Architecture](architecture.md) — the platform anchor: workflow domains served by shared web/database, agent, AI, data and workflow management layers over the Echelon resources.

[![The ePIC Workflow Management System](diagrams/wfms_platform.svg)](diagrams/wfms_platform.svg)

### ePIC AI Infrastructure Stack

In [WFMS Platform](platform.md) — ePIC services, the MCP instrumentation over them, and the AI services built on top.

[![ePIC AI infrastructure stack](diagrams/epic_ai_stack.svg)](diagrams/epic_ai_stack.svg)

### LLM and Automated Services in epicprod

In [WFMS Platform](platform.md) — human-gated LLM assistance and credentialed automation.

[![LLM and automated services in epicprod](diagrams/epicprod_llm_ops_highlevel_tw.svg)](diagrams/epicprod_llm_ops_highlevel_tw.svg)

### E0-E1 Workflow Schematic

In [Streaming Workflows](streaming.md) — the E0-E1 interface: DAQ exit buffer, STF and TF streams to the E1 facilities, and the streaming workflow testbed scope.

[![E0-E1 workflow schematic](diagrams/E0-E1_workflow_schematic.svg)](diagrams/E0-E1_workflow_schematic.svg)

### Fast Processing Pipeline

In [Streaming Workflows](streaming.md) — the testbed fast-processing pipeline from simulated DAQ through TF slices to the standing worker pool.

[![Fast processing pipeline](diagrams/fast-processing-pipeline-v10.svg)](diagrams/fast-processing-pipeline-v10.svg)

### iDDS/PanDA/Harvester Detail

In [Streaming Workflows](streaming.md) — worker provisioning behind the fast-processing pool.

[![iDDS PanDA detail](diagrams/idds-panda-detail-v1.svg)](diagrams/idds-panda-detail-v1.svg)

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

## Reference documents and artifacts

- **This documentation — source repository**: <https://github.com/eic/epic-wfms-docs>
- **ePIC Distributed Workflow Management System requirements**: <https://www.overleaf.com/project/67bdf89a3d44a138da503dea>
- **The ePIC Streaming Computing Model**: <https://zenodo.org/records/14675920>
- **PanDA documentation**: <https://panda-wms.readthedocs.io/>
- **PanDA paper**: <https://link.springer.com/article/10.1007/s41781-024-00114-3>
- **Rucio paper**: <https://link.springer.com/article/10.1007/s41781-019-0026-3>
- **iDDS paper**: <https://link.springer.com/article/10.1140/epjc/s10052-025-15275-7>
- **EIC/ePIC Software Statement of Principles**: <https://eic.github.io/activities/principles.html>
- **Streaming workflow testbed architecture**: <https://github.com/BNLNPPS/swf-testbed/blob/main/docs/architecture.md>
- **epicprod implementation repository**: <https://github.com/BNLNPPS/swf-monitor>
- **PCS — Physics Configuration System**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/PCS.md>
- **epicprod task catalog design**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_TASK_CATALOG.md>
- **Production operations runbook**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_OPS.md>
- **Production operations agent design**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_OPS_AGENT.md>
- **Validation integration plan**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_VALIDATION.md>
- **Production request questionnaire design**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_QUESTIONNAIRE.md>
- **argus-ai assessment application design**: <https://github.com/BNLNPPS/corun-ai/blob/master/docs/argus-ai.md>

## API and MCP references

The programmatic interfaces are documented with the implementation:

- **swf-monitor REST API reference**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/API_REFERENCE.md>
- **swf-monitor MCP server overview**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP.md>
- **MCP tool catalog**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP_TOOL_REFERENCE.md>
- **MCP client setup**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP_CLIENTS.md>
- **PanDA client and API documentation**: <https://panda-wms.readthedocs.io/en/latest/client/client.html>

## Glossary

- **DDM**: Distributed data management
- **Echelon**: The ePIC computing model's resource hierarchy: E0, E1, E2, and E3
- **Harvester**: PanDA service that manages worker submission and execution at computing sites
- **PanDA**: Production and Distributed Analysis system used for distributed workload management
- **PCS**: Physics Configuration System, the epicprod subsystem for production configuration and campaign records
- **Rucio**: Distributed data management system used for dataset, replica, and data-placement management
- **STF**: Super timeframe, an aggregate unit of streaming detector data used in post-DAQ processing
- **TF**: Timeframe, a time-slice unit of streaming detector data
- **WFMS**: Workflow Management System
