__author__ = 'harishrohini'
from src.instructionstages.IF import IF
from src.instructionstages.ID import ID
from src.instructionstages.EX import EX
from src.instructionstages.MEM import MEM
from src.instructionstages.WB import WB


class Load:
    def __init__(self, inst):
        self.inst = inst
        self.IF = IF()
        self.ID = ID()
        self.EX = EX()
        self.MEM = MEM()
        self.WB = WB()
        self.execution_order = ['IF', 'ID', 'EX', 'MEM', 'WB']
        self.execution_status = {'IF': False, 'ID': False, 'EX': False, 'MEM': False, 'WB': False}
        print "in Load class : ", inst

    def next_execution_stage(self, clock, clock_execution_dict, instruction_index):
        print self.inst
        completed = False
        start_next_instruction = False
        next_stage = ''
        for i in self.execution_order:
            if self.execution_status[i] is False:
                self.execution_status[i] = True
                if i == 'WB':
                    completed = True
                if i == 'ID':
                    start_next_instruction = True
                next_stage = i
                break
        if clock in clock_execution_dict:
            clock_execution_dict[clock][instruction_index] = next_stage
        else:
            clock_execution_dict[clock] = {instruction_index: next_stage}
        return clock_execution_dict, completed, start_next_instruction

