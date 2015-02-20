import os
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler, url
from tornado.httpserver import HTTPServer

from handlers import PingHandler, SetupHandler
from settings import memcache, on_heroku
from tornado.options import parse_command_line


def CreateApplication(debug=False):
    base = os.path.dirname(__file__)

    # Common handlers and settings
    application = Application(
        handlers=[
            url(r"/static/(.*)", StaticFileHandler, {
                'path': os.path.join(base, 'static')
            })],
        template_path=os.path.join(base, "templates"),
        debug=debug
    )

    # api.ailurus.ca
    application.add_handlers(r"api\.ailurus\.ca", [
        url(r"/ping", PingHandler),
    ])

    # setup.ailurus.ca
    application.add_handlers(r"setup\.ailurus\.ca", [
        url(r"/", SetupHandler),
    ])

    return application

if __name__ == "__main__":
    parse_command_line()
    port = int(os.environ.get("PORT", 80))
    logging.info("Serving on port " + str(port))

    if on_heroku:
        app = CreateApplication()
        server = HTTPServer(app, xheaders=True)
        server.bind(port)
        server.start(0)
    else:
        app = CreateApplication(debug=True)
        app.listen(port)
    IOLoop.current().start()
