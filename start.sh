#!/usr/bin/env bash
# macOS / Linux launcher
cd "$(dirname "$0")"
exec python3 serve.py "$@"
