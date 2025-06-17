# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fv import Fv, AsyncFv
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Fv) -> None:
        image = client.lineup.image.get()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Fv) -> None:
        image = client.lineup.image.get(
            accept_language="accept-language",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Fv) -> None:
        response = client.lineup.image.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Fv) -> None:
        with client.lineup.image.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_user_id(self, client: Fv) -> None:
        image = client.lineup.image.get_by_user_id(
            user_id="user_id",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_user_id_with_all_params(self, client: Fv) -> None:
        image = client.lineup.image.get_by_user_id(
            user_id="user_id",
            accept_language="accept-language",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_user_id(self, client: Fv) -> None:
        response = client.lineup.image.with_raw_response.get_by_user_id(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_user_id(self, client: Fv) -> None:
        with client.lineup.image.with_streaming_response.get_by_user_id(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_by_user_id(self, client: Fv) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.lineup.image.with_raw_response.get_by_user_id(
                user_id="",
            )


class TestAsyncImage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncFv) -> None:
        image = await async_client.lineup.image.get()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncFv) -> None:
        image = await async_client.lineup.image.get(
            accept_language="accept-language",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncFv) -> None:
        response = await async_client.lineup.image.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncFv) -> None:
        async with async_client.lineup.image.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_user_id(self, async_client: AsyncFv) -> None:
        image = await async_client.lineup.image.get_by_user_id(
            user_id="user_id",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_user_id_with_all_params(self, async_client: AsyncFv) -> None:
        image = await async_client.lineup.image.get_by_user_id(
            user_id="user_id",
            accept_language="accept-language",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_user_id(self, async_client: AsyncFv) -> None:
        response = await async_client.lineup.image.with_raw_response.get_by_user_id(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_user_id(self, async_client: AsyncFv) -> None:
        async with async_client.lineup.image.with_streaming_response.get_by_user_id(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_by_user_id(self, async_client: AsyncFv) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.lineup.image.with_raw_response.get_by_user_id(
                user_id="",
            )
