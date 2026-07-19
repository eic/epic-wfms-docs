# Organization

This section describes how the WFMS effort is organized and coordinated so that contributions remain coherent and
complementary: the participating ePIC groups, coordination with DAQ and S&C, production operations, the host-lab and
E2 facilities, external projects, and the contribution process.

## Organizing Collaborative Efforts

The standing coordination body for the production side is the ePIC Production Working Group, meeting on the first and
third Tuesday of each month: the first meeting prepares the upcoming simulation campaign, addressing infrastructure
changes and incorporating new physics datasets, and the second reviews current production and works new challenges.

Development is coordinated through the shared repositories: contribution is by branch and pull request on the core
repositories, which advance together on coordinated branches, and this documentation is the common reference for what
the system is and where it is going. Plans and designs are developed as repository documents that drive AI
co-development: AI assistants relearn the system continually from the documentation and code, so development knowledge
carries no single point of failure. Because the workflow domains share one platform, effort invested in either front
strengthens both, and WFMS progress is reported into the ePIC software and computing meetings, where decision points on
the system's trajectory are taken.

## Participating Groups

The core WFMS effort is anchored at the host labs, with a small production operations team supported by
the automation the system exists to provide. Participation beyond the labs is growing: the University of Manitoba
and Osaka University have joined as participants in the testbed and production, with Manitoba particularly active in
production. These groups are the first realization of WFMS organization beyond the host labs — the seed of E2-level participation,
where institutions take defined roles in the system's development and operation.

Physics working groups and detector subsystem collaborations participate as the system's customers and as contributors:
they submit production requests, evaluate produced data, and provide production liaisons who carry campaign operations
knowledge into their groups and requirements and requests back to production.

## DAQ and S&C Coordination

The WFMS is an ePIC Software and Computing activity, and its streaming side is developed in coordination with the DAQ
effort: the E0-E1 interface — the exit buffer, the STF and TF streams, and the run controls that cross it — is a joint
design responsibility between DAQ and the WFMS. The streaming computing model and the WFMS requirements document,
both ePIC S&C products, set the shared direction, and the streaming workflow testbed informs ePIC's decision making on
the streaming WFMS over the coming years.

## E1/E2 Facility Involvement

BNL and JLab are the two E1 host-lab facilities of the butterfly model, and each anchors complementary parts of the
present system: PanDA and the WFMS services operate at BNL, while production science data is held in JLab Rucio, with
validation (Hydra) and Rucio metadata infrastructure developed at JLab. The butterfly model's symmetry is the
organizational frame for E1: raw data flows to both labs, and downstream processing roles remain assignable between
them.

E2 involvement is being built from working participation. Compute resources are integrated as PanDA queues — through
OSG-routed submission and as direct queues where that simplifies operations — and storage joins as Rucio storage
elements, as with the Canadian resource contributions associated with Manitoba's participation: a PanDA queue at
Manitoba's GREX facility is established, with further queues in progress at Simon Fraser University and on commercial
cloud. HPC resources are integrated the same way, with NERSC Perlmutter queues in production use, now including GPU
queues. The E2 model of foundations, global facilities with well defined responsibilities, grows from these first
integrations.

## External Projects and Systems

The WFMS builds on established, externally maintained systems and engages their projects rather than forking them,
consistent with the [EIC/ePIC Software Statement of Principles](https://eic.github.io/activities/principles.html).
PanDA, JEDI, iDDS, Harvester, and the pilot are products of the BNL-led PanDA project, and ePIC WFMS development
proceeds in direct coordination with the PanDA core team — the JEDI task-injection path used by epicprod was designed
with and agreed by the PanDA developers. Rucio is a community project with ePIC instances operated at the labs, and
ePIC operational experience returns upstream as contributed features and fixes. Hydra is the ePIC validation
application from JLab, integrated through the interfaces described in Validation. The OSG provides the distributed
submission fabric for much of the resource pool, and the ePIC software stack — containers, CVMFS distribution, and the
supporting CI — is the payload environment the WFMS executes.
