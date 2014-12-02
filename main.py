__author__ = 'harishrohini'
import sys
import os
#print os.getcwd()
#sys.path.append(os.getcwd()+'')
#sys.path.append('/Users/harishrohini/PycharmProjects/EECS645/')
from optparse import OptionParser
from src.ReadContents import ReadContents
from src.Instructions import Instructions
from src.Writer import Writer
from src.Registers import Registers
from src.Memory import Memory
from Clock import Clock


def start_execution(options):
    f = open(options.file, 'r')
    content = f.read()
    read_content = ReadContents()
    instructions = Instructions()
    #print "Id 2 :", id(instructions)
    registers = Registers()
    memory = Memory()
    read_content.read_iregisters(content)
    read_content.read_fpregisters(content)
    read_content.read_memory(content)
    read_content.get_instructions(content)
    #instructions, registers, memory = read_content.return_attrs()
    instructions = read_content.return_attrs()
    #print "registers: ", id(registers), " Inst : ", id(instructions.registers), id(memory), id(instructions.memory)
    #print instructions.get_instructions(), '\n', registers.r['R2'], '\n', memory.location, '\n', registers.f
    instructions.build_instruction_objects()
    #print instructions.instructions_object_list
    #print "In main file : ", id(memory), id(registers), id(instructions)
    clock = Clock(instructions)
    #clock.print_object_ids()
    #print clock.start_clock()
    #print clock.clock
    clock.next_instruction()
    #print "log : ", Registers.f['F4']['contents']
    writer = Writer(clock.clock_execution_dict, Registers.f, len(instructions.instructions_object_list))
    writer.write_to_file()
    writer.write_to_file_registers()
    #clock.next_instruction()
    #instructions = Instructions()
    #instructions.parse(f.read())
    #print instructions.get_instructions()


def main():
    usage = "usage: python main.py -f filename"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", action="store", type="string", help="filename")

    (options, args) = parser.parse_args()

    if not options.file:
        sys.stderr.write("Specify an input file\n")
        sys.stderr.write("Type python main.py --help' for usage.\n")
        sys.exit()
    else:
        start_execution(options)




if __name__ == '__main__':
    main()