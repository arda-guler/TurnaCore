from consts import *

def compile_program(input_file, output_file="output.cis"):
    infile = open(input_file, "r")
    inlines = [line.rstrip() for line in infile.readlines() if ((not line.startswith(';')) and (not line == '\n'))]

    inlines_sanitized = []
    for element in inlines:
        if ' ' in element:
            split_elements = element.split(' ')
            inlines_sanitized.extend(split_elements)
        else:
            inlines_sanitized.append(element)

    labels = {}
    statement_pos = 1
    for line in inlines_sanitized:
        if line.endswith(":"):
            labels[line[0:-1].lower()] = str(statement_pos)
        elif line.startswith("#"):
            pass
        else:
            statement_pos += 1

    consts = {}
    for line in inlines_sanitized:
        if line.lower().startswith("#"):
            lsplit = line[1:].split("=")
            consts[lsplit[0].lower()] = str(lsplit[1])

    print(consts)
    
    outlines = []
    for line in inlines_sanitized:
        if line.startswith("#"):
            pass
        elif line.lower() in labels:
            outlines.append(labels[line.lower()])
        elif line.lower() in consts:
            outlines.append(consts[line.lower()])
        elif line.lower() == "add":
            outlines.append(str(int(cpu_add)))
        elif line.lower() == "sub":
            outlines.append(str(int(cpu_sub)))
        elif line.lower() == "mr1":
            outlines.append(str(int(cpu_mod_reg1)))
        elif line.lower() == "mr2":
            outlines.append(str(int(cpu_mod_reg2)))
        elif line.lower() == "jmp":
            outlines.append(str(int(cpu_jmp)))
        elif line.lower() == "jg":
            outlines.append(str(int(cpu_jg)))
        elif line.lower() == "jl":
            outlines.append(str(int(cpu_jl)))
        elif line.lower() == "je":
            outlines.append(str(int(cpu_je)))
        elif line.lower() == "write":
            outlines.append(str(int(cpu_write)))
        elif line.lower() == "recall":
            outlines.append(str(int(cpu_recall)))
        elif line.lower() == "memw":
            outlines.append(str(int(cpu_memwrite)))
        elif line.lower() == "memr":
            outlines.append(str(int(cpu_memread)))
        elif line.lower() == "halt":
            outlines.append(str(int(cpu_halt)))
        elif line.lower() == "null":
            outlines.append("0")
        elif line.endswith(":"):
            pass
        else:
            outlines.append(line)

    infile.close()
    outfile = open(output_file, "w+")
    for line in outlines:
        outfile.write(line)
        outfile.write("\n")

    outfile.close()
