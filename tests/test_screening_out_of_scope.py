from pathlib import Path
from app.kb import KnowledgeBase
from app.screening import ScreeningAgent, ScreeningSession

ROOT = Path(__file__).resolve().parents[1]


def make_agent():
    return ScreeningAgent(KnowledgeBase(str(ROOT / "data" / "processed" / "chunks.json")))


def test_out_of_scope_question_does_not_become_degree():
    agent = make_agent()
    session = ScreeningSession()
    response = agent.process(session, "What is the company's current stock price?")
    assert "don't have that information" in response.lower()
    assert "stock price" not in session.answers.get("degree", "").lower()
    assert session.status == "IN_PROGRESS"


def test_salary_question_is_grounded_and_not_stored():
    agent = make_agent()
    session = ScreeningSession()
    response = agent.process(session, "What salary will I receive?")
    assert "salary" in response.lower()
    assert "source:" in response.lower()
    assert "degree" not in session.answers
