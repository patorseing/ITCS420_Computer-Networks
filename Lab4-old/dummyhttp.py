# !/usr/bin/python
#Ms. Napatchol Thaipanich 5888205 sec2
#Mr. Arnuphap yupuech 5888236 sec2

import SimpleHTTPServer
import SocketServer

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print "I received a GET request"
        self.wfile.write("LOVE U ALL")


PORT = 3605

httpd = SocketServer.TCPServer(('', PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()
