from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import urllib.parse

# Define metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            # Prometheus metrics endpoint
            self.send_response(200)
            self.send_header('Content-Type', CONTENT_TYPE_LATEST)
            self.end_headers()
            self.wfile.write(generate_latest())
        else:
            # Main app endpoint
            REQUEST_COUNT.inc()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"DevOps Capstone App - Running!")

    def log_message(self, format, *args):
        pass  # suppress access logs

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Server running on port 8080")
    server.serve_forever()
