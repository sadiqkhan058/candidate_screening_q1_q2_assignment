from __future__ import annotations
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from engine import NudgeEngine

ROOT = Path(__file__).resolve().parent
TRANSCRIPT = json.loads((ROOT / "demo_transcript.json").read_text())

STATE = {"started": False, "index": 0, "events": [], "chunks": [], "start_time": None}
ENGINE = NudgeEngine(threshold=.72, cooldown_seconds=8)


def reset():
    STATE.update(started=True, index=0, events=[], chunks=[], start_time=time.time())
    ENGINE.last_emitted.clear()


def tick():
    if not STATE["started"] or STATE["index"] >= len(TRANSCRIPT):
        return
    item = TRANSCRIPT[STATE["index"]]
    time.sleep(float(item.get("delay", 1)))
    received = time.time()
    text = item["text"]
    STATE["chunks"].append({"received_at": received, "speaker": item["speaker"], "text": text})
    for event in ENGINE.process(text, received):
        STATE["events"].append({**event.__dict__, "timestamp": received})
    STATE["index"] += 1
    if STATE["index"] >= len(TRANSCRIPT):
        STATE["started"] = False


class Handler(BaseHTTPRequestHandler):
    def _json(self, data):
        raw = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            raw = (ROOT / "dashboard.html").read_bytes()
            self.send_response(200); self.send_header("Content-Type", "text/html"); self.send_header("Content-Length", str(len(raw))); self.end_headers(); self.wfile.write(raw); return
        if path == "/api/state":
            self._json({"started": STATE["started"], "index": STATE["index"], "total": len(TRANSCRIPT), "chunks": STATE["chunks"], "events": STATE["events"]}); return
        self.send_error(404)

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/start":
            reset(); self._json({"ok": True}); return
        if path == "/api/tick":
            tick(); self._json({"ok": True}); return
        self.send_error(404)

    def log_message(self, *_):
        pass


if __name__ == "__main__":
    print("Q4 dashboard: http://127.0.0.1:8100")
    ThreadingHTTPServer(("127.0.0.1", 8100), Handler).serve_forever()
