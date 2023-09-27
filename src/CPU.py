from binary import *

class Register:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def incr(self):
        self.value += Binary(1)

class CPU:
    def __init__(self, instructions, registers):
        self.instructions = instructions
        self.registers = registers

    def __repr__(self):
        output = "= = = = CPU = = = =\n"
        output += "Register 1: " + str(self.registers[0].get_value()) + " (" + str(int(self.registers[0].get_value())) + ")\n"
        output += "Register 2: " + str(self.registers[1].get_value()) + " (" + str(int(self.registers[1].get_value())) + ")\n"
        output += "Register 3: " + str(self.registers[2].get_value()) + " (" + str(int(self.registers[2].get_value())) + ")\n"
        output += "Register 4: " + str(self.registers[3].get_value()) + " (" + str(int(self.registers[3].get_value())) + ")\n"
        output += "Register 5: " + str(self.registers[4].get_value()) + " (" + str(int(self.registers[4].get_value())) + ")\n"
        output += "= = = = = = = = = =\n"
        return output

    def add(self):
        self.registers[0].set_value(self.registers[0].get_value() + self.registers[1].get_value())

    def subtract(self):
        self.registers[0].set_value(self.registers[0].get_value() + self.registers[1].get_value())

    def assign(self, value):
        if self.registers[2].get_value() == Binary(1):
            self.registers[0].set_value(value)
            
        elif self.registers[2].get_value() == Binary(2):
            self.registers[1].set_value(value)

        elif self.registers[2].get_value() == Binary(3):
            self.registers[3].set_value(value - Binary(2))
            
        else:
            pass

    def perform_instruction(self, instruction):
        if instruction == self.instructions["add"]:
            self.add()

        elif instruction == self.instructions["sub"]:
            self.subtract()

        elif instruction == self.instructions["mod_reg1"]:
            self.registers[2].set_value(Binary(1))

        elif instruction == self.instructions["mod_reg2"]:
            self.registers[2].set_value(Binary(2))

        elif instruction == self.instructions["jmp"]:
            self.registers[2].set_value(Binary(3))

        elif instruction == self.instructions["write"]:
            self.registers[4].set_value(self.registers[0].get_value())

        elif instruction == self.instructions["recall"]:
            self.registers[0].set_value(self.registers[4].get_value())

        elif instruction == self.instructions["jg"]:
            if self.registers[0].get_value() > self.registers[1].get_value():
                self.registers[2].set_value(Binary(3))
            else:
                self.registers[2].set_value(Binary(0))

        elif instruction == self.instructions["jl"]:
            if self.registers[0].get_value() < self.registers[1].get_value():
                self.registers[2].set_value(Binary(3))
            else:
                self.registers[2].set_value(Binary(0))

        elif instruction == self.instructions["je"]:
            if self.registers[0].get_value() == self.registers[1].get_value():
                self.registers[2].set_value(Binary(3))
            else:
                self.registers[2].set_value(Binary(0))

        else:
            self.assign(instruction)

    def read_instruction(self, program):
        address = self.registers[3].get_value()
        new_instruction = program.data[int(address)]
        return new_instruction

    def step(self, program):
        instruction = self.read_instruction(program)
        self.perform_instruction(instruction)
        self.registers[3].incr()
