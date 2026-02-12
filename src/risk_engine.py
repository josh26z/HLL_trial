def compute_risk(signals):
    structural_score = signals["structural_delta"]
    role_score = signals["role_delta"] * 1.5
    session_score = signals["session_delta"]

    unified_risk = structural_score + role_score + session_score

    return unified_risk
