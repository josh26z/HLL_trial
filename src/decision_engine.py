import re

# Termination threshold
RISK_THRESHOLD = 0.5


# High-risk escalation patterns
HIGH_RISK_PATTERNS = [
    r"developer\s*mode",
    r"admin\s*(mode|access|control)",
    r"reveal.*policy",
    r"ignore.*policy",
    r"ignore.*instruction",
    r"bypass.*safety",
    r"bypass.*filter",
    r"override.*system",
    r"system\s*prompt",
    r"jailbreak",
    r"act\s*as\s*system"
]


def detect_escalation(text: str) -> bool:
    text = text.lower()

    for pattern in HIGH_RISK_PATTERNS:
        if re.search(pattern, text):
            return True

    return False


def decide(risk_score: float, prompt: str) -> str:

    # Detect explicit escalation attempts
    if detect_escalation(prompt):
        print("[ESCALATION DETECTED]")
        risk_score += 0.9

    # Clamp risk score
    risk_score = min(risk_score, 1.0)

    # Decision
    if risk_score >= RISK_THRESHOLD:
        return "TERMINATE"

    return "ALLOW"
