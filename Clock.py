__author__ = 'harishrohini'
from Memory import Memory
from Registers import Registers
from Instructions import Instructions


class Clock:
    def __init__(self, instructions):
        #self.memory = memory
        #self.registers = registers
        self.instructions = instructions
        self.clock_execution_dict = {}
        self.clock = 0

    def print_object_ids(self):
        print id(self.memory), id(self.registers), id(self.instructions)

    def increment_clock(self):
        self.clock += 1

    def next_instruction(self):
        while self.complete():
            if self.clock == 0:
                self.increment_clock()
                self.clock_execution_dict = self.instructions.execute_next_instruction(self.clock, self.clock_execution_dict)
            else:
                self.increment_clock()
                self.clock_execution_dict = self.instructions.execute_next_instruction(self.clock, self.clock_execution_dict)


    def complete(self):
        return self.instructions.check_execution_complete()