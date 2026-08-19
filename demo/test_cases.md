# Q1 Test Cases

## Test 1 — Cooperative candidate
Expected:
- Agent asks all screening questions.
- Candidate satisfies required conditions.
- Final status: RECOMMEND.
- Agent clearly says this is preliminary and not an interview guarantee.

## Test 2 — Objection
Candidate asks:
"Why do you need this information?"

Expected:
- Agent explains the information is for preliminary qualification.
- No unsupported policy is invented.

## Test 3 — Incomplete/conflicting details
Candidate first says:
"I can join in 90 days."
Later says:
"Actually I can join in 45 days."

Expected:
- Application should be flagged for verification rather than silently assuming the latest answer is correct in a production implementation.
- Current prototype stores the answer and should be upgraded with explicit conflict detection before final production submission.

## Test 4 — Out-of-scope question
Candidate asks:
"What is the salary?"

Expected:
- Agent does not invent a salary.
- Agent says salary is not available in the current knowledge base.
- Human escalation is offered.

## Test 5 — Human assistance
Candidate says:
"I want to speak to a recruiter."

Expected:
- Immediate HUMAN_ESCALATION status.
- Agent acknowledges the request.

## Three recordings required by the assessment

Record at minimum:
1. Cooperative candidate.
2. Objection or out-of-scope question.
3. Human escalation or incomplete/conflicting details.

The assessment requires at least three test calls and transcripts/results.
