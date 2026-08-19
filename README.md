# Candidate Screening Voice Agent + Production Knowledge Base

This repository implements Questions 1 and 2 of the AI Engineer Assessment using the **Candidate Screening** use case.

## Important assessment note

The assessment PDF requires the voice agent to use a "provided script and business rules", but the uploaded PDF itself does not contain those materials. This project therefore includes a clearly labelled **synthetic candidate-screening policy pack** so the prototype is runnable. Replace the files under `data/raw/` with the actual materials supplied by the assessment before final submission.

## What is implemented

### Question 1 — Knowledge-Grounded Voice Agent
- Browser-based web calling interface.
- Candidate screening conversation flow.
- Qualification logic.
- Objection handling grounded in the knowledge base.
- Unsupported-question fallback.
- Human escalation.
- Lead/application summary action.
- Call transcript and test result capture.

### Question 2 — Production-Ready Knowledge Base
- Document ingestion.
- Text cleaning.
- Duplicate removal.
- PII detection/redaction.
- Chunking with metadata.
- TF-IDF retrieval (no paid vector database required).
- Source citations.
- Five retrieval evaluation cases.
- API endpoint used directly by the voice agent.

## Architecture

```text
Candidate
   |
   v
Browser Voice UI
   |
   | speech-to-text / text-to-speech
   v
FastAPI Voice Agent
   |
   +----> Screening state machine
   |
   +----> RAG retrieval --------------------+
   |                                         |
   v                                         v
Response generation                  Knowledge Base
   |                                  chunks + metadata
   v
Transcript / screening summary
```

## Run locally

Python 3.10+ recommended.

```bash
cd candidate_screening_assignment
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows
# .venv\Scripts\activate

pip install -r requirements.txt

python scripts/ingest.py
uvicorn app.main:app --reload
```

Open:

`http://127.0.0.1:8000`

The browser interface uses the browser's speech recognition/speech synthesis where supported. If speech recognition is unavailable, use the text input in the same interface.

## Environment variables

Copy `.env.example` to `.env`.

The core prototype does not require an LLM API key. An LLM can be added later for more natural response generation, while retrieval and business rules remain grounded in the knowledge base.

## Test

```bash
pytest -q
```

Retrieval evaluation:

```bash
python scripts/evaluate_retrieval.py
```

## Assessment evidence

- `docs/question_1.md` — Q1 implementation and test plan.
- `docs/question_2.md` — Q2 knowledge-base design.
- `docs/architecture.md` — architecture and design decisions.
- `demo/test_cases.md` — required Q1 test coverage.
- `demo/retrieval_evaluation.md` — five Q2 retrieval tests.
- `docs/q1_test_results.md` — observed Q1 test results.
- `docs/q2_retrieval_evidence.md` — five retrieval queries with sources, relevance and verdicts.
- `docs/submission_checklist.md` — final submission checklist.
- `docs/known_limitations.md` — prototype limitations and production improvements.
- `evidence/recordings/` — location for recorded call evidence.
- `data/raw/` — source business material used by the prototype.
- `data/processed/chunks.json` — traceable indexed chunks.

## Production improvements

Before production:
- Replace browser speech APIs with a dedicated voice/telephony platform.
- Add production ASR/TTS with measured latency.
- Replace local TF-IDF retrieval with a managed vector/hybrid search layer if scale requires it.
- Add authentication, encryption, audit logs, rate limits and access controls.
- Add proper PII detection and retention policies.
- Add human handoff integration.
- Add automated regression evaluation for retrieval and screening decisions.
