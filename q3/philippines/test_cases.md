# Philippines Voice Bot Test Cases

## Test Case 1 — Cooperative Customer

Customer:
"Hi, I'd like to know more about your life insurance plans."

Expected behavior:
The bot should respond politely and naturally in English or Filipino/Tagalog depending on the customer's language.

Expected result:
The bot explains available information without inventing policy details and can continue with lead qualification.

---

## Test Case 2 — Sector-Specific Objection

Customer:
"Why do I need life insurance? I already have savings."

Expected behavior:
The bot should acknowledge the concern and explain the general purpose of life insurance without making unsupported financial claims.

Expected result:
The bot remains helpful and does not pressure the customer.

---

## Test Case 3 — Mixed English/Filipino Finance Terms

Customer:
"Pwede ko bang malaman kung magkano ang premium and ano yung coverage?"

Expected behavior:
The bot should understand the English/Filipino combination and respond naturally.

Expected result:
The bot should preserve common insurance terminology such as premium and coverage rather than performing literal translation.

---

## Test Case 4 — Colloquial Taglish

Customer:
"Pwede ba ako magpa-check kung okay na yung policy ko?"

Expected behavior:
The bot should understand natural Taglish and respond conversationally.

Expected result:
The bot should not force the customer into formal English or formal Filipino.

---

## Test Case 5 — Human Escalation

Customer:
"I need to speak with someone about my policy."

Expected behavior:
The bot should acknowledge the request and provide human escalation.

Expected result:
The bot should not continue automated screening unnecessarily.

---

## Test Case 6 — Insurance Terminology

Customer:
"What's the difference between the beneficiary and the policyholder?"

Expected behavior:
The bot should recognize standard insurance terminology and explain the distinction using clear language.

Expected result:
The response should use terms such as beneficiary and policyholder naturally.

---

## Test Case 7 — Language-Preserving Fallback

Customer:
"May coverage ba ako for something that's not listed in my policy?"

Expected behavior:
If the specific policy information is unavailable, the bot should clearly state the limitation.

Expected response:
"Sorry, I don't have access to that specific policy detail. I can connect you with a representative who can check it for you."

Expected result:
No policy detail should be invented.

---

## Test Case 8 — Premium Reminder

Customer:
"Kailan yung next premium payment ko?"

Expected behavior:
The bot should help if the payment information is available.

Expected result:
If the exact date is unavailable, the bot should state the limitation and offer human assistance rather than guessing.

---

## Test Case 9 — Bancaassurance Cross-Sell

Customer:
"I already have life insurance. Do you have anything else that might be useful?"

Expected behavior:
The bot may explain that other relevant insurance or bancassurance products may exist, but should not invent product details.

Expected result:
The bot should identify a possible cross-sell opportunity and provide appropriate information or escalation.

---

## Test Coverage Summary

The Philippines bot should demonstrate:

- Cooperative customer handling.
- Sector-specific objection handling.
- Mixed English/Filipino finance terminology.
- Natural Taglish conversation.
- Human escalation.
- Natural insurance terminology.
- Language-preserving fallback.
- Premium reminder handling.
- Bancassurance cross-sell opportunity handling.
