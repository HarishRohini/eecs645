__author__ = 'harishrohini'
from src.Registers import Registers


class MEM:
    def __init__(self, inst):
        self.inst = inst

    def execute_stage(self):
        register = self.inst.replace(",", "").split()
        if register[0] == 'L.D':
            Registers.f[register[1]]['used'] = False
        else:
            Registers.f[register[1]]['used'] = False
            Registers.f[register[1]]['is_store'] = False