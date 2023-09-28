import sys
import time
import tkinter as tk
import os

from binary import *
from CPU import *
from memory import *
from consts import *

def init_CPU():
    cpu_instructions = {"add": cpu_add,
                        "sub": cpu_sub,
                        "mod_reg1": cpu_mod_reg1,
                        "mod_reg2": cpu_mod_reg2,
                        "jmp": cpu_jmp,
                        "jg": cpu_jg,
                        "jl": cpu_jl,
                        "je": cpu_je,
                        "write": cpu_write,
                        "recall": cpu_recall,
                        "memwrite": cpu_memwrite,
                        "memread": cpu_memread,
                        "halt": cpu_halt}

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
    if len(sys_args) == 2:
        program_file = sys_args[1]
        slow = "y"
    elif len(sys_args) == 3:
        program_file = sys_args[1]
        slow = bool(sys_args[2])
    else:
        print("Programs on disk:")
        progfiles = []
        for f in os.listdir("../programs"):
            if f.endswith(".ao"):
                print(f)
                progfiles.append(f)
        print("\n")
                
        program_file = input("Enter the filename of the program you wish to run: ")
        slow = input("Slow mode (Y/n): ")

    if slow.lower() == "n":
        slow = False
    else:
        slow = True

    program_file = "../programs/" + program_file
    if not program_file.endswith(".ao") or not program_file.endswith(".cis"):
        program_file = program_file + ".ao"

    print("Initializing CPU...")
    cpu = init_CPU()

    mem = Memory(program_file)
    print("Loaded program into memory.")
    print(mem)

    window = tk.Tk()
    window.title("TurnaCore")
    window.iconphoto(False, tk.PhotoImage(file="../icon/tc_icon.png"))
    canvas = tk.Canvas(window, height=480, width=640, bg="black")
    canvas.pack()

    print("Running...")
    while int(cpu.registers[3].get_value()) < mem.size and cpu.run:
        cpu.step(mem)
        # print(cpu)

        if slow:
            # draw memory
            canvas.create_rectangle(360, 10, 620, 470, fill="green")
            mempos = cpu.registers[3].get_value()
            canvas.create_text(380, 24, text="Mem. Loc.: " + str(mempos), anchor="w", fill="white", font=('Arial', 12))
            canvas.create_rectangle(370, 40, 610, 42, fill="black")
            canvas.create_rectangle(370, 225, 610, 255, fill="red")

            for i in range(1, 7):
                if int(mempos) - i > 0:
                    if mem.data[int(mempos) - i] == cpu_add:
                        mtext = str(mem.data[int(mempos) - i]) + " (ADD)"
                    elif mem.data[int(mempos) - i] == cpu_sub:
                        mtext = str(mem.data[int(mempos) - i]) + " (SUB)"
                    elif mem.data[int(mempos) - i] == cpu_mod_reg1:
                        mtext = str(mem.data[int(mempos) - i]) + " (MR1)"
                    elif mem.data[int(mempos) - i] == cpu_mod_reg2:
                        mtext = str(mem.data[int(mempos) - i]) + " (MR2)"
                    elif mem.data[int(mempos) - i] == cpu_jmp:
                        mtext = str(mem.data[int(mempos) - i]) + " (JMP)"
                    elif mem.data[int(mempos) - i] == cpu_jg:
                        mtext = str(mem.data[int(mempos) - i]) + " (JG)"
                    elif mem.data[int(mempos) - i] == cpu_jl:
                        mtext = str(mem.data[int(mempos) - i]) + " (JL)"
                    elif mem.data[int(mempos) - i] == cpu_je:
                        mtext = str(mem.data[int(mempos) - i]) + " (JE)"
                    elif mem.data[int(mempos) - i] == cpu_write:
                        mtext = str(mem.data[int(mempos) - i]) + " (WRITE)"
                    elif mem.data[int(mempos) - i] == cpu_recall:
                        mtext = str(mem.data[int(mempos) - i]) + " (RECALL)"
                    elif mem.data[int(mempos) - i] == cpu_memwrite:
                        mtext = str(mem.data[int(mempos) - i]) + " (MEMW)"
                    elif mem.data[int(mempos) - i] == cpu_memread:
                        mtext = str(mem.data[int(mempos) - i]) + " (MEMR)"
                    elif mem.data[int(mempos) - i] == cpu_halt:
                        mtext = str(mem.data[int(mempos) - i]) + " (HALT)"
                    else:
                        mtext = str(mem.data[int(mempos) - i]) + " (" + str(int(mem.data[int(mempos) - i])) + ")"
                else:
                    mtext = ""
                    
                y_margin = 30
                pos_x = 380
                pos_y = 240 - i * y_margin
                canvas.create_text(pos_x, pos_y, text=mtext, fill="white", font=('Arial', 12), anchor="w")

            for i in range(8):
                if int(mempos) + i < mem.size:
                    if mem.data[int(mempos) + i] == cpu_add:
                        mtext = str(mem.data[int(mempos) + i]) + " (ADD)"
                    elif mem.data[int(mempos) + i] == cpu_sub:
                        mtext = str(mem.data[int(mempos) + i]) + " (SUB)"
                    elif mem.data[int(mempos) + i] == cpu_mod_reg1:
                        mtext = str(mem.data[int(mempos) + i]) + " (MR1)"
                    elif mem.data[int(mempos) + i] == cpu_mod_reg2:
                        mtext = str(mem.data[int(mempos) + i]) + " (MR2)"
                    elif mem.data[int(mempos) + i] == cpu_jmp:
                        mtext = str(mem.data[int(mempos) + i]) + " (JMP)"
                    elif mem.data[int(mempos) + i] == cpu_jg:
                        mtext = str(mem.data[int(mempos) + i]) + " (JG)"
                    elif mem.data[int(mempos) + i] == cpu_jl:
                        mtext = str(mem.data[int(mempos) + i]) + " (JL)"
                    elif mem.data[int(mempos) + i] == cpu_je:
                        mtext = str(mem.data[int(mempos) + i]) + " (JE)"
                    elif mem.data[int(mempos) + i] == cpu_write:
                        mtext = str(mem.data[int(mempos) + i]) + " (WRITE)"
                    elif mem.data[int(mempos) + i] == cpu_recall:
                        mtext = str(mem.data[int(mempos) + i]) + " (RECALL)"
                    elif mem.data[int(mempos) + i] == cpu_memwrite:
                        mtext = str(mem.data[int(mempos) + i]) + " (MEMW)"
                    elif mem.data[int(mempos) + i] == cpu_memread:
                        mtext = str(mem.data[int(mempos) + i]) + " (MEMR)"
                    elif mem.data[int(mempos) + i] == cpu_halt:
                        mtext = str(mem.data[int(mempos) + i]) + " (HALT)"
                    else:
                        mtext = str(mem.data[int(mempos) + i]) + " (" + str(int(mem.data[int(mempos) + i])) + ")"
                else:
                    mtext = ""
                    
                y_margin = 30
                pos_x = 380
                pos_y = 240 + i * y_margin
                canvas.create_text(pos_x, pos_y, text=mtext, fill="white", font=('Arial', 12), anchor="w")

            # draw cpu
            canvas.create_rectangle(10, 10, 350, 470, fill="blue")
            canvas.create_rectangle(10, 135, 350, 165, fill="cyan")
            
            for i in range(5):
                canvas.create_text(20, 30 + i * 30, text="Register" + str(i+1) + ": " + str(cpu.registers[i].get_value()) + " (" + str(int(cpu.registers[i].get_value())) + ")", anchor="w", font=('Arial', 12))
            
            window.update()
            time.sleep(0.1)

            if int(cpu.registers[3].get_value()) < mem.size and cpu.run:
                canvas.delete("all") 

    print("Done!\n")
    print(cpu)
    print(mem)

main()
