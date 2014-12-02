__author__ = 'harishrohini'
from src.instructionstages.IF import IF
from src.instructionstages.ID import ID
from src.instructionstages.A1 import A1
from src.instructionstages.A2 import A2
from src.instructionstages.A3 import A3
from src.instructionstages.A4 import A4
from src.instructionstages.MEM import MEM
from src.instructionstages.WB import WB


class Sub:
    def __init__(self, inst):
        self.inst = inst
        self.IF = IF()
        self.ID = ID(self.inst)
        self.A1 = A1()
        self.A2 = A2()
        self.A3 = A3(self.inst)
        self.A4 = A4(self.inst)
        self.MEM = MEM(self.inst)
        self.WB = WB(self.inst)
        self.execution_order = ['IF', 'ID', 'A1', 'A2', 'A3', 'A4', 'MEM', 'WB']
        self.execution_status = {'IF': False, 'ID': False, 'A1': False, 'A2': False, 'A3': False,
                                 'A4': False, 'MEM': False, 'WB': False}
        #print "In Multiply class : ", inst

    def next_execution_stage(self, clock, clock_execution_dict, instruction_index):
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
                elif i == 'A1':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'A2':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'A3':
                    self.execution_status[i] = True
                    self.A3.execute_stage()
                    next_stage = i
                elif i == 'A4':
                    self.execution_status[i] = True
                    self.A4.execute_stage()
                    self.A4.execute()
                    next_stage = i
                elif i == 'MEM':
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

if __name__ == '__main__':
    ad = Sub()
