#!/bin/zsh
# Version-Timestamp: 2026-10-27 07:44:20 AST
# Usage: tools/selftest.sh /explicit/staged/binary
set -euo pipefail
exec python3 "${0:A:h}/run_checks.py" selftest "${1:?pass the staged binary path}"
