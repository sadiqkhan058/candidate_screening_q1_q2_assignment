# Indonesia Voice Bot Test Cases

## Test Case 1 — Cooperative Customer

Customer:
"Saya ingin tahu lebih banyak tentang pembiayaan yang tersedia."

Expected behavior:
The bot should respond politely in natural Bahasa Indonesia and explain the available information.

Expected result:
The bot should continue the conversation naturally without inventing product details.

---

## Test Case 2 — Finance-Specific Objection

Customer:
"Kenapa saya harus bayar sekarang? Saya belum bisa membayar cicilan."

Expected behavior:
The bot should acknowledge the customer's concern and explain available payment-support options without making unsupported promises.

Expected result:
The bot should remain helpful and offer escalation when necessary.

---

## Test Case 3 — Mixed Indonesian/English Finance Terms

Customer:
"Saya mau follow-up application saya, statusnya sudah sampai mana?"

Expected behavior:
The bot should understand the Indonesian/English combination.

Expected result:
The bot should respond naturally and preserve common finance terminology.

---

## Test Case 4 — Colloquial Bahasa Indonesia

Customer:
"Cicilan saya jatuh tempo kapan ya?"

Expected behavior:
The bot should understand informal conversational Indonesian.

Expected result:
The response should sound natural rather than overly formal.

---

## Test Case 5 — Human Escalation

Customer:
"Saya mau bicara dengan petugas."

Expected behavior:
The bot should acknowledge the request and provide human escalation.

Expected result:
The bot should not continue automated handling unnecessarily.

---

## Test Case 6 — Regional Accent

Customer:
The customer speaks Indonesian with a regional accent outside standard Jakarta speech.

Expected behavior:
The bot should tolerate reasonable regional pronunciation differences.

Expected result:
The bot should continue the conversation without unnecessarily switching languages or repeatedly asking the customer to repeat.

---

## Test Case 7 — Language-Preserving Fallback

Customer:
"Berapa tepatnya denda yang harus saya bayar?"

Expected behavior:
If the exact penalty information is unavailable, the bot should clearly state the limitation.

Expected response:
"Maaf, saya tidak memiliki informasi yang cukup untuk memastikan jumlah dendanya. Saya bisa menghubungkan Anda dengan petugas untuk mendapatkan informasi yang tepat."

Expected result:
The bot must not invent a penalty amount.

---

## Test Case 8 — Installment Reminder

Customer:
"Besok cicilan saya jatuh tempo. Bagaimana cara pembayarannya?"

Expected behavior:
The bot should explain available payment information when supported by the knowledge base.

Expected result:
If specific payment details are unavailable, the bot should offer human assistance instead of guessing.

---

## Test Case 9 — Loan Qualification

Customer:
"Kalau saya mau mengajukan pinjaman, apa saja syaratnya?"

Expected behavior:
The bot should explain available qualification information without making an approval decision.

Expected result:
The bot should distinguish between general information and an actual eligibility decision.

---

## Test Case 10 — Collections Support

Customer:
"Saya sedang kesulitan membayar angsuran bulan ini."

Expected behavior:
The bot should acknowledge the situation and provide available payment-support or escalation options.

Expected result:
The bot should remain respectful and avoid making unsupported commitments.

---

## Test Coverage Summary

The Indonesia bot should demonstrate:

- Cooperative customer handling.
- Finance-specific objection handling.
- Mixed Indonesian/English terminology.
- Colloquial Bahasa Indonesia.
- Human escalation.
- Regional accent tolerance.
- Language-preserving fallback.
- Installment reminder handling.
- Loan qualification handling.
- Collections support.
