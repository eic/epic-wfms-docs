# Concepts

The working vocabulary of the WFMS: the data units, configuration entities, identities, and lifecycles used
throughout this documentation and in the system's interfaces. Definitions here are the reference; the domain sections
describe how the concepts are used.

## Streaming Data Units

**Time frame (TF)** — the atomic unit of ePIC streaming data: a contiguous, self-contained slice of the detector data
stream.

**Super time frame (STF)** — an aggregate of consecutive time frames into a file-sized unit. The STF is the unit of
registration, transfer, bookkeeping, and bulk processing: it is what Rucio registers and moves, what run datasets
collect, and what prompt processing consumes.

**TF slice** — the parallel work unit of fast processing: a subsample of an STF comprising contiguous time frames.
Slice size is set by the target latency for control room plots and statistics and for AI assessments — a TF count
whose reconstruction processing time matches the target, 10-30 seconds in present thinking.

**Run** — a datataking period. The run lifecycle — run imminent, run start, pause and resume, run end — is broadcast
from the DAQ side and drives downstream orchestration. At run start a Rucio run dataset is created; arriving STFs are
registered into it.

## Production Configuration and Identity

**Tag** — a named parameter set capturing the configuration of one production stage: physics (p), event generation
(e), simulation (s), and reconstruction (r), with physics tags grouped by category. A fifth type, background (k), is
not a stage but an orthogonal overlay — a named background configuration composed into a dataset alongside the stage
tags. A tag is `draft` (editable) or `locked` (immutable, a one-way transition), so a configuration used in production
never changes meaning.

**Dataset** — the concrete production unit: one sample, produced by a single task. Its identity composes the
classification tags with any sample-variant discriminator into the composed name. A sample normally registers as a
single Rucio dataset, with planned provision for multiple datasets mapping to one task: Rucio limits a dataset to
100k files, and production tasks have exceeded that, so a large sample subdivides into Rucio block datasets (`.bN`)
under one logical identity.

**Sample variant** — a named discriminator for samples that share a physics configuration but are produced as separate
datasets, such as the angular ranges of a single-particle sample. A variant is a name plus the submission parameters
that produce that sample; each variant materializes as its own dataset and task, distinguished only by the variant
segment of the name.

**Production config** — a reusable template of execution-side settings: software stack, resource targets, splitting,
site and data-handling parameters. Production configs are deliberately mutable working templates; the PanDA task and
job records are the immutable record of what actually ran.

**Composed name** — the identity that runs through the whole system:

```
{scope}.{det_version}.{det_config}.{p_tag}.{e_tag}.{s_tag}.{r_tag}[.{k_tag}][.{sample_name}]
```

The optional segments are the background overlay tag (`k`), present when the dataset composes a background
configuration, and the sample-variant name. A whole-task rerun appends a further optional segment, `.tryN`, to the
name itself — the PanDA task name and the output dataset name — which is what keeps repeated submissions clash-free;
the catalog resolves any `.tryN` name back to the same campaign task (see logical and physical names below).

The composed name states the physics configuration and serves as the task's identity in catalog pages, links, and the
API, and as the produced Rucio dataset name and PanDA task name. The version segment is the detector version — it
describes the conditions of the produced data; campaign membership is bookkeeping and does not rename the identity.

**Logical and physical names** — the composed name is the stable logical identity. Physical names append reserved
suffixes when uniqueness requires them: `.tryN` when an entire task is deliberately rerun, and `.bN` for Rucio block
subdivision of very large datasets. Parsing strips the terminal suffixes, so every physical name resolves back to its
logical identity.

## Requests, Campaign Tasks, and Campaigns

**Production request** — the structured record of a community request, typically submitted by physics working groups
and detector subsystem collaborations. A request is deliberately more abstract than an output — it states the physics,
beam energies, and kinematic range — and one request commonly leads to several produced datasets. Requests specify the
requestor, so task status and completion notifications can reach them. Provenance is by reference: a task resolves
through its request to the originating submission.

**Campaign task** — the submit-ready binding of tags, dataset, and production config; the unit the catalog stages,
submits, and accounts for. Its lifecycle:

```
draft  →  ready  →  submitted  →  completed | partial (recoverable) | failed
```

`draft` covers every incomplete state; a task moves to `ready` under readiness checks and operator confirmation,
`submitted` on submission, and PanDA drives the outcome: completed, partial — recoverable by completing the tail —
or failed.

**PanDA task association** — the record of one physical PanDA submission of a campaign task, preserving the complete
submission history on the task record. Retry is native to PanDA: failed or missing jobs are retried within the existing PanDA
task, under the same name, and the efficient course is always to complete the tail of the existing task. Only the
special case of deliberately rerunning an entire task — essentially cloning it — creates a new submission under a
`.tryN` name, a case that serves mainly system testing on small test tasks.

**Campaign** — a time-ordered grouping of production tasks, named by year and month (25.10, 26.06). Campaigns stage the
catalog:

```
prepping (mutable)  →  current (live)  →  past (frozen archive)
```

Prepping campaigns accept new tasks and clones; the current campaign is where submission and live status happen; past
campaigns preserve all task parameters as the production record.

**Campaign narrative** — a human-authored account of a campaign's goals, priorities, and evolution. It is shared
context for operators and LLMs: daily reports and assessments reason against it.

The lifecycles above in one view:

[![Lifecycles](diagrams/lifecycles.svg)](diagrams/lifecycles.svg)

## Execution

**PanDA task** — the executable unit in PanDA, identified by its JEDI task ID; PanDA breaks it into **jobs** brokered
to **queues** at computing sites, executed by workers that Harvester provisions. The PanDA vocabulary is documented in
full in the [PanDA basic concepts](https://panda-wms.readthedocs.io/en/latest/terminology/terminology.html).

## Platform Operational Entities

**Agent** — a message-driven service process built on the shared agent base, registered and heartbeating in the
monitor. Agents implement testbed workflow roles and the credentialed production operations executor.

**Namespace** — the isolation boundary that lets concurrent users and services run workflows side by side; agents
filter messages by namespace.

**Workflow execution** — one tracked instance of a running workflow, recording its runs, files, messages, and state in
the monitor database.
