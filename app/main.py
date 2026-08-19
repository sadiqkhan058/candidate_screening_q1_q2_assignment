from contextlib import asynccontextmanager
from pathlib import Path
from typing import Dict, Any

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .kb import KnowledgeBase
from .screening import ScreeningAgent, ScreeningSession


ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "data" / "processed" / "chunks.json"
STATIC = ROOT / "static"

@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_agent()
    yield


app = FastAPI(title="Candidate Screening Voice Agent", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=STATIC), name="static")

kb = None
agent = None
sessions: Dict[str, ScreeningSession] = {}


def ensure_agent():
    """Initialize the KB/agent lazily as a safe fallback for tests and alternate ASGI runners."""
    global kb, agent
    if agent is not None:
        return agent
    if not CHUNKS.exists():
        raise RuntimeError("Knowledge base is missing. Run: python scripts/ingest.py")
    kb = KnowledgeBase(str(CHUNKS))
    agent = ScreeningAgent(kb)
    return agent



class StartResponse(BaseModel):
    session_id: str
    message: str


class MessageRequest(BaseModel):
    session_id: str
    text: str


@app.get("/")
def home():
    return FileResponse(STATIC / "index.html")


@app.post("/api/session", response_model=StartResponse)
def start_session():
    ensure_agent()
    import uuid
    sid = str(uuid.uuid4())
    sessions[sid] = ScreeningSession()
    message = (
        "Hello. I am the preliminary screening assistant for the Junior Python/AI Engineer role. "
        "I will ask a few questions about your qualifications. You can request a recruiter at any time. "
        "To begin, what degree did you complete, and what was your field of study?"
    )
    sessions[sid].transcript.append({"speaker": "agent", "text": message})
    return {"session_id": sid, "message": message}


@app.post("/api/message")
def message(req: MessageRequest):
    ensure_agent()
    if req.session_id not in sessions:
        return {"error": "Session not found"}
    response = agent.process(sessions[req.session_id], req.text)
    return {
        "response": response,
        "status": sessions[req.session_id].status,
        "answers": sessions[req.session_id].answers,
    }


@app.get("/api/kb/search")
def kb_search(q: str, k: int = 4):
    ensure_agent()
    return {"query": q, "results": kb.search(q, k)}


@app.get("/api/session/{session_id}")
def session_data(session_id: str):
    if session_id not in sessions:
        return {"error": "Session not found"}
    s = sessions[session_id]
    return {
        "status": s.status,
        "answers": s.answers,
        "transcript": s.transcript,
    }
