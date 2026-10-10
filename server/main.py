from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        payload = {"status": "ok", "service": "reference-harvester-service"}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def log_message(self, format: str, *args) -> None:
        return


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    server = HTTPServer((host, port), ServerHandler)
    print(f"Starting server on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
