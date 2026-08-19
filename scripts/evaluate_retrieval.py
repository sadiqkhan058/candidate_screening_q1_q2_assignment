import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.kb import KnowledgeBase

ROOT = Path(__file__).resolve().parents[1]
kb = KnowledgeBase(str(ROOT / "data" / "processed" / "chunks.json"))

queries = [
    "Is machine learning mandatory?",
    "How soon must a candidate be able to join?",
    "Can an internship count as experience?",
    "Can I ask for a recruiter?",
    "What salary will I receive?",
]

for q in queries:
    results = kb.search(q, 2)
    print("\nQUESTION:", q)
    for r in results:
        print(f"  {r['record_id']} | score={r['score']} | source={r['source']}")
        print("  ", r["content"][:220].replace("\n", " "))
