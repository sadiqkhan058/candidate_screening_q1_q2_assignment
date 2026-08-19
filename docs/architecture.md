# Architecture

## Components

### 1. Web voice interface
Browser microphone -> SpeechRecognition -> text -> API -> response -> SpeechSynthesis.

### 2. FastAPI application
Exposes:
- `POST /api/session`
- `POST /api/message`
- `GET /api/session/{session_id}`
- `GET /api/kb/search`

### 3. Screening state machine
Stores answers, applies required qualification rules, detects human escalation, and produces the preliminary result.

### 4. Knowledge base
Ingested chunks are stored in JSON for this assessment prototype. TF-IDF provides deterministic retrieval and source traceability.

## Production architecture

```text
Telephony/Web Call
      |
      v
Voice Platform / Streaming ASR
      |
      v
Conversation Orchestrator
      |
      +--------> Screening State
      |
      +--------> Hybrid RAG
                     |
                 Vector + BM25
                     |
                 Source records
      |
      v
Response Generator
      |
      v
TTS
      |
      v
Candidate
```

## Why this design

The assessment prioritizes reliable core workflow over unnecessary visual polish. The prototype therefore keeps the business logic explicit and auditable, while grounding information retrieval in traceable records.

## Known limitation

Browser speech APIs are not equivalent to a production telephony voice stack. Before final submission, use the target voice platform specified by the employer or integrate a production voice provider, and measure real call latency.
