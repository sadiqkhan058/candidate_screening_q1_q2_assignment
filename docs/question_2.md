# Question 2 — Production-Ready Knowledge Base

## Source material

The prototype uses:
- `candidate_screening_policy.md`
- `role_description.md`
- `faq.md`
- `source_with_pii_example.md`

These are synthetic sources because the uploaded assessment PDF does not include the separate business source pack.

## Cleaning

The ingestion pipeline:
- Normalizes line endings.
- Removes empty/repeated whitespace.
- Keeps useful headings/content.
- Redacts emails and phone numbers.
- Removes exact duplicate chunks using SHA-256 hashes over normalized text.

## Schema

Each record contains:

- `record_id`
- `title`
- `content`
- `category`
- `source`
- `version`
- `pii`
- `chunk_index`

## Chunking

Documents are split on paragraph boundaries with a maximum chunk size of approximately 900 characters. This keeps policy statements together while producing searchable units.

## Retrieval

The prototype uses TF-IDF with unigram/bigram features and cosine similarity. This keeps the demo reproducible and free of external infrastructure.

For production, a hybrid retrieval approach could combine lexical search with embeddings and a vector index.

## Citations

Every retrieval result returns:
- record ID
- title
- source
- version
- score
- content

This gives the voice agent traceability.

## Retrieval evaluation

Five test queries are required by the assessment. See `demo/retrieval_evaluation.md`.

## Connection to Q1

The Q1 agent calls the same KB retrieval layer for policy/FAQ questions. Therefore the voice agent is not disconnected from the knowledge base.
