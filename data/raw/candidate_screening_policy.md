# Candidate Screening — Business Rules v1.0

## Purpose
Screen applicants for a Junior Python/AI Engineer role before a human recruiter reviews the application.

## Required qualifications
1. Bachelor's degree in Computer Science, Information Technology, Engineering, Mathematics, Statistics, or a closely related field.
2. At least 0 years of professional experience; internships and academic projects are accepted.
3. Python fundamentals are required.
4. Candidate must be legally authorized to work in the hiring location.
5. Candidate must be able to work full-time.
6. Candidate must be available to join within 60 days.

## Preferred qualifications
- Machine Learning or Deep Learning project experience.
- REST API experience.
- SQL fundamentals.
- Git/GitHub experience.

## Screening questions
1. What degree did you complete and in which field?
2. How much professional or internship experience do you have?
3. How comfortable are you with Python?
4. Do you have experience with machine learning or AI projects?
5. Are you legally authorized to work in the hiring location?
6. Can you work full-time?
7. What is your notice period / earliest joining date?
8. Do you have any questions for the recruiter?

## Decision rules
- RECOMMEND: all required qualifications are satisfied.
- NEEDS_REVIEW: a required detail is unknown, conflicting, or cannot be verified.
- NOT_QUALIFIED: a required qualification is explicitly not satisfied.
- HUMAN_ESCALATION: candidate asks for a recruiter/human, reports a sensitive issue, or asks for a policy decision not covered by this document.

## Safe-answer rule
The assistant must not invent hiring policies, salary, interview dates, benefits, visa decisions, or company-specific information not present in the knowledge base.

## Privacy
Do not collect unnecessary sensitive personal information. Do not ask for passwords, financial account details, government ID numbers, health information, or other unnecessary sensitive data.

## Objection handling
- "Why do you need this information?" Explain that the questions are used only for preliminary role qualification and that a recruiter can handle further concerns.
- "Can you guarantee I will get an interview?" No. Explain that the bot only performs preliminary screening and a human recruiter makes the final decision.
- "What is the salary?" If salary information is not in the knowledge base, say it is not available in the current screening information and offer human escalation.
