def do_GET(self):
    if self.path == '/':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, this is a simple API!'.encode())

    elif self.path == '/data':
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.wfile.write(json.dumps(data).encode('utf-8'))

    elif self.path == '/status':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("OK".encode('utf-8'))

    elif self.path == '/info':
        self._set_headers(content_type='application/json')
        data = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }
        self.wfile.write(json.dumps(data).encode('utf-8'))

    else:
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        error_data = {
            "error": "Not Found",
            "message": f"The endpoint '{self.path}' does not exist."
        }
        self.wfile.write(json.dumps(error_data).encode('utf-8'))
