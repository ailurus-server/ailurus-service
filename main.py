import os
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, url
from tornado.httpserver import HTTPServer

from handlers import PingHandler
from settings import memcache


def CreateApplication():
    return Application([
        url(r"/ping", PingHandler),
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logging.info("Serving on port " + str(port))

    app = CreateApplication()
    server = HTTPServer(app, xheaders=True)
    server.bind(port)
    server.start(0)
    IOLoop.current().start()
