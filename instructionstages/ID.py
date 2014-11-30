__author__ = 'harishrohini'
from src.Registers import Registers


class ID:
    def __init__(self, inst):
        self.inst = inst

    def decode_instruction(self):
        #print "In decode stage : ", self.inst
        execution_status = False
        #register = self.inst.split()[1].split(',')[0]
        register = self.find_register()
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

    def find_register(self):
        instruction = self.inst.split()
        register = ''
        if instruction[0] == 'S.D':
            register = instruction[1][2:4]
        else:
            register = instruction[1].split(',')[0]
        return register
