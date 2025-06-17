# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fv import Fv, AsyncFv
from fv.types import PackListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPack:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Fv) -> None:
        pack = client.pack.list()
        assert_matches_type(PackListResponse, pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Fv) -> None:
        pack = client.pack.list(
            accept_language="accept-language",
        )
        assert_matches_type(PackListResponse, pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Fv) -> None:
        response = client.pack.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pack = response.parse()
        assert_matches_type(PackListResponse, pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Fv) -> None:
        with client.pack.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pack = response.parse()
            assert_matches_type(PackListResponse, pack, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPack:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncFv) -> None:
        pack = await async_client.pack.list()
        assert_matches_type(PackListResponse, pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFv) -> None:
        pack = await async_client.pack.list(
            accept_language="accept-language",
        )
        assert_matches_type(PackListResponse, pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFv) -> None:
        response = await async_client.pack.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pack = await response.parse()
        assert_matches_type(PackListResponse, pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFv) -> None:
        async with async_client.pack.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pack = await response.parse()
            assert_matches_type(PackListResponse, pack, path=["response"])

        assert cast(Any, response.is_closed) is True
