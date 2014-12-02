__author__ = 'harishrohini'
from src.instructionstages.IF import IF
from src.instructionstages.ID import ID
from src.instructionstages.M1 import M1
from src.instructionstages.M2 import M2
from src.instructionstages.M3 import M3
from src.instructionstages.M4 import M4
from src.instructionstages.M5 import M5
from src.instructionstages.M6 import M6
from src.instructionstages.M7 import M7
from src.instructionstages.MEM import MEM
from src.instructionstages.WB import WB


class Mul:
    def __init__(self, inst):
        self.inst = inst
        self.IF = IF()
        self.ID = ID(self.inst)
        self.M1 = M1()
        self.M2 = M2()
        self.M3 = M3()
        self.M4 = M4()
        self.M5 = M5()
        self.M6 = M6(self.inst)
        self.M7 = M7(self.inst)
        self.MEM = MEM(self.inst)
        self.WB = WB(self.inst)
        self.execution_order = ['IF', 'ID', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'MEM', 'WB']
        self.execution_status = {'IF': False, 'ID': False, 'M1': False, 'M2': False, 'M3': False,
                                 'M4': False, 'M5': False, 'M6': False, 'M7': False, 'MEM': False, 'WB': False}
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
                elif i == 'M1':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'M2':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'M3':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'M4':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'M5':
                    self.execution_status[i] = True
                    next_stage = i
                elif i == 'M6':
                    self.execution_status[i] = True
                    self.M6.execute_stage()
                    #self.WB.execute_writeback()
                    next_stage = i
                elif i == 'M7':
                    self.execution_status[i] = True
                    self.M7.execute_stage()
                    self.M7.execute()
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