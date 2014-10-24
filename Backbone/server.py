import argparse
import tornado.web
import tornado.httpserver
import tornado.ioloop

if __name__ == "__main__":
    bindport = 4545
    bindhost = "0.0.0.0"
    parser = argparse.ArgumentParser()
    parser.add_argument("-http", help="host:port for http connections")
    args = parser.parse_args()

    if args.http:
        bindhost, bindport = args.http.split(":")

    application = tornado.web.Application([
        (r"/backbone/(.+)", tornado.web.StaticFileHandler, {'path': "html"}),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(bindport, bindhost)
    tornado.ioloop.IOLoop.instance().start()
