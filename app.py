"""
Quick local server for AADI.
Run this instead of Streamlit — it serves index.html directly,
with NO iframe sandbox, so opening websites/YouTube works properly.

Usage:
    python run_local.py

Then open the printed URL in Chrome or Edge.
Other devices on the SAME WiFi can open http://<your-ip>:8000 too.
"""

import http.server
import socketserver
import socket
import webbrowser
import os

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Helpful CORS header in case you fetch external files later
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


if __name__ == "__main__":
    local_ip = get_local_ip()
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print("=" * 55)
        print(f"AADI is running!")
        print(f"  On this PC:        http://localhost:{PORT}")
        print(f"  On other devices:  http://{local_ip}:{PORT}")
        print("  (Other devices must be on the same WiFi network)")
        print("=" * 55)
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping AADI server...")