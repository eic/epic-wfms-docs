# Timeline

Describes the development and utilization of the system to meet Collaboration needs as they evolve over the next decade, culminating in physics datataking in the mid 2030s.

Current production and streaming testbed use, calibration, CI, test beams, streaming challenges, scaling exercises, commissioning, early data-taking, and mature operations.

[![The WFMS timeline](diagrams/wfms_timeline.svg)](diagrams/wfms_timeline.svg)

The out-years align with the joint planning of DAQ, computing, and AI:

[![Streaming computing planning FY25-FY31](diagrams/streaming_planning_fy.svg)](diagrams/streaming_planning_fy.svg)

## Three year activity timeline

The near term is anchored in operating systems. Monthly production campaigns run on epicprod today, and each campaign
exercises the newest automation — the campaign cadence is the delivery and validation rhythm for the production side.
The automation buildout continues through this period: request ingest and requester notification, the validation loop
with Hydra and AI assessment, deepening AI operations and reporting, and the steady conversion of operator procedures
into automated ones with human control points.

The streaming workflow testbed advances from emulated E0-E1 workflows to progressively more realistic exercises:
integration with DAQ developments as the streaming data formats and the exit-buffer interface firm up, scaled streaming
exercises, and support for test beams, which serve as small-scale real-world testbeds for the developing DAQ and
software. Calibration workflows, combining orchestration tools such as Snakemake with the platform, and distributed CI
on PanDA-accessed resources come into use in the same window. E2 participation grows from the first integrations of
institutional compute and storage toward defined facility roles.

Through this period the testbed's purpose is to inform: ePIC decision points on the streaming WFMS trajectory are
taken on the evidence of these exercises.

## The longer high-level timeline

The long-range milestones follow the phases set out in the ePIC streaming computing model report[^streaming-computing-model],
which groups them by the CD process, the detector construction phase, and commissioning and operations, with priority
always given to near-term needs so that development is continuously confronted with real-world exercise.

Through the detector construction phase, to about 2030, the WFMS is the system under test in the escalating series of
collaboration exercises: streaming challenges exercising the streaming workflows from DAQ through offline
reconstruction and the E0/E1 computing and connectivity; data challenges exercising scaling and capability as
distributed ePIC resources reach substantial scale, including the functional roles of the Echelon tiers and E2 in
particular; and analysis challenges exercising autonomous alignment and calibration and end-to-end workflows from
simulated raw data through the analysis model. Throughout, the production system continues in routine operation,
maturing the shared platform the challenges draw on.

Detector commissioning brings distinct requirements: semi-triggered datataking modes, initial calibrations, the
introduction of zero suppression, and the gradual extension of near-real-time processing from Echelon 1 to Echelon 2 —
planned from the experience of the preceding challenges. Early datataking then adopts simpler, more conservative
approaches while the streaming computing model is progressively deployed and validated against real beam data. Mature
operations is the end state the system is designed for: the full streaming model in production, around-the-clock
datataking operation, and the maximal-automation operations model carrying it with the small expert team ePIC will
have.

[^streaming-computing-model]: The ePIC Streaming Computing Model. <https://zenodo.org/records/14675920>
