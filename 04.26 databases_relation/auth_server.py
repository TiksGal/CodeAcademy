import base64
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
USERNAME = "Marius"
PASSWORD = "testas"

class AuthRequestHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.headers.get("Authorization") is None:
            self.send_response(401)
            self.send_header("WWW-Authenticate", "Basic realm=\"Authentication required\"")
            self.end_headers()
            self.wfile.write(b"Authorization required.")
        elif self.is_authenticated(self.headers.get("Authorization")):
            self.do_HEAD()
            self.wfile.write(b"Hello, authenticated user! Glad to see you again!")
        else:
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Forbidden. Wrong credentials.")

    def is_authenticated(self, auth_header):
        auth_type, auth_string = auth_header.split(" ")
        auth_string = base64.b64decode(auth_string).decode("utf-8")
        username, password = auth_string.split(":")
        return username == USERNAME and password == PASSWORD

if __name__ == "__main__":
    with HTTPServer(("", PORT), AuthRequestHandler) as httpd:
        print(f"Serving on port {PORT} with Basic Authentication")
        httpd.serve_forever()

