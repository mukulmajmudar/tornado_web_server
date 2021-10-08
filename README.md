# tornado_web_server
## Clean startup and shutdown for Tornado web servers
Call `tornado_web_server.start(url_handlers, port, address, settings, http_server_args)` to start the web server. Gracefully shutdown the server by sending the `SIGINT` (Ctrl+C) or `SIGTERM` signal.

Install with `pip install git+https://github.com/mukulmajmudar/tornado_web_server`.
