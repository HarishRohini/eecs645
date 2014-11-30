__author__ = 'harishrohini'
from src.Registers import Registers


class WB:
    def __init__(self, inst):
        self.inst = inst

    def execute_writeback(self):
        #print "In WB stage : ", self.inst
        register = self.inst.split()[1].split(',')[0]
        if register[0] == 'F':
            Registers.f[register]['used'] = False
        else:
            Registers.r[register]['used'] = False