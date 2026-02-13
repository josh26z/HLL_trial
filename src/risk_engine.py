def compute_risk(signals):

    structural_score = signals["structural_card"] / 50
    role_score = signals["role_card"] * 2
    session_score = signals["session_growth"] / 20

    risk = structural_score + role_score + session_score

    # Normalize to 0-1 range
    risk = min(risk / 10, 1.0)

    return risk