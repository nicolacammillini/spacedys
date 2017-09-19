from socketserver import StreamRequestHandler, ThreadingTCPServer

class SpacedysHandler(StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())

class SpacedysServer(ThreadingTCPServer):
    pass



server = SpacedysServer(('localhost', 9345), SpacedysHandler)

server.serve_forever()

