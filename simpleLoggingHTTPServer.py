import SimpleHTTPServer
import SocketServer
import cgi
import getopt
import sys

port = 8080

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print self.raw_requestline
        print self.headers

    def do_POST(self):
        
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print self.headers
        for item in form.list:
            print item

try:
    myopts, args = getopt.getopt(sys.argv[1:],"p:")
except getopt.GetoptError, e:
    print (str(e))
    print("Usage: %s -p port (Default 8080)" % sys.argv[0])
    sys.exit(2)

for o, a in myopts:
    if o == '-p':
        port=int(a)


print "serving at port", port

Handler = ServerHandler
httpd = SocketServer.TCPServer(("", port), Handler)
httpd.serve_forever()