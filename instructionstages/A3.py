__author__ = 'harishrohini'
from src.Registers import Registers

class A3:
    def __init__(self, inst):
        self.inst = inst

    def execute_stage(self):
        register = self.inst.replace(",", "").split()[1]
        Registers.f[register]['is_mul'] = True