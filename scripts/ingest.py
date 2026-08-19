import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

PII_PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone": re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{8,}\d)(?!\d)"),
}

def clean(text: str) -> str:
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = []
    for line in text.splitlines():
        if line.strip():
            lines.append(line.strip())
    return "\n".join(lines)

def redact_pii(text: str):
    found = False
    for _, pattern in PII_PATTERNS.items():
        if pattern.search(text):
            found = True
            text = pattern.sub("[REDACTED_PII]", text)
    return text, found

def split_chunks(text: str, max_chars=900):
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, current = [], ""
    for p in paragraphs:
        if len(current) + len(p) + 2 <= max_chars:
            current = f"{current}\n\n{p}".strip()
        else:
            if current:
                chunks.append(current)
            current = p
    if current:
        chunks.append(current)
    return chunks

records = []
seen = set()

for path in sorted(RAW.glob("*.md")):
    raw = path.read_text(encoding="utf-8")
    text = clean(raw)
    text, pii = redact_pii(text)
    for i, chunk in enumerate(split_chunks(text)):
        norm = re.sub(r"\W+", " ", chunk.lower()).strip()
        digest = hashlib.sha256(norm.encode()).hexdigest()
        if digest in seen:
            continue
        seen.add(digest)
        title = next((x[2:].strip() for x in chunk.splitlines() if x.startswith("# ")), path.stem)
        category = "policy" if "policy" in path.stem else "role" if "role" in path.stem else "faq" if "faq" in path.stem else "application_example"
        records.append({
            "record_id": f"kb_candidate_{len(records)+1:03d}",
            "title": title,
            "content": chunk,
            "category": category,
            "source": path.name,
            "version": "1.0",
            "pii": pii,
            "chunk_index": i,
        })

(OUT / "chunks.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
print(f"Created {len(records)} traceable chunks at {OUT/'chunks.json'}")
