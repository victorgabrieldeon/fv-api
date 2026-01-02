# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import FvError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import me, auth, card, pack, user, match, lineup, profit, redeem, userinventory
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.card import CardResource, AsyncCardResource
    from .resources.pack import PackResource, AsyncPackResource
    from .resources.match import MatchResource, AsyncMatchResource
    from .resources.me.me import MeResource, AsyncMeResource
    from .resources.profit import ProfitResource, AsyncProfitResource
    from .resources.redeem import RedeemResource, AsyncRedeemResource
    from .resources.user.user import UserResource, AsyncUserResource
    from .resources.lineup.lineup import LineupResource, AsyncLineupResource
    from .resources.userinventory import UserinventoryResource, AsyncUserinventoryResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Fv", "AsyncFv", "Client", "AsyncClient"]


class Fv(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Fv client instance.

        This automatically infers the `api_key` argument from the `FV_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("FV_API_KEY")
        if api_key is None:
            raise FvError(
                "The api_key client option must be set either by passing api_key to the client or by setting the FV_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("FV_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def profit(self) -> ProfitResource:
        from .resources.profit import ProfitResource

        return ProfitResource(self)

    @cached_property
    def pack(self) -> PackResource:
        from .resources.pack import PackResource

        return PackResource(self)

    @cached_property
    def me(self) -> MeResource:
        from .resources.me import MeResource

        return MeResource(self)

    @cached_property
    def redeem(self) -> RedeemResource:
        from .resources.redeem import RedeemResource

        return RedeemResource(self)

    @cached_property
    def lineup(self) -> LineupResource:
        from .resources.lineup import LineupResource

        return LineupResource(self)

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def card(self) -> CardResource:
        from .resources.card import CardResource

        return CardResource(self)

    @cached_property
    def match(self) -> MatchResource:
        from .resources.match import MatchResource

        return MatchResource(self)

    @cached_property
    def userinventory(self) -> UserinventoryResource:
        from .resources.userinventory import UserinventoryResource

        return UserinventoryResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def with_raw_response(self) -> FvWithRawResponse:
        return FvWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FvWithStreamedResponse:
        return FvWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncFv(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncFv client instance.

        This automatically infers the `api_key` argument from the `FV_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("FV_API_KEY")
        if api_key is None:
            raise FvError(
                "The api_key client option must be set either by passing api_key to the client or by setting the FV_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("FV_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def profit(self) -> AsyncProfitResource:
        from .resources.profit import AsyncProfitResource

        return AsyncProfitResource(self)

    @cached_property
    def pack(self) -> AsyncPackResource:
        from .resources.pack import AsyncPackResource

        return AsyncPackResource(self)

    @cached_property
    def me(self) -> AsyncMeResource:
        from .resources.me import AsyncMeResource

        return AsyncMeResource(self)

    @cached_property
    def redeem(self) -> AsyncRedeemResource:
        from .resources.redeem import AsyncRedeemResource

        return AsyncRedeemResource(self)

    @cached_property
    def lineup(self) -> AsyncLineupResource:
        from .resources.lineup import AsyncLineupResource

        return AsyncLineupResource(self)

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def card(self) -> AsyncCardResource:
        from .resources.card import AsyncCardResource

        return AsyncCardResource(self)

    @cached_property
    def match(self) -> AsyncMatchResource:
        from .resources.match import AsyncMatchResource

        return AsyncMatchResource(self)

    @cached_property
    def userinventory(self) -> AsyncUserinventoryResource:
        from .resources.userinventory import AsyncUserinventoryResource

        return AsyncUserinventoryResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncFvWithRawResponse:
        return AsyncFvWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFvWithStreamedResponse:
        return AsyncFvWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class FvWithRawResponse:
    _client: Fv

    def __init__(self, client: Fv) -> None:
        self._client = client

    @cached_property
    def profit(self) -> profit.ProfitResourceWithRawResponse:
        from .resources.profit import ProfitResourceWithRawResponse

        return ProfitResourceWithRawResponse(self._client.profit)

    @cached_property
    def pack(self) -> pack.PackResourceWithRawResponse:
        from .resources.pack import PackResourceWithRawResponse

        return PackResourceWithRawResponse(self._client.pack)

    @cached_property
    def me(self) -> me.MeResourceWithRawResponse:
        from .resources.me import MeResourceWithRawResponse

        return MeResourceWithRawResponse(self._client.me)

    @cached_property
    def redeem(self) -> redeem.RedeemResourceWithRawResponse:
        from .resources.redeem import RedeemResourceWithRawResponse

        return RedeemResourceWithRawResponse(self._client.redeem)

    @cached_property
    def lineup(self) -> lineup.LineupResourceWithRawResponse:
        from .resources.lineup import LineupResourceWithRawResponse

        return LineupResourceWithRawResponse(self._client.lineup)

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def card(self) -> card.CardResourceWithRawResponse:
        from .resources.card import CardResourceWithRawResponse

        return CardResourceWithRawResponse(self._client.card)

    @cached_property
    def match(self) -> match.MatchResourceWithRawResponse:
        from .resources.match import MatchResourceWithRawResponse

        return MatchResourceWithRawResponse(self._client.match)

    @cached_property
    def userinventory(self) -> userinventory.UserinventoryResourceWithRawResponse:
        from .resources.userinventory import UserinventoryResourceWithRawResponse

        return UserinventoryResourceWithRawResponse(self._client.userinventory)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)


class AsyncFvWithRawResponse:
    _client: AsyncFv

    def __init__(self, client: AsyncFv) -> None:
        self._client = client

    @cached_property
    def profit(self) -> profit.AsyncProfitResourceWithRawResponse:
        from .resources.profit import AsyncProfitResourceWithRawResponse

        return AsyncProfitResourceWithRawResponse(self._client.profit)

    @cached_property
    def pack(self) -> pack.AsyncPackResourceWithRawResponse:
        from .resources.pack import AsyncPackResourceWithRawResponse

        return AsyncPackResourceWithRawResponse(self._client.pack)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithRawResponse:
        from .resources.me import AsyncMeResourceWithRawResponse

        return AsyncMeResourceWithRawResponse(self._client.me)

    @cached_property
    def redeem(self) -> redeem.AsyncRedeemResourceWithRawResponse:
        from .resources.redeem import AsyncRedeemResourceWithRawResponse

        return AsyncRedeemResourceWithRawResponse(self._client.redeem)

    @cached_property
    def lineup(self) -> lineup.AsyncLineupResourceWithRawResponse:
        from .resources.lineup import AsyncLineupResourceWithRawResponse

        return AsyncLineupResourceWithRawResponse(self._client.lineup)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def card(self) -> card.AsyncCardResourceWithRawResponse:
        from .resources.card import AsyncCardResourceWithRawResponse

        return AsyncCardResourceWithRawResponse(self._client.card)

    @cached_property
    def match(self) -> match.AsyncMatchResourceWithRawResponse:
        from .resources.match import AsyncMatchResourceWithRawResponse

        return AsyncMatchResourceWithRawResponse(self._client.match)

    @cached_property
    def userinventory(self) -> userinventory.AsyncUserinventoryResourceWithRawResponse:
        from .resources.userinventory import AsyncUserinventoryResourceWithRawResponse

        return AsyncUserinventoryResourceWithRawResponse(self._client.userinventory)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)


