from src.hll_core import HyperLogLog


class MonitoringEngine:
    def __init__(self, hll_manager):
        self.hll_manager = hll_manager

    def process(self, user_id, structural_features, role_features):

        # Per-prompt structural HLL
        temp_structural = HyperLogLog()
        for f in structural_features:
            temp_structural.add(f)
        structural_card = temp_structural.estimate()

        # Per-prompt role HLL
        temp_role = HyperLogLog()
        for f in role_features:
            temp_role.add(f)
        role_card = temp_role.estimate()

        # Session HLL (cumulative but growth-based)
        session_hll = self.hll_manager.get_session_hll(user_id)
        previous_session = session_hll.estimate()

        for f in structural_features:
            session_hll.add(f)

        new_session = session_hll.estimate()
        session_growth = new_session - previous_session

        return {
            "structural_card": structural_card,
            "role_card": role_card,
            "session_growth": session_growth,
        }