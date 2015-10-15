from src.handlers import *
import os.path
import tornado.options
import tornado.ioloop
import tornado.httpserver

tornado.options.define("port", default=8000, help="run on the given port", type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', DashboardHandler), (r'/module', ModuleHandler), (r'/task', TaskHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "pages"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()
