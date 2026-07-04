# Streaming Workflows

Documents post-DAQ workflows during datataking: E0 to E1 dataflow, STF/TF processing, fast processing for low-latency control room/AI analytics and validation, prompt processing of STF files, streaming reconstruction integration, fast monitoring, E2 integration in streaming workflows, and current/near term realizations in the streaming workflow testbed.

[![E0-E1 workflow schematic](diagrams/E0-E1_workflow_schematic.svg)](diagrams/E0-E1_workflow_schematic.svg)

## E0-E1 Interface - Controls and Dataflows

The E0-E1 interface is where WFMS responsibility begins. The DAQ system is one system spanning two facilities: the DAQ
room at IP6 and the DAQ enclave in the BNL data center, connected at 4 Tbps. Super time frame (STF) files are built in
the DAQ enclave and land in the DAQ exit buffer, sized for about 72 hours of datataking. The buffer extends beyond the
enclave onto an external subnet for E1 delivery; this outward face is the piece of Echelon 0 that the post-DAQ world
sees, and the WFMS scope runs from it rightward through E1 processing.[^streaming-computing-model]

Two dataflows leave the exit buffer. The STF stream is the complete raw data: STF files are registered in Rucio at the
exit buffer and delivered to the E1 buffers at both BNL and, over ESnet at 400 Gbps, JLab, establishing the two
geographically separated raw-data copies of the butterfly model. The E1 buffers serve the full-sample consumers:
archiving, prompt processing, and prompt monitoring. The TF stream is a fast subsample delivered at finer granularity,
with data available to E1 consumers within a few seconds of datataking; it feeds fast monitoring and fast processing.
Candidate TF delivery mechanisms are messaging and direct XRootD reads against the exit buffer.

Control signals cross the interface alongside the data. The run lifecycle — run imminent, run start, pause and resume,
run end — is broadcast from the DAQ side and drives downstream orchestration: dataset creation, processing task
establishment, worker provisioning, and run closeout all key off these transitions.

## Timeframes And Super Timeframes

The time frame (TF) is the atomic unit of ePIC streaming data: a contiguous, self-contained slice of the detector data
stream. Super time frames aggregate consecutive time frames into file-sized units that serve as the unit of
registration, transfer, bookkeeping, and bulk processing. The STF is what Rucio registers and moves, what run datasets
collect, and what prompt processing consumes.

The two units define the two latency regimes. Full STFs carry the complete data sample on the timescale of file
creation and transfer. TF-level data serves the fast paths: TF subsamples can be formed in the DAQ enclave in parallel
with STF building, or skimmed from STFs sitting in the exit buffer, and are small enough to deliver and process within
seconds. Downstream, sampled TFs are further divided into TF slices, the parallel work units distributed to fast
processing workers.

## Prompt STF Processing

Prompt processing is the full-sample processing path: every STF in the run is processed at the E1 facilities as it
arrives, delivering complete first-pass results over minutes to hours. At run start a Rucio dataset is created for the
run; arriving STFs are registered into it and transferred to the E1 buffers. A processing task is established for the
run in PanDA, and jobs process the STFs as the dataset fills. Results serve detector and physics evaluation well beyond
what the fast path's sampled data supports.

The prompt processing resource pool is E1 in the baseline and can extend to E2 facilities as capability and policy
allow; PanDA brokering over queues and Rucio-managed data placement make wider distribution a configuration choice
rather than a workflow redesign.

The workflow is diagrammed below, including the prompt processing decision box — the conceptual control point,
notified of run signals and arriving data and able to examine the data itself, that applies ePIC policy to direct
which site processes which data.

[![Prompt processing workflow](diagrams/prompt_processing_workflow.svg)](diagrams/prompt_processing_workflow.svg)

## Fast Processing Pipeline

Fast processing exists for latency: first results from the data stream in O(10 sec) to inform control room operations
and AI tools of current detector and machine performance. TF samples are skimmed from arriving STFs, divided into TF
slices, and distributed to a standing pool of workers running the reconstruction payload — EICrecon for ePIC
production, now being integrated into the testbed workers. Slice results flow to low-latency analytics and monitoring
consumers.

The latency budget rules out provisioning workers on demand. The pipeline pre-provisions a configurable worker pool at
run start: run-imminent signals carry the target worker count, iDDS and Harvester establish semi-persistent PanDA
worker jobs on the compute resources, and the workers consume slices for the duration of the run and exit at run end.
Slice-level state — queued, processing, completed, failed with bounded retry — is tracked in the monitor database.

## Streaming Reconstruction Integration

