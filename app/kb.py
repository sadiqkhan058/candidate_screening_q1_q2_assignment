import json
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class Chunk:
    record_id: str
    title: str
    content: str
    category: str
    source: str
    version: str
    pii: bool
    chunk_index: int


class KnowledgeBase:
    def __init__(self, chunks_path: str):
        self.chunks_path = chunks_path
        self.chunks: List[Chunk] = []
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = None
        self.load()

    def load(self):
        with open(self.chunks_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        self.chunks = [Chunk(**x) for x in raw]
        self.matrix = self.vectorizer.fit_transform([c.content for c in self.chunks])

    def search(self, query: str, k: int = 4) -> List[Dict[str, Any]]:
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix)[0]
        order = scores.argsort()[::-1][:k]
        results = []
        for idx in order:
            c = self.chunks[int(idx)]
            results.append({
                "record_id": c.record_id,
                "title": c.title,
                "content": c.content,
                "category": c.category,
                "source": c.source,
                "version": c.version,
                "score": round(float(scores[idx]), 4),
            })
        return results

    def context(self, query: str, k: int = 4) -> str:
        results = self.search(query, k)
        return "\n\n".join(
            f"[{r['record_id']}] {r['title']} ({r['source']})\n{r['content']}"
            for r in results
        )
