# TurnaCore

![Multiplication](https://github.com/arda-guler/TurnaCore/assets/80536083/bfe4d51a-ab84-478c-afe1-7f4115404b06)

*A TurnaCore machine multiplying 13 and 27.*

TurnaCore is an imaginary 16-bit CPU with a custom architecture, created mainly for creating low-level programming challenges. [Read more about the architecture here](https://github.com/arda-guler/TurnaCore/blob/master/docs/CPU_architecture.txt).

The AO language is a custom assembly language to write programs for TurnaCore machines. [Read more about it here](https://github.com/arda-guler/TurnaCore/blob/master/docs/AO_language.txt).

Don't forget to read the docs!

## Use

**Run src/main.py** to start the TurnaCore machine. A TurnaCore machine can load one program into memory at a time (unless you write two programs back to back on the same source code file).

Running simply as:
```
main.py
```
powers up a TurnaCore machine. The emulator will then scan the /programs folder and ask you to pick a program to run. Then, it will as you whether you want to run the program in *slow mode* (explained below) or not.

Running via:
```
main.py <filename>
```
powers up a TurnaCore machine and loads up a program into memory. The emulator starts in *slow mode* (explained below) by default.

Running via:
```
main.py <filename> <slow_mode(Y/n)>
```
allows you to pick whether you want to start in *slow mode* (explained below) or not.

## What is this 'Slow Mode' anyway?

Slow mode has a Tkinter GUI for easily keeping track of what the machine is doing. The machine takes quite a lot longer to execute each instruction so that your eyes can keep up with the numbers. Good for debugging and education, not good for running extremely large programs just for the result. If slow mode is not enabled, instructions are carried out as fast as possible, with no GUI output (just the command line printouts at the end of the program).
