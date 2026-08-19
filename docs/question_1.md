# Question 1 — Candidate Screening Voice Agent

## Use case

A voice assistant conducts preliminary screening for a Junior Python/AI Engineer role.

## Conversation flow

1. Greeting and consent/context.
2. Degree and field.
3. Experience.
4. Python comfort.
5. AI/ML project experience.
6. Work authorization.
7. Full-time availability.
8. Joining timeline.
9. Final preliminary result.
10. Human escalation whenever requested.

## Qualification logic

Required:
- Relevant bachelor's degree.
- Python fundamentals.
- Legal work authorization.
- Full-time availability.
- Joining within 60 days.

Experience may be zero because internships and academic projects are accepted.

ML/DL, REST APIs, SQL and Git/GitHub are preferred rather than mandatory.

## Grounding

The agent uses the Q2 knowledge base for policy/FAQ questions. It does not rely on a prompt containing all FAQs.

## Safe fallback

If the KB does not contain an answer:
> "I don't have that information in the current screening knowledge base. I can connect you with a recruiter for that question."

## Human escalation

Escalation occurs when:
- Candidate explicitly requests a human/recruiter.
- Candidate asks for a decision outside the documented screening scope.

## Required test coverage

The assessment asks for:
- Cooperative customer/candidate.
- Objection.
- Incomplete or conflicting details.
- Out-of-scope question.
- Human-assistance request.

The demo plan in `demo/test_cases.md` covers these.
