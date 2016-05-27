#coding:utf8
#time:2016.05.28
__author__ = 'tanghan'

from tornado import ioloop, options, httpserver
from application import application
from tornado.options import define,options

define('port', default=12345, help='run on given port', type=int)

def main():
    options.parse_command_line()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Control-C'
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()