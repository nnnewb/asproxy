import logging
from asyncio import sleep, get_event_loop

import coloredlogs
from aiohttp.web import Server, ServerRunner, TCPSite

from asproxy.server import proxy_handler

coloredlogs.install(level=logging.DEBUG, fmt='%(asctime)s [%(levelname).1s] %(name)s: %(message)s')


async def main():
    host = '127.0.0.1'
    port = 8080
    server = Server(proxy_handler)
    runner = ServerRunner(server)
    await runner.setup()
    site = TCPSite(runner, host, port)
    await site.start()

    print(f'============== Serving on http://{host}:{port}/ ===================')

    # pause here for serving
    while True:
        await sleep(100 * 3600)


loop = get_event_loop()
try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
loop.close()
