from dnsalert import dnsalert
import tornado

if __name__ == "__main__":
    #dnsalert.run(debug=True, host='127.0.0.1', port=9666)
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(dnsalert))
    http_server.listen(9666)
    IOLoop.instance().start()
