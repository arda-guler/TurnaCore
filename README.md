# TurnaCore
TurnaCore is an imaginary 8-bit CPU with a custom architecture, created mainly for creating low-level programming challenges. [Read more about the architecture here](https://github.com/arda-guler/TurnaCore/blob/master/docs/CPU_architecture.txt) or below.

The AO language is a custom assembly language to write programs for TurnaCore machines. [Read more about it here](https://github.com/arda-guler/TurnaCore/blob/master/docs/AO_language.txt) or below.

## TurnaCore CPU Architecture

![CPU](https://github.com/arda-guler/TurnaCore/assets/80536083/8d1ba771-0a63-435f-9b72-fa8eb8f3ddaa)

TurnaCore is under development. The following information is valid for the current version.

The TurnaCore CPU has 5 registers, numbered 1, 2, 3, 4 and 5. Each register can hold a number between 00000000 and 11111111. (These values correspond to 0 and 255 in decimal.)

The TurnaCore CPU can execute programs on the memory, but it can not write to the memory.

Register 1 and 2 are general registers that can be directly written on. Addition and subtraction operations act on Register 1.

Register 3 is the operation mode register. It tells the CPU what to do with the upcoming numerical value to be read.

Register 4 is the address register. It keeps track of the address from which the instructions/data are being read. It increments automatically and keeps reading the loaded program from first instruction to the last, unless a jump command is executed. A jump command allows the value of Register 4 to be controlled directly, which makes loops, if-else conditionals and goto instructions possible.

Register 5 acts as a short term memory register. The value of Register 1 can be copied into Register 5, so that the value stored  in Register 5 can be copied into Register 1.

## AO Programming Language

The AO (ASM Operands) language is a very low-level assembly language designed for TurnaCore machines. 
It matches 1-to-1 to the equivalent compiled binary machine code. Actually, the only thing it makes is to
convert the "human-readable" TurnaCore instructions into corresponding binary values, which are "CPU-readable".

A program written in AO programming language is a combination of "instructions" and "data". All "instructions" 
and "data" are mere numbers, but the TurnaCore CPU architecture acknowledges certain numbers as built-in 
instructions to execute.

In AO programming language, each "expression" (either an instruction or data) is separated by spaces and
newline characters.

The following is an example AO program:
```
MR1
1
MR2
5
```

In this program, MR1 and MR2 are instructions whereas 1 and 5 are data. MR1 tells the CPU to switch to Modify 
Register 1 mode, and the following data 1 is then used to modify the value of Register 1. Then, the CPU is
switched to Modify Register 2 mode using the MR2 instruction. The last line is the data which is used to 
modify the value of Register 2. When this program is executed, Register 1 should hold the value 1 and Register 2
should hold the value 5.

The same program can be written as follows for better readability:
```
MR1 1
MR2 5
```

Do not forget that this is not a function - argument arrangement. 1 is not an argument for the MR1 insturction.
They are merely two expressions that come after each other.

You can use the semicolon (;) as the first character in a line to denote a comment line. 

Adding comments to the example program above can be done as follows:
```
; This program sets the value of Register 1 to 1 and Register 2 to 5.
; Let's set Register 1 first.
MR1 1
; Let's set Register 2 next.
MR2 5
; Voila!
```

AO files are compiled into CIS (compiled instruction sequence) files. These are the files which the CPU reads.

See TurnaCore Instruction Set for a list of all instructions.

## TurnaCore Instruction Set

**ADD**: Adds value in Register 2 onto Register 1

**SUB**: Subtracts value in Register 2 from Register 1

**MR1**: Switches CPU mode to "Modify Register 1"

**MR2**: Switches CPU mode to "Modify Register 2"

**JMP**: Switches CPU mode to "Jump"

**JG**: Switches CPU mode to "Jump" if Register 1 is greater than Register 2; else, switches to a dummy CPU mode

**JL**: Switches CPU mode to "Jump" if Register 1 is less than Register 2; else, switches to a dummy CPU mode

**JE**: Switches CPU mode to "Jump" if Register 1 is equal to Register 2; else, switches to a dummy CPU mode

**WRITE**: Copies Register 1 value to Register 5

**RECALL**: Copies Register 5 value to Register 1
