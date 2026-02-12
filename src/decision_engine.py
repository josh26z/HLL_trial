def decide(risk_score):
    if risk_score < 10:
        return "ALLOW"
    elif risk_score < 30:
        return "SANITIZE"
    elif risk_score < 60:
        return "BLOCK"
    else:
        return "TERMINATE"
