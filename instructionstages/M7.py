__author__ = 'harishrohini'
from src.Registers import Registers


class M7:
    def __init__(self, inst):
        self.inst = inst

    def execute_stage(self):
        register = self.inst.replace(",", "").split()[1]
        Registers.f[register]['is_mul'] = False
        Registers.f[register]['used'] = False

    def execute(self):
        instruction = self.inst.replace(",", "").split()
        print instruction
        Registers.f[instruction[1]]['contents'] = str(float(Registers.f[instruction[2]]['contents']) * float(Registers.f[instruction[3]]['contents']))
        print Registers.f[instruction[1]]['contents']
