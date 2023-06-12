#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/10 17:54:19
@说明: 
"""


import asyncio
from typing import (
    Optional,
    Union,
    Any,
    Callable,
    Mapping,
    List
)
from httpx import AsyncClient
from httpx._config import (
    DEFAULT_LIMITS,
    DEFAULT_MAX_REDIRECTS,
    DEFAULT_TIMEOUT_CONFIG,
    Limits
)
from httpx._transports.base import AsyncBaseTransport
from httpx._transports.base import AsyncBaseTransport
from httpx._types import (
    AuthTypes,
    CertTypes,
    CookieTypes,
    HeaderTypes,
    ProxiesTypes,
    QueryParamTypes,
    TimeoutTypes,
    URLTypes,
    VerifyTypes,
    RequestContent,
    RequestData,
    RequestFiles,
)
from httpx._client import (
    UseClientDefault,
    RequestExtensions,
    USE_CLIENT_DEFAULT
)


__all__ = [
    "RequestHttp"
]


class RequestHttp(AsyncClient):
    def __init__(
        self,
        *,
        auth: Optional[AuthTypes] = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        verify: VerifyTypes = True,
        cert: Optional[CertTypes] = None,
        http1: bool = True,
        http2: bool = False,
        proxies: Optional[ProxiesTypes] = None,
        mounts: Optional[Mapping[str, AsyncBaseTransport]] = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
        follow_redirects: bool = False,
        limits: Limits = DEFAULT_LIMITS,
        max_redirects: int = DEFAULT_MAX_REDIRECTS,
        event_hooks: Optional[
            Mapping[str, List[Callable[..., Any]]]
        ] = None,
        base_url: URLTypes = "",
        transport: Optional[AsyncBaseTransport] = None,
        app: Optional[Callable[..., Any]] = None,
        trust_env: bool = True,
        default_encoding: Union[str, Callable[[bytes], str]] = "utf-8",
    ):
        super().__init__(
            auth=auth,
            params=params,
            headers=headers,
            cookies=cookies,
            verify=verify,
            cert=cert,
            http1=http1,
            http2=http2,
            proxies=proxies,
            mounts=mounts,
            timeout=timeout,
            follow_redirects=follow_redirects,
            limits=limits,
            max_redirects=max_redirects,
            event_hooks=event_hooks,
            base_url=base_url,
            transport=transport,
            app=app,
            trust_env=trust_env,
            default_encoding=default_encoding
        )

    async def safe_request(
            self,
            method: str,
            url: URLTypes,
            *,
            content: Optional[RequestContent] = None,
            data: Optional[RequestData] = None,
            files: Optional[RequestFiles] = None,
            json: Optional[Any] = None,
            params: Optional[QueryParamTypes] = None,
            headers: Optional[HeaderTypes] = None,
            cookies: Optional[CookieTypes] = None,
            auth: Union[AuthTypes, UseClientDefault,
                        None] = USE_CLIENT_DEFAULT,
            follow_redirects: Union[bool,
                                    UseClientDefault] = USE_CLIENT_DEFAULT,
            timeout: Union[TimeoutTypes,
                           UseClientDefault] = USE_CLIENT_DEFAULT,
            extensions: Optional[RequestExtensions] = None
    ):
        response = await self.request(
            method=method,
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            auth=auth,
            follow_redirects=follow_redirects,
            extensions=extensions,
        )
        return response


async def requests():
    async with RequestHttp() as client:
        response = await client.safe_request(method="GET", url="https://www.baidu.com/")
        status_code = response.status_code
        print("Response status code:", status_code)
        return response, status_code


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(requests())
    print(response)
