# Known Limitations and Production Improvements

## Current prototype limitations

1. Browser Web Speech APIs are used for the local demo and are not a production telephony stack.
2. Retrieval uses a lightweight TF-IDF implementation rather than a production hybrid/vector search service.
3. The prototype uses a synthetic candidate-screening source pack because the assessment PDF available for development did not include the separate business-source files.
4. The evaluation set is intentionally small and should be expanded for production regression testing.
5. Human escalation is represented in application state; a real deployment would connect it to a recruiter queue or contact center.

## Production improvements

- Use streaming production ASR/TTS or a telephony voice platform and measure P50/P95 latency.
- Add hybrid BM25/vector retrieval with reranking and metadata filtering.
- Add authentication, authorization, audit logging, rate limits and encrypted storage.
- Add stronger PII detection, retention and deletion policies.
- Integrate recruiter handoff with a ticket/ATS/contact-center workflow.
- Expand retrieval and screening regression tests and monitor precision/recall over time.
- Add observability for API latency, retrieval scores, fallback rate and escalation rate.
