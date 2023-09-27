import sys

from binary import *
from CPU import *
from program import *

def init_CPU():
    NULL = Binary(0)
    
    cpu_add = Binary(255)
    cpu_sub = Binary(254)
    cpu_mod_reg1 = Binary(253)
    cpu_mod_reg2 = Binary(252)
    cpu_jmp = Binary(251)
    cpu_jg = Binary(250)
    cpu_jl = Binary(249)
    cpu_je = Binary(248)
    cpu_write = Binary(247)
    cpu_recall = Binary(246)

    cpu_instructions = {"add": cpu_add,
                        "sub": cpu_sub,
                        "mod_reg1": cpu_mod_reg1,
                        "mod_reg2": cpu_mod_reg2,
                        "jmp": cpu_jmp,
                        "jg": cpu_jg,
                        "jl": cpu_jl,
                        "je": cpu_je,
                        "write": cpu_write,
                        "recall": cpu_recall}

    reg1 = Register(NULL)
    reg2 = Register(NULL)
    reg3 = Register(NULL)
    reg4 = Register(NULL)
    reg5 = Register(NULL)

    registers = [reg1, reg2, reg3, reg4, reg5]
    
    cpu = CPU(cpu_instructions, registers)
    return cpu

def main():
    sys_args = sys.argv
    if len(sys_args) >= 2:
        program_file = sys_args[1]
    else:
        program_file = input("Program filename:")

    print("Initializing CPU...")
    cpu = init_CPU()

    prog = Program(program_file)
    print("Loaded program.")
    print(prog)

    print("Running...")
    while int(cpu.registers[3].get_value()) < prog.size:
        cpu.step(prog)
        print(cpu)

main()
