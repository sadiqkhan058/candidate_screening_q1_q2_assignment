# Final Submission Checklist

## Implementation

- [x] Q1 browser voice/text screening interface
- [x] Screening state machine and qualification rules
- [x] Objection handling
- [x] Conflicting-information clarification
- [x] Out-of-scope safe fallback
- [x] Human escalation
- [x] Q2 ingestion and cleaning pipeline
- [x] PII redaction example
- [x] Chunk metadata and source tracking
- [x] Deterministic retrieval
- [x] Five retrieval evaluations
- [x] Q1 connected to Q2 retrieval layer
- [x] Automated tests: 10 passed

## Evidence

- [x] Q1 scenario screenshots available from local testing
- [x] Two recordings covering three screening scenarios
- [ ] Add a third short test-call recording if possible, because the assessment wording asks for at least three test calls
- [x] Retrieval evidence in `docs/q2_retrieval_evidence.md`

## Files to submit

- Repository/project folder
- README.md
- requirements.txt
- .env.example
- docs/
- demo/
- data/
- tests/
- scripts/
- static/
- Recorded calls/transcripts where requested

## Security

- [x] No API keys or credentials committed
- [x] `.env.example` provided
- [x] PII example is redacted in processed knowledge-base content

## Final demo

1. Start the app.
2. Demonstrate a normal screening.
3. Demonstrate one objection or unsupported question.
4. Demonstrate human escalation.
5. Briefly show the retrieval evaluation and source traceability.
