__author__ = 'harishrohini'
from src.Registers import Registers
from src.Memory import Memory


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

    def execute(self):
        instruction = self.inst.replace(",", "").split()
        if instruction[0] == 'L.D':
            inst = instruction[2].split("(")
            offset = inst[0]
            r_register = inst[1][:-1]
            l_register = instruction[1]
            Registers.f[l_register]['contents'] = Memory.location[str(int(Registers.r[r_register]['contents']) + int(offset))]
            #print Registers.f[l_register]['contents']
            #print result
        else:
            inst = instruction[1].split("(")
            offset = inst[0]
            l_register = inst[1][:-1]
            r_register = instruction[2]
            Memory.location[str(int(Registers.r[l_register]['contents']) + int(offset))] = Registers.f[r_register]['contents']

            #print Memory.location['16']
