# Foundations

This section defines the WFMS scope, requirements basis, streaming computing model alignment, computing use cases, Echelon model,
and butterfly model. It explains what the system must accomplish and why it is structured this way.

The WFMS foreseen by ePIC for physics operations is not presently realized, nor should it be a decade prior to datataking. ePIC is building towards it, focused on current needs, with an operating streaming workflow testbed evaluating an agentic and PanDA/Rucio based infrastructure for E0-E1-E2 datataking workflows, and an operating production system integrating PanDA, Rucio and AI systems through an agentic infrastructure. The trajectory of these developments is aligned with the end goal, if all goes well. ePIC decision points in the future will determine the trajectory. This document describes the end goal, the present technical implementations, and the planned timeline (at a high level, appropriate to this stage of the project).

## WFMS Scope

The ePIC Workflow Management System (WFMS) is the shared workflow, data management, monitoring, automation, and
operations layer for ePIC computing, from datataking to global production.
It encompasses streaming and production — including workflows that combine aspects of both —
in a common WFMS platform for the experiment, spanning post-DAQ E0-E1 streaming processing, global production campaigns,
validation workflows, distributed analysis support, calibration, distributed CI, and future datataking operations.

The present system has two active implementation fronts, building from a common platform for a coherent and efficient overall WFMS capability:

- the **streaming workflow testbed**, prototyping E0-to-E1 streaming workflow and dataflow orchestration for the documented ePIC streaming computing model[^streaming-computing-model]
- **epicprod**, the automated production system. It gathers and integrates production requests from the community,
  establishes the physics configurations that define request production tasks, and documents and manages present, past
  and future production campaigns. It configures execution-ready tasks and executes them on a distributed computing
  infrastructure using PanDA and Rucio, with robust and comprehensive monitoring from drill-down expert diagnostics to
  user-friendly overviews. Maximal automation and AI integration throughout the system enable high quality production
  operations with minimal human operations effort.

## Requirements

The WFMS is guided by the ePIC distributed workflow management system requirements[^wfms-requirements] and the ePIC streaming computing
model.[^streaming-computing-model]

The requirements establish the main design obligations:

- support all major ePIC processing use cases, from streaming post-DAQ processing through production, reprocessing,
validation, calibration, and analysis
- operate across heterogeneous distributed resources, including E1 host-lab facilities, E2 facilities around the globe, E3 user
environments, and opportunistic or specialized resources
- integrate workflow management with distributed data management, so data availability and data placement can drive
processing
- provide web, REST, programmatic, and operational interfaces suitable for users, operators, facilities, and automated
services
- maintain provenance, bookkeeping, metadata, monitoring, diagnostics, and logs as integral parts of the system
- support high-quality operations with maximal automation and minimal routine human effort
- allow fast-turnaround development and deployment without losing operational control

The WFMS computing use cases include stored data streaming and monitoring, alignment and calibration, prompt
reconstruction, first-pass reconstruction, reprocessing, simulation production, validation, analysis workflows, and
modeling or digital-twin workflows.

The ePIC computing model is organized by Echelons:

- **E0**: detector and DAQ environment at the experiment site and extending to a 'DAQ enclave' in the BNL computing center
- **E1**: the two host-lab computing facilities at BNL and JLab
- **E2**: global ePIC processing and data facilities with well defined responsibilities in ePIC computing
- **E3**: home-institute and user-side computing environments: computing where ePIC physicists are

The host-lab symmetry of the
'butterfly model' is central to the E1 design. E0 is necessarily bound to BNL where the EIC is located, but post-DAQ,
the butterfly model expresses symmetry in computing capability between the two host labs.
Raw data flows from E0 to both E1 sites, establishing geographically
separated raw-data copies and preserving flexibility in how ePIC assigns downstream processing roles between BNL and
JLab, and other facilities.

[![The ePIC computing model](diagrams/epic_computing_model.svg)](diagrams/epic_computing_model.svg)

## Streaming Computing Model Alignment

The ePIC streaming computing model drives the WFMS architecture from the start. ePIC data processing begins with a
continuous post-DAQ data stream during datataking, delivering first results from E1 processing in O(10sec) to inform
control room operations and AI tools of current detector and machine performance, and delivering more complete and digested
prompt processing from bulk E1 (and possibly E2) resources over minutes and hours. The system must be capable of
delivering evaluation, validation and calibration results at the latencies ePIC demands, from seconds for detector
and data evaluation/validation to ~2 weeks for full calibration cycles.
The WFMS therefore has to support
data-driven operation, near-real-time monitoring, prompt processing, calibration feedback, and distributed execution
as baseline system capabilities.

The streaming workflow testbed exercises this model directly. It prototypes the E0 to E1 interface,
time frame based processing, fast monitoring, Rucio data handling, PanDA task execution,
a fast agentic message-based infrastructure, monitor-backed
deep operational state, and REST and MCP services that inform collaborating software, AIs and people.
These are the early implementation of WFMS behavior needed for datataking, to inform ePIC's decision making on
streaming WFMS over the next several years.

The epicprod production system exercises the same platform from a different direction. It uses PanDA, monitoring, task
cataloging, AI based assessments and diagnostics, human-in-the-loop control and curation,
and data product cataloging to run the simulation/reconstruction campaign operations that ePIC needs today,
automated to the greatest extent possible to minimize the demand on the scarce operations effort ePIC has available.
The production experience feeds the same WFMS design: operational clarity, automation, provenance, site awareness, and
reliable human control.

Further workflow domains are foreseen and are starting to be addressed: distributed CI using PanDA-accessed resources,
calibration workflows combining orchestration tools like Snakemake with the ePIC WFMS platform, and analysis workflows
that can benefit from the platform, e.g. by leveraging distributed resources and/or centrally managed execution.

The foundation is therefore one platform serving multiple workflow domains. Streaming, production, validation,
calibration, distributed CI, and analysis have distinct operational needs, but they should converge on shared
services, shared data models where practical, shared monitoring, and shared operational discipline.

[^wfms-requirements]: ePIC Distributed Workflow Management System requirements. <https://www.overleaf.com/project/67bdf89a3d44a138da503dea>

[^streaming-computing-model]: The ePIC Streaming Computing Model. <https://zenodo.org/records/14675920>
