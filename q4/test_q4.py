from engine import NudgeEngine


def names(events):
    return {e.signal for e in events}


def test_required_signals():
    e = NudgeEngine(cooldown_seconds=5)
    assert "missed_cross_sell" in names(e.process("The customer has a second vehicle."))
    assert "rising_frustration" in names(e.process("This is ridiculous, I am fed up."))
    assert "payment_difficulty" in names(e.process("I can't pay this month."))
    assert "compliance_risk" in names(e.process("We need the required disclosure."))


def test_duplicate_suppression():
    e = NudgeEngine(cooldown_seconds=10)
    first = e.process("I can't pay this month.", now=100)
    second = e.process("I can't pay this month.", now=105)
    third = e.process("I can't pay this month.", now=111)
    assert len(first) == 1
    assert len(second) == 0
    assert len(third) == 1


def test_low_confidence_threshold_is_respected():
    e = NudgeEngine(threshold=.95)
    assert e.process("I can't pay this month.") == []
