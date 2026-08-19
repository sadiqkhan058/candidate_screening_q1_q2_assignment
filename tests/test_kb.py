import json
from pathlib import Path

from app.kb import KnowledgeBase

ROOT = Path(__file__).resolve().parents[1]

def test_kb_loads():
    kb = KnowledgeBase(str(ROOT / "data" / "processed" / "chunks.json"))
    assert len(kb.chunks) > 0

def test_salary_query_returns_grounded_source():
    kb = KnowledgeBase(str(ROOT / "data" / "processed" / "chunks.json"))
    results = kb.search("What salary will I receive?", 3)
    assert results
    assert any("salary" in r["content"].lower() for r in results)
