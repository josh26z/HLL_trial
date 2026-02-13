import hashlib
import math


class HyperLogLog:
    def __init__(self, p=10):
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m

    def _hash(self, value):
        h = hashlib.sha256(value.encode()).digest()
        return int.from_bytes(h[:8], 'big')  # 64-bit hash

    def add(self, value):
        x = self._hash(value)

        idx = x & (self.m - 1)
        w = x >> self.p

        rank = self._rho(w)
        self.registers[idx] = max(self.registers[idx], rank)

    def _rho(self, w):
        if w == 0:
            return 64 - self.p + 1
        return (64 - self.p) - w.bit_length() + 1

    def estimate(self):
        alpha = 0.7213 / (1 + 1.079 / self.m)

        Z = sum(2.0 ** -r for r in self.registers)
        E = alpha * self.m * self.m / Z

        # Small range correction
        V = self.registers.count(0)

        if E <= 2.5 * self.m:
            if V != 0:
                E = self.m * math.log(self.m / V)

        return E