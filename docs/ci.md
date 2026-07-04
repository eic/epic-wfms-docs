# Distributed CI

Documents WFMS support for distributed continuous integration: ePIC software validation running on PanDA-accessed
distributed resources.

## Distributed CI Workflow Domain

ePIC's continuous integration builds and validates the experiment software on every change; distributed CI extends
its reach beyond dedicated CI runners to the distributed resources the WFMS manages. CI workloads run as PanDA jobs —
the same task machinery that runs production — giving CI access to scale, to specialized resources such as GPUs, and
to the sites the software must ultimately run on. The same capability serves site and resource validation: a
controlled workload whose outcome qualifies the resource, as described in [Validation](validation.md).

## Status

The first real distributed CI jobs are running: ePIC benchmark workflows execute in CI through Snakemake executors,
and eicweb CI jobs submit work to BNL through PanDA. The domain is in development toward routine use in the
near-term window of the [Timeline](timeline.md).
