from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from multi_agent_demo import MultiAgentLessonDemo, default_scenario, scenario_to_dict


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "web"
HOST = "127.0.0.1"
PORT = 8000


def build_demo_payload() -> dict[str, object]:
    scenario = default_scenario()
    demo = MultiAgentLessonDemo()
    return {
        "scenario": scenario_to_dict(scenario),
        "steps": demo.run_as_steps(scenario),
    }


class DemoRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/":
            self._serve_file(STATIC_DIR / "index_pl.html", content_type="text/html; charset=utf-8")
            return

        if parsed_path.path == "/api/demo":
            payload = json.dumps(build_demo_payload(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        if parsed_path.path.startswith("/static/"):
            relative_path = parsed_path.path.removeprefix("/static/")
            file_path = STATIC_DIR / relative_path
            content_type = self._guess_content_type(file_path.suffix)
            self._serve_file(file_path, content_type=content_type)
            return

        self.send_error(404, "Not Found")

    def log_message(self, format: str, *args: object) -> None:
        return

    def _serve_file(self, file_path: Path, content_type: str) -> None:
        if not file_path.exists():
            self.send_error(404, "Not Found")
            return

        payload = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    @staticmethod
    def _guess_content_type(suffix: str) -> str:
        if suffix == ".css":
            return "text/css; charset=utf-8"
        if suffix == ".js":
            return "application/javascript; charset=utf-8"
        return "text/plain; charset=utf-8"


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), DemoRequestHandler)
    print(f"Open http://{HOST}:{PORT} in your browser")
    print("Press Ctrl+C to stop the server")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
