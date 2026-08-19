from pathlib import Path
from app.kb import KnowledgeBase
from app.screening import ScreeningAgent, ScreeningSession

ROOT = Path(__file__).resolve().parents[1]

def make_agent():
    kb = KnowledgeBase(str(ROOT / "data" / "processed" / "chunks.json"))
    return ScreeningAgent(kb)

def test_not_qualified_without_python():
    a = make_agent()
    s = ScreeningSession()
    a.process(s, "I completed BTech in Computer Science.")
    a.process(s, "I have a 6 month internship.")
    response = a.process(s, "No, I do not know Python.")
    assert s.status == "NOT_QUALIFIED"
    assert "requirement" in response.lower()

def test_human_escalation():
    a = make_agent()
    s = ScreeningSession()
    response = a.process(s, "I want to speak to a recruiter.")
    assert s.status == "HUMAN_ESCALATION"
    assert "human" in response.lower() or "recruiter" in response.lower()


def test_objection_is_answered_before_screening():
    from app.kb import KnowledgeBase
    from app.screening import ScreeningAgent, ScreeningSession
    kb = KnowledgeBase("data/processed/chunks.json")
    agent = ScreeningAgent(kb)
    s = ScreeningSession()
    agent.process(s, "Why do you need my degree information?")
    assert "preliminary qualification" in s.transcript[-1]["text"].lower()
    assert "recruiter" in s.transcript[-1]["text"].lower()
    assert "degree" not in s.answers

def test_conflicting_experience_is_not_stored():
    a = make_agent()
    s = ScreeningSession()
    # The first answer is intentionally unrelated to the degree question and contains
    # contradictory experience statements. The agent should ask for clarification and
    # must not store it as the candidate's degree.
    response = a.process(
        s,
        "I have 2 years of professional experience. Actually, I am a fresher and I have never worked professionally."
    )
    assert "inconsistent" in response.lower()
    assert "clarify" in response.lower()
    assert "degree" not in s.answers
    assert "experience" not in s.answers
    assert s.pending_clarification == "experience"
    follow_up = a.process(s, "I am a fresher with no professional work experience.")
    assert s.answers["experience"] == "I am a fresher with no professional work experience."
    assert "degree" in follow_up.lower()


def test_degree_question_rejects_cross_field_experience_answer():
    a = make_agent()
    s = ScreeningSession()
    response = a.process(s, "I have 2 years of professional experience.")
    assert "degree" in response.lower()
    assert "degree" not in s.answers
