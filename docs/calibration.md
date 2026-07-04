# Calibration

This section documents WFMS support for ePIC calibration workflows, the platform's multi-step orchestration domain.

## Calibration Workflow Domain

Calibration closes the slowest loop of the streaming computing model: from first detector evaluation within seconds
to full calibration cycles of up to about two weeks, calibrations produced from streamed data feed back into prompt
and subsequent processing. The calibrations themselves — algorithms, constants, and their validity — belong to the
detector and reconstruction experts; the WFMS contributes the orchestration: dependency-managed multi-step workflows,
execution on platform resources, and the bookkeeping that records what ran on what.

## Realization on the Platform

Calibration is where dependency management is central, and Snakemake is the platform's layer for it, as described in
[WFMS Platform](platform.md): workflows are described as Snakemake rules, with a published Snakemake executor plugin
dispatching work through PanDA and a Rucio storage plugin in development for data handling. The integration is well
advanced — ePIC benchmark workflows run in CI through these executors — and calibration workflows on the platform
come into use in the near-term window of the [Timeline](timeline.md).
