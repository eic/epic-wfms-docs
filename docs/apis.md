# APIs

The WFMS exposes its services through REST interfaces. Every interface
served by the monitoring platform is described by an OpenAPI 3 schema
generated directly from the code, so the published documentation tracks the
implementation. The schema is browsable interactively and is the single
source of endpoint detail; the design documents linked below state each
interface's purpose and semantics.

## Interactive Documentation

- [Swagger UI](https://epic-devcloud.org/prod/api/schema/swagger-ui/) —
  browse and exercise every endpoint
- [Redoc](https://epic-devcloud.org/prod/api/schema/redoc/) — the same
  schema as reference documentation
- [OpenAPI schema](https://epic-devcloud.org/prod/api/schema/) — the raw
  machine-readable schema, suitable for client generation

These pages serve on the public face at `epic-devcloud.org`; the same pages
serve inside the BNL perimeter under `/swf-monitor/api/schema/` on the
production host.

## Interfaces

- **Validation interface v1** (`/prod/pcs/api/v1/`) — the
  production–validation loop: open completion and campaign-catalog reads,
  and the authenticated results receiver. Design:
  [EPICPROD_VALIDATION.md](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/EPICPROD_VALIDATION.md).
  The base URL serves an index of the interface's endpoints and
  documentation.
- **PCS API** (`/prod/pcs/api/`) — tags, datasets, production
  configurations, and campaign tasks of the Physics Configuration System.
  Design: [PCS](pcs.md) and
  [PCS.md](https://github.com/BNLNPPS/swf-epicprod/blob/main/docs/PCS.md).
- **PanDA views API** (`/prod/api/panda/`) — read-only task, job, queue,
  and resource-usage data, the source for the external monitoring pages.

AI clients reach the same platform through its MCP services, described on
the [WFMS Platform](platform.md) page.
