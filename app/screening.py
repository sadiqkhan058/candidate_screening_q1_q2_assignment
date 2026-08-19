from dataclasses import dataclass, field
from typing import Dict, List, Optional
from .kb import KnowledgeBase


REQUIRED_FIELDS = [
    "degree",
    "experience",
    "python",
    "work_authorization",
    "full_time",
    "joining_days",
]

QUESTIONS = {
    "degree": "What degree did you complete, and what was your field of study?",
    "experience": "How much professional or internship experience do you have?",
    "python": "How comfortable are you with Python?",
    "ai_experience": "Do you have experience with machine learning or AI projects?",
    "work_authorization": "Are you legally authorized to work in the hiring location?",
    "full_time": "Are you available to work full-time?",
    "joining_days": "What is your notice period, or how soon could you join?",
}


@dataclass
class ScreeningSession:
    answers: Dict[str, str] = field(default_factory=dict)
    transcript: List[Dict[str, str]] = field(default_factory=list)
    status: str = "IN_PROGRESS"
    pending_clarification: Optional[str] = None


class ScreeningAgent:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def classify_answer(self, field: str, text: str) -> Optional[bool]:
        t = text.lower().strip()

        if field == "degree":
            return None  # store raw; validate with recruiter/LLM in production

        if field == "experience":
            return None

        if field == "python":
            if any(x in t for x in ["no", "not", "never"]):
                return False
            if any(x in t for x in ["yes", "comfortable", "good", "strong", "basic", "beginner", "experience"]):
                return True

        if field == "work_authorization":
            if any(x in t for x in ["no", "not authorized", "cannot"]):
                return False
            if any(x in t for x in ["yes", "authorized", "legally"]):
                return True

        if field == "full_time":
            if any(x in t for x in ["no", "part-time", "part time"]):
                return False
            if any(x in t for x in ["yes", "full-time", "full time"]):
                return True

        if field == "joining_days":
            nums = [int(x) for x in __import__("re").findall(r"\b\d+\b", t)]
            if nums:
                return nums[0] <= 60
            if "immediately" in t or "immediate" in t:
                return True

        return None

    def next_field(self, session: ScreeningSession) -> Optional[str]:
        for field in ["degree", "experience", "python", "ai_experience",
                      "work_authorization", "full_time", "joining_days"]:
            if field not in session.answers:
                return field
        return None

    def grounded_answer(self, user_text: str) -> str:
        # Salary is explicitly covered by the FAQ as unavailable. Handle it with
        # the exact grounded policy rather than allowing a low TF-IDF score to
        # produce a generic response.
        if "salary" in user_text.lower() or "compensation" in user_text.lower():
            return (
                "Salary information is not available in the current screening knowledge base, "
                "so I don't want to guess. Source: faq.md. I can connect you with a recruiter for salary-related questions."
            )

        results = self.kb.search(user_text, k=3)
        if not results or results[0]["score"] < 0.18:
            return (
                "I don't have that information in the current screening knowledge base, so I don't want to guess. "
                "I can connect you with a recruiter for that question."
            )
        top = results[0]
        content = top["content"]
        for line in content.splitlines():
            clean = line.strip().lstrip("- ")
            if clean and not clean.startswith("#"):
                return (
                    f"According to the screening information: {clean} "
                    f"Source: {top['source']}. This is preliminary screening information; a recruiter can help with further concerns."
                )
        return (
            f"I found relevant screening information but cannot provide a reliable answer from it. "
            f"Source: {top['source']}. I can connect you with a recruiter."
        )

    def is_out_of_scope_query(self, user_text: str) -> bool:
        """Detect candidate questions that should not be stored as screening answers."""
        t = user_text.lower().strip()
        explicit_topics = [
            "stock price", "share price", "stock market", "company valuation",
            "salary", "compensation", "benefits", "bonus", "interview date",
            "interview schedule", "office address", "company revenue", "profit",
            "ceo", "funding", "visa policy", "work visa", "relocation package",
        ]
        if any(topic in t for topic in explicit_topics):
            return True
        question_starts = [
            "what is ", "what's ", "what are ", "can you tell me", "when is ",
            "when will ", "where is ", "who is ", "how much does ", "how much is ",
            "how long is ",
        ]
        return "?" in t and any(t.startswith(start) for start in question_starts)

    def detect_conflict_or_mismatch(self, field: str, user_text: str) -> Optional[str]:
        """Detect obvious contradictions or answers that belong to another screening field.

        When details are inconsistent, the agent pauses the normal flow and asks for
        clarification instead of storing the statement under the wrong field.
        """
        t = user_text.lower().strip()

        if field == "experience":
            positive = any(p in t for p in [
                "years of professional experience", "years of work experience",
                "professional experience", "worked professionally"
            ])
            negative = any(p in t for p in [
                "i am a fresher", "no professional experience", "never worked professionally",
                "never worked full-time", "no work experience"
            ])
            if positive and negative:
                return (
                    "I noticed that your professional-experience details are inconsistent. "
                    "Could you please clarify whether you have any professional work experience, "
                    "and if so, how many years?"
                )

        # If the candidate gives experience information while we are asking for the degree,
        # do not incorrectly save that text as the degree. If it is also contradictory,
        # prioritize clarification of the experience details.
        if field == "degree" and any(p in t for p in [
            "professional experience", "work experience", "years of experience",
            "i am a fresher", "never worked professionally", "internship experience"
        ]):
            positive = any(p in t for p in [
                "years of professional experience", "years of work experience",
                "professional experience", "worked professionally"
            ])
            negative = any(p in t for p in [
                "i am a fresher", "no professional experience", "never worked professionally",
                "never worked full-time", "no work experience"
            ])
            if positive and negative:
                return (
                    "I noticed that your professional-experience details are inconsistent. "
                    "Could you please clarify whether you have any professional work experience, "
                    "and if so, how many years?"
                )
            return (
                "I noticed that your response contains experience information, but I was asking about your degree. "
                "Could you please provide your degree and field of study first?"
            )

        return None

    def handle_objection(self, user_text: str) -> Optional[str]:
        t = user_text.lower().strip()
        # These are intentionally explicit because they are business-rule examples
        # provided in the knowledge base, not invented policies.
        if any(p in t for p in [
            "why do you need", "why are you asking", "why do i need to provide",
            "why do i have to provide", "why do you ask"
        ]):
            return (
                "These questions are used only for preliminary qualification for the Junior Python/AI Engineer role. "
                "If you have concerns about providing the information, I can connect you with a human recruiter."
            )
        if any(p in t for p in [
            "guarantee an interview", "guarantee i will get", "will i definitely get an interview",
            "am i guaranteed an interview"
        ]):
            return (
                "No. This screening is preliminary and does not guarantee an interview. "
                "A human recruiter makes the final interview decision."
            )
        if "salary" in t or "compensation" in t or "benefits" in t:
            return self.grounded_answer(user_text)
        return None

    def process(self, session: ScreeningSession, user_text: str) -> str:
        session.transcript.append({"speaker": "candidate", "text": user_text})

        lower = user_text.lower()
        if any(p in lower for p in ["human", "recruiter", "speak to a person", "talk to a person", "real person"]):
            session.status = "HUMAN_ESCALATION"
            response = "Sure. I can mark this for human recruiter assistance. A recruiter will need to handle questions or decisions outside my screening scope."
            session.transcript.append({"speaker": "agent", "text": response})
            return response

        objection = self.handle_objection(user_text)
        if objection:
            session.transcript.append({"speaker": "agent", "text": objection})
            return objection

        # Candidate questions must be answered before field assignment. Otherwise an
        # out-of-scope question such as a stock-price question could accidentally be
        # stored as the current screening field (e.g. degree).
        if self.is_out_of_scope_query(user_text):
            response = self.grounded_answer(user_text)
            session.transcript.append({"speaker": "agent", "text": response})
            return response

        field = session.pending_clarification or self.next_field(session)
        if field is None:
            session.status = self.evaluate(session)
            response = self.final_response(session)
            session.transcript.append({"speaker": "agent", "text": response})
            return response

        mismatch = self.detect_conflict_or_mismatch(field, user_text)
        if mismatch:
            # If the problem was detected while asking another field, route the next
            # response to the field that needs clarification.
            if "professional-experience" in mismatch:
                session.pending_clarification = "experience"
            elif field == "experience":
                session.pending_clarification = "experience"
            session.transcript.append({"speaker": "agent", "text": mismatch})
            return mismatch

        session.pending_clarification = None
        session.answers[field] = user_text

        # Explicitly fail a required boolean requirement.
        decision = self.classify_answer(field, user_text)
        if decision is False and field in ["python", "work_authorization", "full_time"]:
            session.status = "NOT_QUALIFIED"
            response = f"Thanks for clarifying. Based on the stated screening requirements, this requirement is not currently satisfied. I can still escalate your application to a recruiter if you would like."
            session.transcript.append({"speaker": "agent", "text": response})
            return response

        next_f = self.next_field(session)
        if next_f:
            response = QUESTIONS[next_f]
        else:
            session.status = self.evaluate(session)
            response = self.final_response(session)

        session.transcript.append({"speaker": "agent", "text": response})
        return response

    def evaluate(self, session: ScreeningSession) -> str:
        for f in REQUIRED_FIELDS:
            if f not in session.answers or not session.answers[f].strip():
                return "NEEDS_REVIEW"
        return "RECOMMEND"

    def final_response(self, session: ScreeningSession) -> str:
        if session.status == "RECOMMEND":
            return "Thanks. Based on the information provided, you meet the stated preliminary screening requirements. This is not a guarantee of an interview; a human recruiter makes the final decision."
        return "Thanks. I have enough information to flag your application for recruiter review. A human recruiter can verify the remaining details."
