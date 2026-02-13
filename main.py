print("CLEAN VERSION RUNNING")

from src.preprocessing import canonicalize
from src.feature_extraction import extract_structural_features, extract_role_features
from src.hll_manager import HLLManager
from src.monitoring import MonitoringEngine
from src.risk_engine import compute_risk
from src.decision_engine import decide


def main():
    hll_manager = HLLManager()
    monitor = MonitoringEngine(hll_manager)

    user_id = "user_1"

    while True:
        prompt = input("Enter prompt: ")

        clean_text = canonicalize(prompt)

        structural_features = extract_structural_features(clean_text)
        role_features = extract_role_features(clean_text)

        signals = monitor.process(user_id, structural_features, role_features)

        risk_score = compute_risk(signals)

        decision = decide(risk_score,prompt)

        print("\n--- DEBUG ---")
        print("Signals:", signals)
        print("Risk Score:", round(risk_score, 3))
        print("Decision:", decision)
        print("-------------\n")


if __name__ == "__main__":
    main()