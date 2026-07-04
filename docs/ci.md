# Distributed CI

This section documents WFMS support for distributed continuous integration: ePIC software validation running on
PanDA-accessed distributed resources.

## Distributed CI Workflow Domain

ePIC's continuous integration builds and validates the experiment software on every change; distributed CI extends
its reach beyond dedicated CI runners to the distributed resources the WFMS manages. CI workloads run as PanDA jobs —
the same task machinery that runs production — giving CI access to scale, to specialized resources such as GPUs, and
to the sites the software must ultimately run on. The same capability serves site and resource validation: a
controlled workload whose outcome qualifies the resource, as described in [Validation](validation.md).

## Status

The first real distributed CI jobs are running: ePIC benchmark workflows execute in CI through Snakemake executors,
and eicweb CI jobs submit work to BNL through PanDA — bridged from the GitLab runner by jacamar-ci with EIC-developed
HTCondor and PanDA executors, relieving the dedicated CI infrastructure whose overload motivated the domain. The WFMS
applies the same discipline to itself: panda-compose, a containerized PanDA instance developed for testing and
contributed upstream to the PanDA project, runs end-to-end workflow tests, including the testbed prompt-processing
workflow, in GitHub Actions. The domain is in development toward routine use in the near-term window of the
[Timeline](timeline.md).
