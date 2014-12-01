__author__ = 'harishrohini'
from src.Registers import Registers


class ID:
    def __init__(self, inst):
        self.inst = inst

    def decode_instruction(self):
        print "In decode stage : ", self.inst
        execution_status = False
        #register = self.inst.split()[1].split(',')[0]
        instruction = self.inst.split()
        if instruction[0] in ['L.D', 'S.D']:
            if instruction[0] == 'L.D':
                execution_status = True
                register = self.find_register()
                Registers.f[register]['used'] = True
                #Registers.f[register]['is_store'] = True
                #pass
            else:
                register = self.find_dependent_register()
                is_used, is_mul = self.find_dependency(register)
                if is_used is True:
                    if is_mul:
                        execution_status = True
                    else:
                        execution_status = False
                else:
                    execution_status = True
            """"
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
            """
        else:
            print "MUL ISNG"
            registers = self.find_registers()
            status = self.is_used(registers[1:])
            #is_mul_status = self.is_used_mul(registers)
            print registers
            if status:
                Registers.f[registers[0]]['used'] = True
                execution_status = True
            else:
                execution_status = False
            #pass
        return execution_status

    def find_register(self):
        instruction = self.inst.split()
        register = ''
        if instruction[0] == 'S.D':
            register = instruction[1][2:4]
        elif instruction[0] == 'L.D':
            register = instruction[1].split(',')[0]
        else:
            register = instruction[1][:-1]
        return register

    def find_registers(self):
        registers = self.inst.replace(",", "").split()[1:]
        return registers

    def is_used(self, registers):
        status = True
        for i in registers:
            if Registers.f[i]['used']:
                status = False
                break
        return status

    def is_used_mul(self, registers):
        status = True
        for i in registers:
            if Registers.f[i]['used']['is_mul']:
                status = False
                break
        return status

    def find_dependent_register(self):
        return self.inst.replace(",", "").split()[2]

    def find_dependency(self, register):
        return Registers.f[register]['used'], Registers.f[register]['is_mul']
