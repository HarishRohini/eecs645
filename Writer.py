__author__ = 'harishrohini'


class Writer:
    def __init__(self, clock_execution_dict, registers, inst_length):
        self.clock_execution_dict = clock_execution_dict
        self.registers = registers
        self.inst_length = inst_length

    def write_to_file(self):
        timing_file = raw_input("\n Enter Timing File name : ")
        f = open(timing_file, 'w')
        #f.write(' '*6)
        f.write("\t")
        for i in range(1, self.inst_length+1):
            if i < 10:
                f.write("I#"+str(i))
            else:
                f.write("I#"+str(i))
            f.write("\t")
        f.write("\n")
        for index in self.clock_execution_dict:
            if index < 10:
                f.write("C#"+str(index)+" ")
            else:
                f.write("C#"+str(index))
            f.write(" ")
            for i in range(0, self.inst_length):
                if i in self.clock_execution_dict[index]:
                    if len(self.clock_execution_dict[index][i]) < 3:
                        f.write(self.clock_execution_dict[index][i]+" ")
                    else:
                        f.write(self.clock_execution_dict[index][i])
                else:
                    f.write("   ")
                f.write(" ")
            f.write("\n")
        f.close()

    def write_to_file_registers(self):
        register_file = raw_input("Enter register file : ")
        f = open(register_file, 'w')
        for i in self.registers:
            if self.registers[i]['contents'] != 0:
                f.write(i + '\t' + str(self.registers[i]['contents']) + '\n')
        f.close()