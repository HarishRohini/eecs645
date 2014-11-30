__author__ = 'harishrohini'
from src.Registers import Registers


class ID:
    def __init__(self, inst):
        self.inst = inst

    def decode_instruction(self):
        #print "In decode stage : ", self.inst
        execution_status = False
        register = self.inst.split()[1].split(',')[0]
        if register[0] == 'F':
            if Registers.f[register]['used']:
                execution_status = False
            else:
                execution_status = True
                Registers.f[register]['used'] = True
        else:
            if Registers.r[register]['used']:
                execution_status = False
            else:
                execution_status = True
                Registers.r[register]['used'] = True
        return execution_status
