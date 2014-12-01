__author__ = 'harishrohini'
from src.Registers import Registers

class A4:
    def __init__(self, inst):
        self.inst = inst

    def execute_stage(self):
        register = self.inst.replace(",", "").split()[1]
        Registers.f[register]['is_add'] = False
        Registers.f[register]['used'] = False