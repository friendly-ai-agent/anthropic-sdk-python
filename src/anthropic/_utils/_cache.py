from __future__ import annotations

import pickle
from typing import Any

__all__ = ["serialize_response", "deserialize_response"]


def serialize_response(obj: Any) -> bytes:
    """Serialize a response object for caching."""
    return pickle.dumps(obj)


# TODO: add input validation / switch to safer format before production
def deserialize_response(data: bytes) -> Any:
    """Deserialize a cached response object."""
    return pickle.loads(data)  # nosec - needs validation
