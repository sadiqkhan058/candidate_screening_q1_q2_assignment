# Question 4 — Live Insights and Nudges From Call Audio

A fast, self-contained real-time prototype for detecting useful call signals and generating agent nudges.

## Pipeline

```text
Simulated/replayed call chunks
        ↓
Streaming transcript chunks
        ↓
Signal extraction
        ↓
Confidence threshold
        ↓
Duplicate suppression + cooldown
        ↓
Nudge generation
        ↓
Live browser dashboard
```

## Why transcript replay?

The assignment explicitly permits **live call audio or a recording replayed at real-time speed**. To keep the prototype fast and dependency-free, `demo_transcript.json` represents the streaming ASR output of a replayed call. Each chunk is delayed before processing, so nudges appear while the call is still in progress rather than after a completed recording is uploaded.

## Signals implemented

- **Missed cross-sell** — second/another vehicle → multi-vehicle offer suggestion.
- **Compliance risk** — required disclosure language → reminder before proceeding.
- **Rising frustration** — frustration/anger phrases → acknowledge concern.
- **Payment difficulty** — inability to pay → approved support/callback path.

## Run

```bash
cd q4
python server.py
```

Open `http://127.0.0.1:8100` and click **Start live replay**.

## Tests

```bash
cd q4
python -m pytest -q
```

## Latency

The server records the arrival time of each transcript chunk and immediately runs signal extraction/nudge logic in-process. This demo intentionally has no external LLM/API call, so processing overhead is expected to be small relative to the simulated audio delay. A production deployment should measure ASR, signal extraction, LLM (if used), and delivery separately and report P50/P95 latency under concurrent load.

## Limitations

- Transcript chunks stand in for actual streaming ASR audio.
- Signal extraction is deterministic keyword/rule based.
- No telephony integration is included.
- A production system should use streaming ASR, richer classifiers, authenticated WebSocket/webhook delivery, persistence, observability, and load testing.
- False positives should be measured on a larger labelled call set.
