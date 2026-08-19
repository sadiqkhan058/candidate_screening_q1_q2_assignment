# Question 1 — Test Results

The browser-based Candidate Screening Voice Agent was tested against the required screening scenarios.

## Results

| Test | Scenario | Observed result | Verdict |
|---|---|---|---|
| 1 | Cooperative candidate | Agent completed the preliminary screening flow and handled degree, experience, Python, AI/ML, authorization, availability and joining timeline. | PASS |
| 2 | Objection | Candidate asked why degree information was needed. Agent explained that the questions are for preliminary qualification and offered recruiter assistance. | PASS |
| 3 | Conflicting information | Candidate first stated 2 years of professional experience and then said they were a fresher. Agent detected the inconsistency and asked for clarification before continuing. | PASS |
| 4 | Out-of-scope question | Candidate asked for the company's current stock price. Agent stated that the information was not in the screening knowledge base and did not invent a value; recruiter assistance was offered. | PASS |
| 5 | Human escalation | Candidate explicitly requested a recruiter. Agent acknowledged the request and marked the interaction for human recruiter assistance. | PASS |

## Automated tests

Final local test run:

```text
10 passed
```

## Recorded evidence

Two recordings were captured covering three of the required scenarios. The recordings should be placed in `evidence/recordings/` before submission if audio files are included in the repository or submission package.

The current implementation also supports text fallback when browser speech recognition is unavailable.

## Known limitation

The assessment asks for at least three test calls. The current evidence set contains two recordings covering three scenarios. If time permits, add one short third recording before submission to remove this evidence gap.
