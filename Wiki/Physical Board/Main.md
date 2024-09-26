## The Physical Board

I used KiCad to design the schematics and PCB's

The whole CPU is divided into the following modules and boards:

1. The Register File Module (16):
    a. 15 Registers, 14 GP and 1 Status Register
    b. 1 Register File Manger board

2. IR PC (5):
    a. the IR board 
    b. the PC board
    c. the CON board
    d. the SC board
    e. the TC board

3. ALU module (4):
    a. 2 register boards (X,Y)
    b. ALU
    c. Cycle enabler

4. MEM and Control logic (3):
    a. RAM and ROM board
    b. MAR MDR
    c. Control board
