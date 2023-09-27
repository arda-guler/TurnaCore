def compile_program(input_file, output_file="output.cis"):
    infile = open(input_file, "r")
    inlines = [line.rstrip() for line in infile.readlines() if not line.startswith(';')]

    inlines_sanitized = []
    for element in inlines:
        if ' ' in element:
            split_elements = element.split(' ')
            inlines_sanitized.extend(split_elements)
        else:
            inlines_sanitized.append(element)
    
    outlines = []
    for line in inlines_sanitized:
        if line.lower() == "add":
            outlines.append("255")
        elif line.lower() == "sub":
            outlines.append("254")
        elif line.lower() == "mr1":
            outlines.append("253")
        elif line.lower() == "mr2":
            outlines.append("252")
        elif line.lower() == "jmp":
            outlines.append("251")
        elif line.lower() == "jg":
            outlines.append("250")
        elif line.lower() == "jl":
            outlines.append("249")
        elif line.lower() == "je":
            outlines.append("248")
        elif line.lower() == "write":
            outlines.append("247")
        elif line.lower() == "recall":
            outlines.append("246")
        elif line.lower() == "null":
            outlines.append("0")
        else:
            outlines.append(line)

    infile.close()
    outfile = open(output_file, "w+")
    for line in outlines:
        outfile.write(line)
        outfile.write("\n")

    outfile.close()
