import re


# High-risk escalation patterns
HIGH_RISK_PATTERNS = [
    r"developer mode",
    r"reveal.*policy",
    r"ignore.*instruction",
    r"bypass.*safety",
    r"system prompt",
    r"jailbreak"
]

RISK_THRESHOLD = 0.6


def detect_escalation(text: str) -> bool:
    text = text.lower()
    for pattern in HIGH_RISK_PATTERNS:
        if re.search(pattern, text):
            return True
    return False


def decide(risk_score: float, prompt: str) -> str:
    # Deterministic override
    if detect_escalation(prompt):
        risk_score += 0.7

    risk_score = min(risk_score, 1.0)

    if risk_score >= RISK_THRESHOLD:
        return "TERMINATE"

    return "ALLOW"