from binary import *
from compiler import *
from consts import *

class Memory:
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
        output = "\nMEMORY:\n"
        output += "--------\n"
        for idx, i in enumerate(self.data):
            output += str(idx) + ": " + str(i) + "\n"

        return output

    def load(self):
        with open(self.file) as f:
            lines = [Binary(int(line.rstrip())) for line in f]

        self.data = lines
        self.size = len(lines)

    def write_to_memory(self, address, value):
        address = int(address)

        if address <= len(self.data) - 1:
            self.data[address] = value
            return
        
        if address > len(self.data) - 1:
            padding = address - len(self.data) + 1
            for i in range(padding):
                self.data.append(NULL)

        self.data.append(value)
        self.size = len(self.data)

    def read_from_memory(self, address):
        address = int(address)
        
        if address > len(self.data) - 1:
            return NULL

        return self.data[address]
