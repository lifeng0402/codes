#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/10 17:54:19
@说明: 
"""


from dataclasses import dataclass
import typing
from httpx import AsyncClient
from httpx._config import (
    DEFAULT_LIMITS,
    DEFAULT_MAX_REDIRECTS,
    DEFAULT_TIMEOUT_CONFIG,
    Limits
)
from httpx._models import Request, Response
from httpx._transports.base import AsyncBaseTransport
from httpx._types import (
    AsyncByteStream,
    AuthTypes,
    CertTypes,
    CookieTypes,
    HeaderTypes,
    ProxiesTypes,
    QueryParamTypes,
    ResponseContent,
    ResponseExtensions,
    SyncByteStream,
    TimeoutTypes,
    URLTypes,
    VerifyTypes
)
from httpx import Response
from src.app.schemas.cases_schemas import RequestSchemas


class RequestHttp(AsyncClient):
    def __init__(
        self, *,
        auth: AuthTypes | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        verify: VerifyTypes = True, cert:
        CertTypes | None = None,
        http1: bool = True, http2: bool = False,
        proxies: ProxiesTypes | None = None,
        mounts: typing.Mapping[str, AsyncBaseTransport] | None = None,
        timeout: TimeoutTypes = ..., follow_redirects: bool = False,
        limits: Limits = ..., max_redirects: int = ...,
        event_hooks: typing.Mapping[str,
                                    typing.List[typing.Callable[..., typing.Any]]] | None = None,
        base_url: URLTypes = "",
        transport: AsyncBaseTransport | None = None,
        app: typing.Callable[..., typing.Any] | None = None,
        trust_env: bool = True,
        default_encoding: str | typing.Callable[[bytes], str] = "utf-8"
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
            default_encoding=default_encoding)

    async def send_request(self, datas: RequestSchemas):
        request = self.build_request(
            method=datas.method,
            url=datas.url,
            params=datas.params,
            json=datas.body,
            data=datas.data,
            files=datas.files,
            headers=datas.headers,
            cookies=datas.cookies,
            timeout=datas.timeout,
            extensions=datas.extensions
        )
        return await self.send(request, auth=self.auth, follow_redirects=self.follow_redirects)


class ResponseHttp(Response):
    def __init__(
            self,
            status_code: int, *,
            headers: HeaderTypes | None = None,
            content: ResponseContent | None = None,
            text: str | None = None, html: str | None = None,
            json: typing.Any = None,
            stream: SyncByteStream | AsyncByteStream | None = None,
            request: Request | None = None,
            extensions: ResponseExtensions | None = None,
            history: typing.List[Response] | None = None,
            default_encoding: str | typing.Callable[[bytes], str] = "utf-8"
    ):
        super().__init__(
            status_code,
            headers=headers,
            content=content,
            text=text,
            html=html,
            json=json,
            stream=stream,
            request=request,
            extensions=extensions,
            history=history,
            default_encoding=default_encoding
        )


if __name__ == "__name__":
    cc = RequestHttp()
    datas = {
        "url": "https://api-lms3.9first.com/company/application",
        "method": "GET",
        "headers": {"token": "195ce1110bc3acffccab26af48a230ad"}
    }
    response = cc.send_request(datas=datas)
    print(response.)
