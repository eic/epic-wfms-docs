# ePIC Workflow Management System

The ePIC Workflow Management System (WFMS) provides the shared workflow, data-management, monitoring, automation, and operations layer for ePIC computing.

The system spans post-DAQ streaming processing, global production campaigns, validation workflows, calibration, distributed CI, and analysis workflow support. These are workflow domains on one common distributed platform rather than separate systems. Two implementation fronts operate today — the streaming workflow testbed and the epicprod automated production system — building toward the full model.

## Documentation Structure

- **Foundations** defines the WFMS scope, requirements basis, streaming computing model alignment, computing use cases, Echelon model, and butterfly model
- **Concepts** defines the working vocabulary of the system: streaming data units, configuration and identity, requests, campaign tasks, campaigns, and their lifecycles
- **Architecture** describes the overall WFMS design: common system structure, data/control flow, human-in-the-loop automation, AI integration
- **WFMS Platform** covers the realization of the architecture with specific technology and implementation choices
- **Streaming Workflows** documents post-DAQ workflows during datataking
- **Production System** documents the epicprod automated production system
- **Physics Configuration System** documents PCS, where physicists meet the production system: the tag catalog, dataset composition, composed-name identity, and the browse and compose interface
- **Validation** documents WFMS support for ePIC validation activities
- **Calibration** documents WFMS support for calibration workflows, the multi-step orchestration domain
- **Distributed CI** documents ePIC software validation running on PanDA-accessed distributed resources
- **Distributed Analysis** describes the support for distributed and managed analysis workflows
- **Operations** describes how the WFMS is operated
- **Organization** describes the organization of WFMS efforts and how the work is coordinated
- **Timeline** describes the development and use of the system as Collaboration needs evolve over the coming decade, culminating in physics datataking in the mid-2030s
- **References** collects reference documents, glossary terms, external links, API references, MCP references, and requirements material
- **Diagram Gallery** collects all the system diagrams

Suggested entry points by reader: physicists requesting or consuming production data — Concepts, Production System,
Physics Configuration System, and Distributed Analysis; production and validation operators — Operations and the
runbook links in References; DAQ
and streaming collaborators — Foundations and Streaming Workflows; contributors and facility participants —
Architecture, WFMS Platform, and Organization.

This documentation is the system description; per-component design and operational detail lives with the
implementations, linked from [References](reference.md). The documentation is maintained in the
[eic/epic-wfms-docs](https://github.com/eic/epic-wfms-docs) repository.
