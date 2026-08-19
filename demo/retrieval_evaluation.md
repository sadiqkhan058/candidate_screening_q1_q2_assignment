# Q2 Retrieval Evaluation

| # | Query | Expected source/topic | Verdict |
|---|---|---|---|
| 1 | Is machine learning mandatory? | FAQ: ML is preferred, not mandatory | Correct |
| 2 | How soon must I be able to join? | Policy/role: within 60 days | Correct |
| 3 | Does an internship count as experience? | FAQ/policy: yes | Correct |
| 4 | Can I request a recruiter? | FAQ/policy: yes | Correct |
| 5 | What salary will I receive? | Role/FAQ: salary not provided | Correct if system retrieves this absence statement |

Run `python scripts/evaluate_retrieval.py` to inspect the retrieved chunks and scores.

For the final assessment submission, replace this expected table with actual measured results, including the retrieved record ID, source reference, relevance explanation, and verdict for each query.
