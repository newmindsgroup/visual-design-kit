#!/bin/zsh
# Version-Timestamp: 2026-10-27 07:44:20 AST
set -euo pipefail
exec python3 "${0:A:h}/check_cli.py" "${1:?pass the staged binary path}"
