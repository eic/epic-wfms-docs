# Executive Summary

The ePIC Workflow Management System (WFMS) is the shared workflow and dataflow orchestration, monitoring,
automation, and operations layer for ePIC computing, from streaming datataking to global production. Its scope is
set by the ePIC WFMS requirements and the ePIC streaming computing model: support for all major processing use cases
(post-DAQ streaming processing, production campaigns, validation, calibration, distributed CI, and analysis
workflows) operating across the Echelon resource hierarchy, from the E0 DAQ egress buffer and the E0-E1 interface, through the BNL and JLab
host labs (E1, in the two-site symmetry of the butterfly model) to global facilities (E2) and user environments
(E3). The central design decision is
one platform serving all workflow domains: shared services, monitoring, AI capability, and operational discipline,
rather than a separate system per domain.

The full WFMS foreseen for physics operations is not presently realized, nor should it be a decade before datataking.
The system is built for current needs on a trajectory aligned with the end goal, and ePIC decision points along the
way determine the trajectory. This document describes the end goal, the operating implementations, and the timeline
connecting them.

## What Operates Today

Two implementation fronts operate on the common platform.

**epicprod**, the automated production system, runs ePIC simulation and reconstruction campaigns on the monthly
campaign rhythm, and the campaigns are moving to it now (July 2026). It carries a production request from physicist submission
through physics configuration, campaign preparation, PanDA execution, cataloged data products, and (soon) validation, with AI throughout the process synthesising, evaluating, and formulating active decisions for human approval (human always in the loop). The request
interface and the Physics Configuration System (PCS) are the principal places where physicists meet the system: the
request interface carries a group's production needs into the system and tracks them, and PCS is the configuration
layer, a catalog of physics and processing definitions from which tasks are composed, with a composed name carrying
the physics identity through catalog, PanDA task, and Rucio data products. Past production has been assimilated, making
the catalog the complete ePIC production record. AI assistance appears throughout as durable, attributed artifacts
(assessments, daily campaign reports, comment discussion) and deterministic actions composed by AI and offered for human approval.

The **streaming workflow testbed** prototypes the datataking workflows of the streaming computing model: the E0-E1
interface, time frame and super time frame processing, and processing at the two E1 facilities, exercised on real
services (PanDA, Rucio, ActiveMQ, the platform monitor) with simulated datataking. Two workflows are presently realized: prompt
processing of super time frames as they arrive, and fast processing delivering high-statistics results in O(10 s) from a
standing pool of PanDA-managed workers. The reconstruction payload integration runs EICrecon as a persistent
message-driven process, a capability contributed upstream and available in the ePIC container stack.

The platform beneath both implementation fronts provides the common monitor, web, database, and messaging services; REST APIs and
MCP tools exposing state and information to people, programs, and AI clients; an alarm system, the first fielded in the
PanDA ecosystem; credentialed operations agents that keep privileged actions out of the web tier; and the corun-ai
service executing LLM work and holding its products as durable artifacts with model and prompt provenance.

The adjacent workflow domains are at earlier stages by design. Fast monitoring is the first domain extending testbed operation to remote Tier 2s. Distributed CI is running its first real jobs: ePIC
benchmark workflows execute through Snakemake executors, and eicweb CI jobs submit work to BNL through PanDA.
Calibration builds on the same Snakemake integration, with a published PanDA executor plugin. The validation loop
with Hydra, the ePIC validation application, is at the proposal stage, with the AI assessment application (corun-ai)
operating. Analysis support is a foreseen domain; the platform serves it today through data access, provenance, and
programmatic interfaces.

## Approach

The WFMS builds on established, externally maintained systems rather than developing its own: PanDA, JEDI, iDDS, and
Harvester from the BNL-led PanDA project, with development in direct coordination with the PanDA core team; Rucio for
distributed data management; XRootD for data access; Snakemake for dependency-managed workflows. ePIC operational
experience returns upstream as contributed features.

ePIC operates production with a small team, so operational quality has to come from the system. The operating
principle is maximal automation with explicit human control: automation carries routine mechanics, alarms and reports
concentrate attention, no failure is silent, and production experts make the decisions. AI is integrated under the
same discipline. AI services consume structured system state and produce assessments, reports, and diagnostics as
recorded artifacts open to comment; operational authority remains with humans and deterministic services. AI is also
a development instrument: the system is developed in AI pair-programming against its repository documentation, which
keeps development knowledge in documents and code rather than in any single person.

## Deployment

The system is developed and deployed on the EIC PanDA infrastructure at BNL, supported by the BNL SCDF facility. SCDF servers provide the development and deployment hub, carrying the platform services, databases, the credentialed production
operations agent, and the scripted development-to-deployment cycle. An external proxy host, epic-devcloud.org, opens
the production face to the whole collaboration without BNL credentials and is also the home of the corun-ai LLM research harness service.
The AI pair-programming workflow validates development/developer succession every
working day: a new AI session reaches working competence from the repositories and documentation alone, so
development knowledge manifestly transfers by construction. The human developer doesn't make a sound in the daily bootstrapping, it is automatic. The deployment side of succession is covered by operational
inventories of the two hosts
([EPICPROD_SUCCESSION.md](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_SUCCESSION.md) and
[DEVCLOUD_SUCCESSION.md](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/DEVCLOUD_SUCCESSION.md))
recording the services, schedules, credentials, and operator-bound operations a successor needs, with a further step
planned: a containerized recreation path for the external host, reducing its re-establishment to a scripted rebuild
and one configuration change.

## Timeline

Near term, the production campaigns and their automation buildout carry the operational load while the testbed
advances toward realism: DAQ integration as the E0-E1 interface, streaming formats and exit-buffer interface firm up; scaled streaming
exercises; and test beam support. Calibration and distributed CI come into routine use in the same window. Throughout
detector construction the WFMS is a principal system in the collaboration's escalating
streaming, data, and analysis challenges, and the collaboration's decision points on the streaming WFMS trajectory
are taken on that evidence. Commissioning and early datataking adopt conservative approaches while the streaming
model is progressively deployed, reaching steady-state operation in the mid-2030s: the full streaming model,
around-the-clock datataking, and the AI-instrumented maximal-automation operations model carrying it.
