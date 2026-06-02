from typing import Any
from typing_extensions import Iterator, AsyncIterator


def consume_sync_iterator(iterator: Iterator[Any]) -> None:
    """Exhaust a synchronous iterator, discarding all values."""
    for _ in iterator:
        ...


async def consume_async_iterator(iterator: AsyncIterator[Any]) -> None:
    """Exhaust an asynchronous iterator, discarding all values."""
    async for _ in iterator:
        ...
