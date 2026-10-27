#!/bin/zsh
# Version-Timestamp: 2026-10-27 07:44:20 AST
set -euo pipefail
exec python3 "${0:A:h}/tools/build_stage.py" "$@"
