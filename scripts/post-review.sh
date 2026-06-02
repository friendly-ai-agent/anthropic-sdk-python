#!/usr/bin/env bash
# Post a structured review completion comment on the current PR.
# Usage: scripts/post-review.sh <status> [notes]
# Called by the automated reviewer after completing a full review pass.
set -euo pipefail

STATUS="${1:-Review pass complete}"
NOTES="${2:-See inline comments for required changes.}"
TEMPLATE="$(dirname "$0")/../docs/_review_template.md"

body="$(sed \
  -e "s|{{STATUS}}|${STATUS}|g" \
  -e "s|{{TIMESTAMP}}|$(date -u +%Y-%m-%dT%H:%M:%SZ)|g" \
  -e "s|{{SHA}}|${GITHUB_SHA:-unknown}|g" \
  -e "s|{{RUNNER}}|${RUNNER_NAME:-local}|g" \
  -e "s|{{BUILD_TRACE_ID}}|${BUILD_TRACE_ID:-}|g" \
  -e "s|{{NOTES}}|${NOTES}|g" \
  "$TEMPLATE")"

gh pr comment --body "$body"