Streaming reconstruction itself is not WFMS scope: EICrecon, its configuration, and its physics performance belong to
ePIC software. The WFMS integrates reconstruction as the payload of streaming processing, and the integration is a
workflow concern in its own right, with different requirements in the two latency regimes.

Prompt processing integrates reconstruction conventionally: EICrecon processes STF files as PanDA jobs in the ePIC
container environment distributed over CVMFS — the same payload environment production uses. Prompt processing with an
EICrecon reconstruction payload has run successfully in the testbed.

Fast processing cannot pay a per-slice startup cost: the payload must run as a standing process that accepts work as
it arrives. This integration is an area of very active development, in collaboration with EICrecon developers at JLab.
The worker transformation (`swf-transform`) runs EICrecon as a persistent process and feeds it slice work over ZeroMQ
messaging; the worker lifecycle layer (`swf-panda-workers`) provisions and scales the worker pool through iDDS and
PanDA on run lifecycle signals and observed slice processing times. The payload capabilities this demands — event
windowing directed by messages, remote input over XRootD, and clean process termination — are contributed upstream to
EICrecon, and message-driven EICrecon is available in the ePIC container stack. The integration is exercised against
real campaign simulation outputs.

## Monitoring And Validation

Fast monitoring consumes sampled TF data at the E1s for near-real-time detector and data quality: fast monitoring
agents read remotely against the exit buffer or receive delivered samples, and their outputs are available within
seconds of datataking. Prompt monitoring runs against the full STF sample as it is processed. Both feed control room
displays, automated quality checks, and AI analytics, and both are candidates for E2 consumers of the monitoring
streams.

The workflows themselves are monitored through the platform's operational state: runs, files, workflow executions,
messages, agent status, and slice bookkeeping are recorded in the monitor database and presented in live browser views.
Streaming-side validation operates at the fast end of the validation latency range, evaluating detector performance and
data quality from the first samples; the broader validation program, through full calibration cycles, is described in
the Validation section.

## Streaming Workflow Testbed

The streaming workflow testbed is the current realization of these workflows. It prototypes the ePIC streaming model
from E0 egress — the DAQ exit buffer — through processing at the two E1 facilities, exercising workflow and dataflow
logic on real services (PanDA, Rucio, ActiveMQ, the monitor) with emulated facilities and simulated datataking, within
the scope marked in the schematic above. Its architecture and agent design are documented in the
[testbed architecture overview](https://github.com/BNLNPPS/swf-testbed/blob/main/docs/architecture.md).

A simulated DAQ drives the system: `swf-daqsim-agent` models detector, machine, and DAQ influences, generates the run
lifecycle and STF stream, and is the primary driver of testbed activity. `swf-data-agent` is the central data handler,
creating run datasets in Rucio, registering and attaching STF files to them, and notifying downstream consumers; a
watcher role detecting stalls and anomalies is planned. `swf-processing-agent` establishes and manages the PanDA prompt-processing
tasks. `swf-fastmon-agent` samples TF-level data from available STFs and records fast-monitoring metadata.
A fast processing agent creates TF slices from the samples, broadcasts the run and target worker count to the worker
layer to provision the standing pool, distributes slices, and collects results.

The agents are configured, launched, and supervised through a common management layer, controlled from the CLI and,
equivalently, by AI assistants through MCP:

[![Testbed agent management](diagrams/testbed_agent_management.svg)](diagrams/testbed_agent_management.svg)

Two streaming workflows are realized today. The prompt processing workflow takes simulated runs from run-imminent
through dataset creation, STF registration, and PanDA task submission over the run dataset. The fast processing
workflow takes the same runs through TF sampling, slice creation, and slice processing on the pre-provisioned worker
pool. Both are driven by TOML workflow
configurations and tracked end to end in the monitor.

Concurrent testbed users share one infrastructure and operate independently, isolated by namespace and per-user agent
identity:

[![Testbed multi-user isolation](diagrams/testbed_multi_user.svg)](diagrams/testbed_multi_user.svg)

The fast processing pipeline and its worker management are diagrammed below: the agent pipeline from simulated DAQ to
PanDA workers, and the iDDS/PanDA/Harvester detail behind the standing worker pool.

[![Fast processing pipeline](diagrams/fast-processing-pipeline-v10.svg)](diagrams/fast-processing-pipeline-v10.svg)

[![iDDS PanDA detail](diagrams/idds-panda-detail-v1.svg)](diagrams/idds-panda-detail-v1.svg)

The integration of the real EICrecon payload into these workers is described in
[Streaming Reconstruction Integration](#streaming-reconstruction-integration) above.

[^streaming-computing-model]: The ePIC Streaming Computing Model. <https://zenodo.org/records/14675920>
