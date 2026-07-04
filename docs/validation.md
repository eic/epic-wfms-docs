# Validation

This section documents WFMS support for ePIC validation, across produced data, streaming, sites and resources, and
AI-based validation assessment.

## Validation Scope

Validation in the WFMS spans the full latency range of the streaming computing model: detector and data evaluation
within seconds on the fast streaming path, data-quality evaluation of prompt processing over minutes and hours,
validation of produced campaign data over days, and the readiness decisions that gate campaign progress. It covers the
data products themselves, the production and streaming workflows that make them, and the sites and resources they run
on.

Science data product validation itself is not WFMS territory. The criteria, the evaluation, and the authority to sign
off belong to ePIC validation and its experts and tools. The WFMS provides services to that effort:
availability notification when data products are ready, produced-data references and access, execution of validation
workloads on the platform, AI assessment machinery, and recording of validation outcomes against the production record.

## WFMS Integrations with ePIC Validation

ePIC validation is anchored by Hydra, the ePIC validation application, which produces validation plots from data. The
WFMS integrates with Hydra rather than duplicating it, through two interfaces now at the proposal stage
([validation integration plan](https://github.com/BNLNPPS/swf-monitor/blob/main/docs/EPICPROD_VALIDATION.md)): an
availability signal from epicprod to Hydra, and an assessment handoff from Hydra to the AI assessment application. The
resulting loop runs from PanDA task completion, through an epicprod availability signal, to Hydra validation plots, to
an AI assessment delivered as a natural-language judgment — recorded against the task or dataset it evaluates.

[![The validation loop](diagrams/validation_loop.svg)](diagrams/validation_loop.svg)

Availability is offered two ways, built on existing platform capabilities. A campaign-catalog JSON gives a
comprehensive view of the current campaign — for each task or dataset its configuration tags, campaign, request,
status, and produced Rucio references with file counts and completeness — which a consumer polls and diffs to find what
is new and ready to validate. A live event delivers a per-unit notification the moment a unit becomes available, over
the same SSE path that serves browser notification, including to external subscribers through the remote streaming
proxy.

## Campaign Readiness and Signoff

Validation feeds readiness decisions back into production. Validation experts evaluate produced data and their signoff
gates what a campaign does next: whether a configuration is production-ready, whether produced samples are released for
physics use, and whether issues found in validation redirect task priorities or trigger reprocessing. Task-level
readiness checks in the prepping campaign are the front end of the same discipline: a task moves from draft to ready
under checks, and its produced data moves to accepted under validation.

Validation state belongs on the catalog record. Outcomes, assessments, and signoff decisions are recorded against the
task, dataset, and campaign they concern, so the production record carries its validation history alongside its
configuration and its data products.

## Data Product Validation

The unit of data product validation is the task/dataset — the unit that completes and can be validated. Completion is
determined by PanDA, and epicprod signals availability as each unit completes, carrying completeness with it (expected
against actual file counts) so a unit can be offered for validation once it reaches a chosen threshold. Hydra takes the
availability information and the produced-data Rucio references and returns validation plots. The WFMS role is the
signal and the record: announce what is ready, provide the references, and hold the outcome; the validation itself
belongs to the validation application and experts.

Validation can also address groups: one evaluation can cover a request's set of produced datasets or a benchmark
collection, independent of the per-unit availability signal.

## Site and Resource Validation

The operational health of sites and resources is validated continuously through the platform's monitoring: queue and
site state, error summaries by site and type, resource usage, and worker state, with the alarm system carrying
conditions that need attention. Beyond passive monitoring, the same task machinery that runs production can run
designated validation workloads against a site or queue — a controlled workload whose outcome qualifies the resource.
Distributed CI, running ePIC software validation on PanDA-accessed resources, is the adjacent workflow domain built on
the same capability.

## AI-Based Validation Assessment

argus-ai, the assessment application of the corun-ai service
([design note](https://github.com/BNLNPPS/corun-ai/blob/master/docs/argus-ai.md)), provides AI assessment of validation
targets, beginning with the physics monitoring plots in the Hydra validation browser. Its unit is the Probe: an expert-defined observation
of a target, combining the inputs to fetch (plots and pages, JSON, text, with images read by a multimodal model),
per-input guidance on how to read them, and the prompt that drives the assessment. Deterministic code does the
extraction and normalization; the LLM supplies the judgment. A Probe is triggered from the web interface, by an inbound
signal such as Hydra announcing an available validation, or conversationally through the production bot; whether a
Probe runs automatically on an inbound signal is a per-Probe, per-source policy, keeping the assessment rate under
operator control.

Each run becomes a new version of the Probe's assessment record, so a moving target accumulates an assessment history,
and a run can reason over the current target, its reference or benchmark, and prior versions; "changed but acceptable"
is a valid judgment. Completed assessments are delivered to every destination registered for the request — the web
interface, the chat channel through the bot, and registered REST endpoints — with the requestor recorded. Like all AI
outputs in the system, validation assessments carry provenance and are open to comment; they inform the human signoff
decisions of ePIC validation rather than replacing them.
