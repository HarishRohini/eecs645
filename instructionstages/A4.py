__author__ = 'harishrohini'
from src.Registers import Registers

class A4:
    def __init__(self, inst):
        self.inst = inst

    def execute_stage(self):
        register = self.inst.replace(",", "").split()[1]
        Registers.f[register]['is_add'] = False
        Registers.f[register]['used'] = False

    def execute(self):
        instruction = self.inst.replace(",", "").split()
        #print instruction
        if instruction[0] == 'ADD.D':
            Registers.f[instruction[1]]['contents'] = str(float(Registers.f[instruction[2]]['contents']) + float(Registers.f[instruction[3]]['contents']))
            #print Registers.f[instruction[1]]['contents']
        else:
            Registers.f[instruction[1]]['contents'] = str(float(Registers.f[instruction[2]]['contents']) - float(Registers.f[instruction[3]]['contents']))
            #print Registers.f[instruction[1]]['contents']