__author__ = 'harishrohini'
from Instructions import Instructions
from Registers import Registers
from Memory import Memory


class ReadContents:
    def __init__(self):
        self.instructions = Instructions()
        self.registers = Registers()
        self.memory = Memory()

    def read_iregisters(self, data):
        registers_data = data[data.find('I-REGISTERS')+len('I-REGISTERS')+1:data.find('FP-REGISTERS')].splitlines()
        #print registers_data
        for index in registers_data:
            regs = index.split()
            #print regs
            self.registers.r[regs[0]]['contents'] = regs[1]
        #print self.registers.r

    def read_fpregisters(self, data):
        registers_data = data[data.find('FP-REGISTERS')+len('FP-REGISTERS')+1:data.find('MEMORY')].splitlines()
        for index in registers_data:
            regs = index.split()
            #print regs
            self.registers.f[regs[0]]['contents'] = regs[1]
        #print self.registers.f

    def read_memory(self, data):
        memory_data = data[data.find('MEMORY')+len('MEMORY')+1:data.find('CODE')].splitlines()
        #print "em", memory_data
        for index in memory_data:
            regs = index.split()
            #print regs
            self.memory.location[regs[0]] = regs[1]
        #print self.memory.location

    def get_instructions(self, data):
        start = data.find('CODE')
        code = data[start+5:]
        self.instructions.instructions = code.splitlines()
        self.instructions.memory = self.memory
        self.instructions.registers = self.registers
        #print self.instructions

    def return_attrs(self):
        #print "id : ", id(self.instructions)
        return self.instructions, self.registers, self.memory

if __name__ == '__main__':
    a = ReadContents()
    f = open('input.txt', 'r')
    contents = f.read()
    a.read_iregisters(contents)
    a.read_fpregisters(contents)
    a.read_memory(contents)