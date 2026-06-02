# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import httpx

RAW_RESPONSE_HEADER = "X-Stainless-Raw-Response"
OVERRIDE_CAST_TO_HEADER = "____stainless_override_cast_to"

# Default timeout is 10 minutes; connect timeout is 5 seconds.
DEFAULT_TIMEOUT = httpx.Timeout(timeout=10 * 60, connect=5.0)

# Maximum number of automatic retries on transient errors (429, 500, 502, 503, 504).
DEFAULT_MAX_RETRIES = 2

# Connection pool limits for the underlying httpx client.
DEFAULT_CONNECTION_LIMITS = httpx.Limits(max_connections=1000, max_keepalive_connections=100)

# Retry backoff parameters: exponential backoff capped at MAX_RETRY_DELAY seconds.
INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0

HUMAN_PROMPT = "\n\nHuman:"

AI_PROMPT = "\n\nAssistant:"

MODEL_NONSTREAMING_TOKENS = {
    "claude-opus-4-20250514": 8_192,
    "claude-opus-4-0": 8_192,
    "claude-4-opus-20250514": 8_192,
    "anthropic.claude-opus-4-20250514-v1:0": 8_192,
    "claude-opus-4@20250514": 8_192,
    "claude-opus-4-1-20250805": 8192,
    "anthropic.claude-opus-4-1-20250805-v1:0": 8192,
    "claude-opus-4-1@20250805": 8192,
}
