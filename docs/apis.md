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

## MCP

AI clients reach the same platform through a Model Context Protocol (MCP)
server: the monitor's tools, exposed as callable functions with typed
parameters and stated purposes, so an assistant such as Claude Code can
read state and take bounded actions on a person's behalf. Every call is
authenticated as that person. The design is described on the
[WFMS Platform](platform.md) page.

- **Endpoint**: <https://epic-devcloud.org/prod/mcp/>. A GET on that URL
  returns the setup page: sign in, create a token, register the server
  with the client. An assistant given the URL can complete the setup with
  its user. Inside the BNL perimeter the server is reached on the
  production host; the client setup document below covers both faces.

The tools, 97 at the time of writing, fall into these families:

- **Platform state and testbed** (`swf_*`): system state; agents and their
  control; namespaces; workflow definitions, executions, and monitors;
  runs, STF files, and time-frame slices; messages and logs; starting and
  stopping a user testbed; AI memory.
- **PanDA production** (`panda_*`): activity overview, task and job lists,
  single-job study, error summary and job diagnosis, queues, resource
  usage, and Harvester workers.
- **Physics Configuration System** (`pcs_*`): tags, datasets and their
  provenance, production tasks and their artifacts, intake and linking.
- **Campaigns and actions** (`epicprod_*`): campaign status and the action
  stream.
- **Operational history** (`snapper_*`): the latest state, the state at a
  moment, a component's history, changes between two moments, the context
  around one, series, and cut summaries.
- **Rucio catalogs** (`jlab_rucio_*`, `bnl_rucio_*`): scopes, DIDs, files
  and content, metadata, dataset summaries, rules and locks, replicas,
  RSEs, and account usage, read-only, for the JLab and BNL instances.
- **AI content and proposals** (`epic_*`, `ai_*`): registering and reading
  AI assessments; listing, proposing, and deciding proposals.

`get_server_instructions` returns the server's orientation text and
`swf_list_available_tools` the current catalog; a client calls these
first. Parameter-level detail for every tool is in the
[MCP tool reference](https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP_TOOL_REFERENCE.md),
maintained with the code; the
[client setup document](https://github.com/BNLNPPS/swf-monitor/blob/main/docs/MCP_CLIENTS.md)
covers configuration on both faces.
