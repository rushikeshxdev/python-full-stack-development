from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.end_headers()

        self.wfile.write(b"Hello! You just talked to a Python backend!")

server = HTTPServer(("localhost", 8001), MyServer)
print("Server running on port 8001")
server.serve_forever()
server.server_close()