#!/usr/bin/env python3
"""Tiny local web server for the ESP32 Smart Parking simulator (Python 3 standard library only)."""
import http.server, socketserver, webbrowser, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".js": "text/javascript", ".css": "text/css",
                      ".html": "text/html", ".glb": "model/gltf-binary"}
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()
    def log_message(self, *args):
        pass

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    for port in range(start, start + 20):
        try:
            srv = Server(("127.0.0.1", port), Handler)
            break
        except OSError:
            continue
    else:
        print("No free port found."); sys.exit(1)
    url = f"http://localhost:{port}"
    print(f"  Serving {ROOT}\n  Open {url}\n  Press Ctrl+C (or close this window) to stop.")
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
