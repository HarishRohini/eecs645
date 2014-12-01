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
        self.ID = ID(self.inst)
        self.EX = EX()
        self.MEM = MEM(self.inst)
        self.WB = WB(self.inst)
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
                if i == 'IF':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'ID':
                    if self.ID.decode_instruction():
                        next_stage = i
                        self.execution_status[i] = True
                        start_next_instruction = True
                    else:
                        next_stage = 's'
                    #start_next_instruction = True
                elif i == 'EX':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'MEM':
                    self.MEM.execute_stage()
                    self.execution_status[i] = True
                    next_stage = i
                else:
                    self.execution_status[i] = True
                    #self.WB.execute_writeback()
                    completed = True
                    next_stage = i
                break
        if clock in clock_execution_dict:
            clock_execution_dict[clock][instruction_index] = next_stage
        else:
            clock_execution_dict[clock] = {instruction_index: next_stage}
        return clock_execution_dict, completed, start_next_instruction

