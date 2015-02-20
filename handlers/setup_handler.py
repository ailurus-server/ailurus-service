from tornado.web import RequestHandler


class SetupHandler(RequestHandler):
    def get(self):
        self.render("setup.html")
