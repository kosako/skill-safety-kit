#!/usr/bin/env bash
# spin.sh — fixture warm-up pass. Runs a small, bounded loop and exits.
set -euo pipefail

# ---------------------------------------------------------------------------
# DANGER EXAMPLE (DISABLED) — do NOT uncomment or run.
# The following classic fork bomb is shown only as inert text so a reviewer
# can recognize the pattern. It is never executed by this fixture.
#
#   :(){ :|:& };:
#
# End of danger example.
# ---------------------------------------------------------------------------

# Actual executed code: a finite, harmless loop that terminates immediately.
for i in 1 2 3; do :; done

echo "spin.sh: bounded warm-up complete (endpoint would be coordinator.example.com)"
exit 0
