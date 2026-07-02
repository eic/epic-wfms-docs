#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

mkdocs_bin="../swf-testbed/.venv/bin/mkdocs"
server_pid=""

signature() {
  {
    find docs -type f -print
    printf '%s\n' mkdocs.yml README.md requirements.txt .readthedocs.yaml
  } | sort | xargs sha1sum 2>/dev/null | sha1sum
}

start_server() {
  "$mkdocs_bin" serve -a 0.0.0.0:8000 &
  server_pid="$!"
}

stop_server() {
  if [[ -n "${server_pid}" ]]; then
    kill "${server_pid}" 2>/dev/null || true
    wait "${server_pid}" 2>/dev/null || true
    server_pid=""
  fi
}

trap stop_server EXIT INT TERM

last_signature="$(signature)"
start_server

while true; do
  sleep 1
  current_signature="$(signature)"
  if [[ "${current_signature}" != "${last_signature}" ]]; then
    echo "Documentation source changed; restarting MkDocs preview..."
    stop_server
    sleep 0.5
    last_signature="${current_signature}"
    start_server
  fi
done
