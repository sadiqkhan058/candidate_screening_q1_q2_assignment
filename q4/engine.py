from __future__ import annotations
from dataclasses import dataclass, asdict
import re
import time
from typing import Iterable


@dataclass
class Signal:
    name: str
    confidence: float
    evidence: str
    nudge: str
    topic: str


@dataclass
class NudgeEvent:
    timestamp: float
    signal: str
    confidence: float
    evidence: str
    nudge: str


class NudgeEngine:
    """Small deterministic signal/nudge engine for a real-time demo."""

    def __init__(self, threshold: float = 0.72, cooldown_seconds: float = 8.0):
        self.threshold = threshold
        self.cooldown_seconds = cooldown_seconds
        self.last_emitted: dict[str, float] = {}

    def detect(self, text: str) -> list[Signal]:
        t = text.lower()
        out: list[Signal] = []

        if any(x in t for x in ["second vehicle", "another vehicle", "two cars", "another car"]):
            out.append(Signal("missed_cross_sell", .91, text, "Customer mentioned another vehicle. Suggest the multi-vehicle offer.", "sales"))

        if any(x in t for x in ["disclosure", "terms and conditions", "required disclosure", "important information"]):
            out.append(Signal("compliance_risk", .88, text, "Required disclosure may be missing. Remind the agent before proceeding.", "compliance"))

        frustration = ["frustrated", "this is ridiculous", "angry", "upset", "already told you", "can't believe", "fed up"]
        if any(x in t for x in frustration):
            out.append(Signal("rising_frustration", .86, text, "Acknowledge the customer's concern before continuing.", "sentiment"))

        if any(x in t for x in ["can't pay", "cannot pay", "payment is difficult", "struggling to pay", "payment problem", "can't afford"]):
            out.append(Signal("payment_difficulty", .90, text, "Offer an approved payment-support or callback path.", "collections"))

        return out

    def emit(self, signals: Iterable[Signal], now: float | None = None) -> list[NudgeEvent]:
        now = time.time() if now is None else now
        events = []
        for s in signals:
            if s.confidence < self.threshold:
                continue
            last = self.last_emitted.get(s.name)
            if last is not None and now - last < self.cooldown_seconds:
                continue
            self.last_emitted[s.name] = now
            events.append(NudgeEvent(now, s.name, s.confidence, s.evidence, s.nudge))
        return events

    def process(self, text: str, now: float | None = None) -> list[NudgeEvent]:
        return self.emit(self.detect(text), now)


if __name__ == "__main__":
    engine = NudgeEngine()
    for line in [
        "The customer says they also have a second vehicle.",
        "This is ridiculous, I have already told you twice.",
        "I can't pay the installment this month.",
        "We still need to cover the required disclosure.",
    ]:
        for event in engine.process(line):
            print(asdict(event))
