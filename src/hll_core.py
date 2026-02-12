import math
import hashlib
import numpy as np


class HyperLogLog:
    def __init__(self, p=10):
        self.p = p
        self.m = 1 << p
        self.registers = np.zeros(self.m)

    def _hash(self, value: str) -> int:
        return int(hashlib.sha256(value.encode()).hexdigest(), 16)

    def add(self, value: str):
        x = self._hash(value)
        idx = x & (self.m - 1)
        w = x >> self.p
        rank = self._rho(w)
        self.registers[idx] = max(self.registers[idx], rank)

    def _rho(self, w):
        return (w.bit_length() - w.to_bytes((w.bit_length() + 7) // 8, 'big').find(b'\x01') * 8 + 1) if w != 0 else 1

    def estimate(self):
        alpha = 0.7213 / (1 + 1.079 / self.m)
        Z = 1.0 / np.sum(2.0 ** -self.registers)
        E = alpha * self.m ** 2 * Z
        return E

    def merge(self, other):
        self.registers = np.maximum(self.registers, other.registers)
