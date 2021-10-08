import logging
import asyncio

import tornado.web
import tornado.httpserver
import asyncio_application

logger = logging.getLogger(__name__)
http_server = None

def start(url_handlers, port=80, address='', settings=None, http_server_args=None):
    '''
    Start the Tornado web server.

    This call is blocking as it starts the event loop.
    '''
    if settings is None:
        settings = {}
    if http_server_args is None:
        http_server_args = {}

    # Create Tornado application
    tornado_app = tornado.web.Application(url_handlers, **settings)

    # Create a new HTTPServer
    global http_server
    http_server = tornado.httpserver.HTTPServer(tornado_app, **http_server_args)

    # Start listening
    http_server.listen(port, address)

    loop = asyncio.get_event_loop()

    # Log on next loop iteration
    loop.call_soon(lambda: logger.info('Started web server'))

    # Start the asyncio application (blocking – starts event loop)
    asyncio_application.start()

    # When we get here, the asyncio application has been shutdown and the loop
    # has stopped. So we run the shutdown procedure.
    loop.run_until_complete(shutdown())


async def shutdown():
    # Stop the HTTPServer from listening for new connections.
    http_server.stop()

    # Close all connections
    await http_server.close_all_connections()
