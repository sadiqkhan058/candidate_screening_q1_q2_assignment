# Q4 Latency / Quality Report

## What the prototype measures

Each incoming transcript chunk is timestamped when received. Signal extraction and nudge generation happen immediately in the same process. The dashboard polls the current state once per second for a simple live display.

## Required evaluation areas

| Area | Prototype evidence |
|---|---|
| Real-time processing | Transcript chunks are delayed and processed one at a time during replay |
| Useful nudges | Four required signal types are implemented |
| Duplicate suppression | Per-signal cooldown prevents repetitive alerts |
| Confidence control | Threshold defaults to 0.72 |
| Noisy/ambiguous calls | Unmatched chunks generate no nudge |
| Missed opportunity | A call can mention a second vehicle; the cross-sell nudge is emitted immediately |

Exact P50/P95 numbers are not claimed because this local prototype has not been benchmarked under production load. For the walkthrough, show the live dashboard and mention this limitation explicitly.