class FvWithStreamedResponse:
    _client: Fv

    def __init__(self, client: Fv) -> None:
        self._client = client

    @cached_property
    def profit(self) -> profit.ProfitResourceWithStreamingResponse:
        from .resources.profit import ProfitResourceWithStreamingResponse

        return ProfitResourceWithStreamingResponse(self._client.profit)

    @cached_property
    def pack(self) -> pack.PackResourceWithStreamingResponse:
        from .resources.pack import PackResourceWithStreamingResponse

        return PackResourceWithStreamingResponse(self._client.pack)

    @cached_property
    def me(self) -> me.MeResourceWithStreamingResponse:
        from .resources.me import MeResourceWithStreamingResponse

        return MeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def redeem(self) -> redeem.RedeemResourceWithStreamingResponse:
        from .resources.redeem import RedeemResourceWithStreamingResponse

        return RedeemResourceWithStreamingResponse(self._client.redeem)

    @cached_property
    def lineup(self) -> lineup.LineupResourceWithStreamingResponse:
        from .resources.lineup import LineupResourceWithStreamingResponse

        return LineupResourceWithStreamingResponse(self._client.lineup)

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def card(self) -> card.CardResourceWithStreamingResponse:
        from .resources.card import CardResourceWithStreamingResponse

        return CardResourceWithStreamingResponse(self._client.card)

    @cached_property
    def match(self) -> match.MatchResourceWithStreamingResponse:
        from .resources.match import MatchResourceWithStreamingResponse

        return MatchResourceWithStreamingResponse(self._client.match)

    @cached_property
    def userinventory(self) -> userinventory.UserinventoryResourceWithStreamingResponse:
        from .resources.userinventory import UserinventoryResourceWithStreamingResponse

        return UserinventoryResourceWithStreamingResponse(self._client.userinventory)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)


class AsyncFvWithStreamedResponse:
    _client: AsyncFv

    def __init__(self, client: AsyncFv) -> None:
        self._client = client

    @cached_property
    def profit(self) -> profit.AsyncProfitResourceWithStreamingResponse:
        from .resources.profit import AsyncProfitResourceWithStreamingResponse

        return AsyncProfitResourceWithStreamingResponse(self._client.profit)

    @cached_property
    def pack(self) -> pack.AsyncPackResourceWithStreamingResponse:
        from .resources.pack import AsyncPackResourceWithStreamingResponse

        return AsyncPackResourceWithStreamingResponse(self._client.pack)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithStreamingResponse:
        from .resources.me import AsyncMeResourceWithStreamingResponse

        return AsyncMeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def redeem(self) -> redeem.AsyncRedeemResourceWithStreamingResponse:
        from .resources.redeem import AsyncRedeemResourceWithStreamingResponse

        return AsyncRedeemResourceWithStreamingResponse(self._client.redeem)

    @cached_property
    def lineup(self) -> lineup.AsyncLineupResourceWithStreamingResponse:
        from .resources.lineup import AsyncLineupResourceWithStreamingResponse

        return AsyncLineupResourceWithStreamingResponse(self._client.lineup)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def card(self) -> card.AsyncCardResourceWithStreamingResponse:
        from .resources.card import AsyncCardResourceWithStreamingResponse

        return AsyncCardResourceWithStreamingResponse(self._client.card)

    @cached_property
    def match(self) -> match.AsyncMatchResourceWithStreamingResponse:
        from .resources.match import AsyncMatchResourceWithStreamingResponse

        return AsyncMatchResourceWithStreamingResponse(self._client.match)

    @cached_property
    def userinventory(self) -> userinventory.AsyncUserinventoryResourceWithStreamingResponse:
        from .resources.userinventory import AsyncUserinventoryResourceWithStreamingResponse

        return AsyncUserinventoryResourceWithStreamingResponse(self._client.userinventory)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)


Client = Fv

AsyncClient = AsyncFv
