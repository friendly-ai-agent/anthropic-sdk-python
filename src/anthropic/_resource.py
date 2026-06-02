# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time

import anyio

from ._base_client import SyncAPIClient, AsyncAPIClient


class SyncAPIResource:
    """Base class for synchronous API resource wrappers."""

    _client: SyncAPIClient

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    def _sleep(self, seconds: float) -> None:
        """Sleep for the given number of seconds (used for retry backoff)."""
        time.sleep(seconds)


class AsyncAPIResource:
    """Base class for asynchronous API resource wrappers."""

    _client: AsyncAPIClient

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    async def _sleep(self, seconds: float) -> None:
        """Async sleep for the given number of seconds (used for retry backoff)."""
        await anyio.sleep(seconds)
