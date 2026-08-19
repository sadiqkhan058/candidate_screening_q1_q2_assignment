# Question 2 — Retrieval Evidence

This document records the five retrieval queries executed by `scripts/evaluate_retrieval.py`.

The prototype uses deterministic TF-IDF retrieval over traceable knowledge-base chunks. Each result exposes a record ID, source, score and retrieved content.

## 1. Is machine learning mandatory?

**Retrieved record:** `kb_candidate_002`  
**Source:** `faq.md`  
**Score:** `0.2174`

**Retrieved evidence:** The FAQ states that machine learning is not mandatory; Python is required and machine-learning/deep-learning experience is preferred.

**Relevance:** Directly answers whether ML is mandatory and distinguishes required Python skills from preferred ML experience.

**Verdict:** **Correct**

## 2. How soon must a candidate be able to join?

**Retrieved record:** `kb_candidate_001`  
**Source:** `candidate_screening_policy.md`  
**Score:** `0.1204`

**Retrieved evidence:** The screening policy states that the candidate must be available to join within 60 days.

**Relevance:** Directly supports the joining-time qualification rule used by the screening state machine.

**Verdict:** **Correct**

## 3. Can an internship count as experience?

**Retrieved record:** `kb_candidate_002`  
**Source:** `faq.md`  
**Score:** `0.2113`

**Retrieved evidence:** The FAQ states that internships and academic projects are accepted for the experience question.

**Relevance:** Directly answers whether internship experience is accepted during screening.

**Verdict:** **Correct**

## 4. Can I ask for a recruiter?

**Retrieved record:** `kb_candidate_001`  
**Source:** `candidate_screening_policy.md`  
**Score:** `0.1451`

**Retrieved evidence:** The policy defines `HUMAN_ESCALATION` when a candidate asks for a recruiter/human or asks for a policy decision outside the documented screening scope. The FAQ also states that a candidate may request human assistance at any time.

**Relevance:** The retrieved policy record contains the explicit escalation rule. A second retrieved FAQ record (`kb_candidate_002`, `faq.md`, score `0.0785`) independently supports the same behavior.

**Verdict:** **Correct**

## 5. What salary will I receive?

**Retrieved record:** `kb_candidate_002`  
**Source:** `faq.md`  
**Score:** `0.1459`

**Retrieved evidence:** The FAQ explicitly states that the current screening knowledge base does not contain salary information and that the assistant should not invent it.

**Relevance:** This is the expected safe-answer behavior for an unsupported salary question and is the basis of the out-of-scope test demonstrated in Q1.

**Verdict:** **Correct**

## Retrieval summary

| # | Query | Top record | Source | Verdict |
|---|---|---|---|---|
| 1 | Is machine learning mandatory? | `kb_candidate_002` | `faq.md` | Correct |
| 2 | How soon must a candidate be able to join? | `kb_candidate_001` | `candidate_screening_policy.md` | Correct |
| 3 | Can an internship count as experience? | `kb_candidate_002` | `faq.md` | Correct |
| 4 | Can I ask for a recruiter? | `kb_candidate_001` | `candidate_screening_policy.md` | Correct |
| 5 | What salary will I receive? | `kb_candidate_002` | `faq.md` | Correct |

## Traceability

The source files are stored under `data/raw/`, and processed chunks are stored in `data/processed/chunks.json`. The Q1 agent uses the same KB retrieval layer for policy/FAQ questions, keeping the retrieval layer connected to the voice-agent flow.

## Prototype limitation

The current retrieval layer is intentionally lightweight and deterministic. For production, retrieval quality could be improved with hybrid lexical/vector retrieval, reranking, metadata filters, larger evaluation sets and regression monitoring.
