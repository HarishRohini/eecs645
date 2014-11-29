__author__ = 'harishrohini'
from src.instructiontypes.Load import Load
from src.Memory import Memory
from src.Registers import Registers


class Instructions:
    def __init__(self):
        self.instructions = []
        self.instructions_object_list = []
        self.memory = Memory()
        self.registers = Registers()
        self.completed_instructions = []
        self.instructions_queue = [0]

    def parse(self, data):
        start = data.find('CODE')
        code = data[start+5:]
        self.instructions = code.splitlines()

    def get_instructions(self):
        return self.instructions

    def build_instruction_objects(self):
        for instruction in self.instructions:
            operation_type = instruction.split()
            if operation_type[0] == 'L.D':
                instruction_object = Load(instruction)
                self.instructions_object_list.append(instruction_object)
                #print "load : ", test.test(instruction)
            elif operation_type[0] == 'MUL.D':
                print "Mul  : ", instruction
            elif operation_type[0] == 'S.D':
                print "Store: ", instruction
            elif operation_type[0] == 'ADD.D':
                print "Add  : ", instruction
            else:
                print "Other"
        print self.instructions_object_list
            #self.instructions_object_list.append(instruction_object)

    def next_instruction(self):
        pass

    def execute_next_instruction(self, clock, clock_execution_dict):
        print "Instruction queue : ", self.instructions_queue, "clock cycle : ", clock
        for index in self.instructions_queue:
            if index not in self.completed_instructions:
                print "index : ", index, "completed inst : ",self.completed_instructions
                clock_execution_dict, completed, start_next_instruction = self.instructions_object_list[index].next_execution_stage(clock, clock_execution_dict, index)
                print "clock_execution_dict", clock_execution_dict, "completed : ", completed
                if completed:
                    #self.instructions_queue.remove(index)
                    self.completed_instructions.append(index)
                if start_next_instruction:
                    if index < len(self.instructions_object_list) - 1:
                        self.instructions_queue.append(index+1)
        return clock_execution_dict

    def execute_first_instruction(self, clock, clock_execution_dict):
        print self.instructions_object_list[0].next_execution_stage(clock, clock_execution_dict)
        #pass

    def check_execution_complete(self):
        if len(self.completed_instructions) == len(self.instructions_object_list):
            return False
        else:
            return True



if __name__ == '__main__':
    i = Instructions()
    f = open('input.txt', 'r')
    contents = f.read()
    i.parse(contents)
    i.build_instruction_objects()
