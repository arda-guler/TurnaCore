from binary import *
from compiler import *

class Program:
    def __init__(self, file):
        self.file = file
        self.data = []
        self.size = 0

        # compile the program into a CIS before loading
        # if it is an AO file
        if file.endswith(".ao"):
            print("Compiling", file, "...")
            compile_program(file, file[0:-3] + ".cis")
            print("Compilation complete.")
        self.file = file[0:-3] + ".cis"
        
        self.load()

    def __repr__(self):
        output = "\nPROGRAM:\n"
        output += "--------\n"
        for idx, i in enumerate(self.data):
            output += str(idx) + ": " + str(i) + "\n"

        return output

    def load(self):
        with open(self.file) as f:
            lines = [Binary(int(line.rstrip())) for line in f]

        self.data = lines
        self.size = len(lines)
