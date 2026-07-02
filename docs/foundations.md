# Foundations

Defines the WFMS scope, requirements basis, streaming computing model alignment, computing use cases, Echelon model, and butterfly model. This section explains what the system must accomplish and why it is structured this way.

## WFMS Scope

The ePIC WFMS manages distributed workflows across heterogeneous computing resources used by the ePIC experiment. The scope includes post-DAQ streaming processing and monitoring, prompt reconstruction, calibration and validation workflows, simulation and reconstruction production campaigns, analysis-oriented workflow support, distributed data management integration, monitoring, diagnostics, provenance, and operational control.

## Requirements

The WFMS is guided by the ePIC distributed workflow management system requirements and the ePIC streaming computing model.

- ePIC WFMS requirements: <https://www.overleaf.com/project/67bdf89a3d44a138da503dea>
- ePIC streaming computing model report: <https://zenodo.org/records/14675920>

The WFMS is organized around computing use cases defined by the streaming computing model and WFMS requirements:

- stored data streaming and monitoring,
- alignment and calibration,
- prompt reconstruction,
- first-pass reconstruction,
- reprocessing,
- simulation production,
- analysis workflows,
- modeling and digital-twin workflows.

The ePIC computing model is organized by Echelons:

- Echelon 0 (E0): detector and DAQ environment,
- Echelon 1 (E1): the two host-lab computing facilities at BNL and JLab,
- Echelon 2 (E2): global ePIC processing and data facilities,
- Echelon 3 (E3): home-institute and user-side computing environments.

The butterfly model is the symmetric use of the two E1 facilities. Raw data flows from E0 to both E1 sites, enabling geographically separated raw-data copies and flexible policy choices for downstream processing roles.

## Streaming Computing Model Alignment
