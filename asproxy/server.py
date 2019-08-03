import asyncio

from aiohttp.web import BaseRequest
from aiohttp.web import Response
from aiohttp.client import request as client_request


async def proxy_handler(request: BaseRequest):
    if request.method == 'CONNECT':
        return await http_tunnel(request)
    else:
        return await http_proxy(request)


async def http_proxy(request: BaseRequest):
    async with client_request(request.method, url=request.url, headers=request.headers, data=request.content) as resp:
        return Response(body=resp.content, headers=resp.headers)


async def http_tunnel(request: BaseRequest):
    transport: asyncio.Transport
    protocol: asyncio.Protocol

    loop = asyncio.get_event_loop()
    transport, protocol = await loop.create_connection(asyncio.protocols.Protocol, request.url.host, request.url.port)
    request.protocol.data_received = transport.write
    protocol.data_received = request.transport.write

    return Response()
