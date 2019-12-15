from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from io import BytesIO
import cgitb; cgitb.enable()
import cgi

from trabalho import Teste
# import sys, os
# import time

# sys.path.append(os.environ['PYDFHOME'])
# from pyDF import *



class GP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        teste = Teste()
        teste.main()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8088...'
    httpd.serve_forever()

run()