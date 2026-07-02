# ePIC WFMS Documentation

This repository is the source for the Read the Docs documentation site for the ePIC Workflow Management System.

The site is organized around the ePIC distributed workflow management system as a shared platform for streaming, production, analysis, and other distributed workflows such as calibration and distributed CI.

## Local Preview

Use the existing `swf-testbed` virtual environment rather than creating a separate environment for this docs repository:

```bash
./serve-docs.sh
```

The preview server listens on port `8000`.

- If working through VS Code Remote SSH, forward port `8000` and open `http://localhost:8000/`.
- If the server is directly reachable, open `http://pandaserver02:8000/`.

The preview script polls the documentation sources once per second and restarts MkDocs automatically when docs or config files change. This avoids relying on filesystem change notifications, which can be unreliable on the shared filesystem.

The script expects `../swf-testbed/.venv` to exist and to have the MkDocs requirements installed. If the environment is missing the documentation dependencies, install them into that existing environment:

```bash
../swf-testbed/.venv/bin/pip install -r requirements.txt
```
