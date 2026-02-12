class MonitoringEngine:
    def __init__(self, hll_manager):
        self.hll_manager = hll_manager

        self.structural_baseline = 0
        self.role_baseline = 0
        self.session_baseline = {}

    def process(self, user_id, structural_features, role_features):
        # Structural
        for f in structural_features:
            self.hll_manager.structural_hll.add(f)

        structural_card = self.hll_manager.structural_hll.estimate()
        structural_delta = structural_card - self.structural_baseline

        # Role
        for f in role_features:
            self.hll_manager.role_hll.add(f)

        role_card = self.hll_manager.role_hll.estimate()
        role_delta = role_card - self.role_baseline

        # Session
        session_hll = self.hll_manager.get_session_hll(user_id)

        for f in structural_features:
            session_hll.add(f)

        session_card = session_hll.estimate()
        session_delta = session_card - self.session_baseline.get(user_id, 0)

        return {
            "structural_delta": structural_delta,
            "role_delta": role_delta,
            "session_delta": session_delta,
        }
