from src.hll_core import HyperLogLog


class HLLManager:
    def __init__(self):
        self.session_hll = {}

    def get_session_hll(self, user_id):
        if user_id not in self.session_hll:
            self.session_hll[user_id] = HyperLogLog()
        return self.session_hll[user_id]