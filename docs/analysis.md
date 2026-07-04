# Distributed Analysis

This section describes WFMS support for distributed and managed analysis workflows, which supplement rather than
replace individual standalone analysis: E3 and user computing, data access, notebooks and programmatic interfaces,
reproducibility, and the growth path toward managed analysis.

## Distributed Analysis Workflow Domain

Analysis belongs to the physicist. The WFMS role is to supplement standalone analysis where scale, data locality, or
shared execution helps: analysis workloads too large for local resources, systematic production of analysis-level
derived data over campaign outputs, and common analysis passes that many groups would otherwise run separately. PanDA
brings a proven capability here — it has served large-scale distributed user analysis for ATLAS for two decades — so
the execution machinery exists; the ePIC questions are which analysis patterns benefit from managed execution and how
they are packaged, to be worked out with the analysis community as the need matures. Managed production of campaign
benchmark analyses over newly produced data is a first candidate.

Analysis is a foreseen workflow domain rather than an operating one. The requirements place it in WFMS scope, the
platform serves it today through data access and metadata services, and managed analysis workflows are the growth path.

## Echelon 3 Support and User Computing

Echelon 3 is computing where ePIC physicists are: home institutes, university clusters, and personal machines. The WFMS
serves E3 rather than managing it. From an E3 environment a physicist can discover data products through the catalog,
read them remotely or arrange their transfer, submit managed workloads to E1 and E2 resources when local capacity is
not enough, and follow those workloads through the same open read-only monitoring the collaboration uses. E3 resources
themselves stay under their owners' control.

## Data Access

Data access is the analysis service the system already provides. Produced data products are cataloged with their Rucio
references beside the physics configuration that made them, so discovery runs from physics terms to concrete datasets:
a composed task name states its configuration, and the catalog links it to its outputs, their status, and their
locations. Files are readable over XRootD, including remote streaming reads against E1 storage, and Rucio rules can
place data where analysis needs it.

## Notebooks and Services

The platform's REST APIs and MCP tools give notebooks and analysis scripts the same programmatic access that the
system's own services use: dataset discovery, configuration and provenance metadata, production status, and monitoring
state. A notebook can locate a campaign's outputs, resolve their replicas, and read them over XRootD with no
analysis-specific infrastructure. The MCP interface extends the same access to AI assistants, so analysis users can ask
provenance and status questions conversationally. Dedicated analysis services can grow on the platform as community
usage patterns emerge.

## Reproducibility

The production record gives analysis its data-side reproducibility. A composed task name states the full physics
configuration of a dataset; the catalog resolves it through configuration, task, and request to the produced outputs;
and locked configurations are stable references, so an analysis can state exactly what it consumed in terms that remain
resolvable years later. Managed analysis workflows extend the same discipline forward: a managed pass is a cataloged
task with recorded configuration, inputs, and outputs. Reproducibility of the analysis code itself remains with the
analyst and the collaboration's software practices; the WFMS contributes the provenance of everything the analysis
consumed.
