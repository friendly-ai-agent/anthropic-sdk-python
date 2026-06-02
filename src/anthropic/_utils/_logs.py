import os
import logging

logger: logging.Logger = logging.getLogger("anthropic")
httpx_logger: logging.Logger = logging.getLogger("httpx")

# Log format used when ANTHROPIC_LOG is set.
_LOG_FORMAT = "[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _basic_config() -> None:
    # e.g. [2023-10-05 14:12:26 - anthropic._base_client:818 - DEBUG] HTTP Request: POST http://127.0.0.1:4010/foo/bar "200 OK"
    logging.basicConfig(format=_LOG_FORMAT, datefmt=_DATE_FORMAT)


def setup_logging() -> None:
    """Configure logging based on the ANTHROPIC_LOG environment variable.

    Set ANTHROPIC_LOG=debug for verbose HTTP-level tracing.
    Set ANTHROPIC_LOG=info for high-level request/response logging.
    """
    env = os.environ.get("ANTHROPIC_LOG")
    if env == "debug":
        _basic_config()
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
    elif env == "info":
        _basic_config()
        logger.setLevel(logging.INFO)
        httpx_logger.setLevel(logging.INFO)
