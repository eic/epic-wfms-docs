# References

This section collects the reference material of the documentation: reference documents and requirements material,
API and MCP references, and the glossary. The system diagrams are collected in the [Diagram Gallery](gallery.md).

## Reference Documents and Artifacts

- **This documentation — source repository**: <https://github.com/eic/epic-wfms-docs>
- **ePIC Distributed Workflow Management System requirements**: <https://www.overleaf.com/project/67bdf89a3d44a138da503dea>
- **The ePIC Streaming Computing Model**: <https://zenodo.org/records/14675920>
- **E0-E1 interface document** (the interface as understood in 2026; input to the September 2026 Streaming Computing Model formalization): <https://github.com/BNLNPPS/swf-testbed/blob/infra/baseline-v39/docs/e0-e1-interface.md>
- **ePIC Production System: Status and Plans** (ePIC S&C meeting talk, June 24 2026 — the definitive current (June 2026) description of the production system, with interface views and near-term plans): <https://docs.google.com/presentation/d/1Mhc5Isfq0dKOqYbf7fdFQvu7tM86gsKLYx542aYVL0U/edit>
- **Production bot demo video** (June 2026): <https://drive.google.com/file/d/1VXIJJHfCaqE2iK_5QawJNamciGhFVQEI/view>
- **PanDA documentation**: <https://panda-wms.readthedocs.io/>
- **PanDA paper**: <https://link.springer.com/article/10.1007/s41781-024-00114-3>
- **Rucio paper**: <https://link.springer.com/article/10.1007/s41781-019-0026-3>
- **iDDS paper**: <https://link.springer.com/article/10.1140/epjc/s10052-025-15275-7>
- **EIC/ePIC Software Statement of Principles**: <https://eic.github.io/activities/principles.html>
- **Streaming workflow testbed architecture**: <https://github.com/BNLNPPS/swf-testbed/blob/main/docs/architecture.md>
- **Testbed progress notes** (working document — meeting notes, progress highlights, technical detail): <https://docs.google.com/document/d/1PUoo-W6dCeOKsD4VubYTgSxBHBUb4D5dYfVy1oLYh7E/edit>
- **epicprod implementation repository**: <https://github.com/BNLNPPS/swf-monitor>
- **epicprod production domain repository** (production applications and documentation consolidate here; its `docs/ARCHITECTURE_MAP.md` records what lives where): <https://github.com/BNLNPPS/swf-epicprod>
- **PCS — Physics Configuration System**: <https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/PCS.md>
- **epicprod task catalog design**: <https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_TASK_CATALOG.md>
- **Production operations runbook**: <https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_OPS.md>
- **Production operations agent design**: <https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_OPS_AGENT.md>
- **Validation integration plan**: <https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_VALIDATION.md>
- **Production request questionnaire design**: <https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_QUESTIONNAIRE.md>
- **argus-ai assessment application design**: <https://github.com/BNLNPPS/corun-ai/blob/master/docs/argus-ai.md>

## API and MCP References

The programmatic interfaces are documented with the implementation:

- **swf-monitor REST API reference**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/API_REFERENCE.md>
- **swf-monitor MCP server overview**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP.md>
- **MCP tool catalog**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP_TOOL_REFERENCE.md>
- **MCP client setup**: <https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP_CLIENTS.md>
- **PanDA client and API documentation**: <https://panda-wms.readthedocs.io/en/latest/client/client.html>

## Glossary

- **DDM**: Distributed data management
- **Echelon**: The ePIC computing model's resource hierarchy: E0, E1, E2, and E3
- **EVGEN**: Event-generation data, the generator outputs consumed as production inputs
- **Harvester**: PanDA service that manages worker submission and execution at computing sites
- **iDDS**: intelligent Data Delivery Service, the workflow orchestration component of the PanDA ecosystem
- **JEDI**: The PanDA task definition and execution layer
- **MCP**: Model Context Protocol, the structured tool interface serving AI clients
- **PanDA**: Production and Distributed Analysis system used for distributed workload management
- **PCS**: Physics Configuration System, the epicprod subsystem for production configuration and campaign records
- **RECO**: Reconstruction output data products
- **Rucio**: Distributed data management system used for dataset, replica, and data-placement management
- **SSE**: Server-Sent Events, the push channel delivering asynchronous notifications to browser pages
- **STF**: Super time frame, an aggregate unit of streaming detector data used in post-DAQ processing
- **TF**: Time frame, a time-slice unit of streaming detector data
- **WFMS**: Workflow Management System
