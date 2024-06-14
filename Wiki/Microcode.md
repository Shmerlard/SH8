# The micro code

## The control lines
the control lines are divided to 4 8-bit eeproms
### EEPROM 0
```
PROGRAM COUNTER:
    PCin
    PCout
    PCinc

REGISTER FILE:
    RFin
    RFout
    DSTsel

INSTRUCTION REGISTER:
    IRin
    IRout
```
### EEPROM 1
```
MEMORY REGISTERS:
    MARin
    MDRen
    WRsel
    MEMsel

TIMING CONTROL:
    TCend
    GOTO6
    HLT
```
### EEPROM 2
```
ALU:
    Xin
    Yin
    Yout
    ALUctrl[0]
    ALUctrl[1]
    ALUctrl[2]
    ALUctrl[3]
```
### EEPROM 3
```
NOT YET IMPLEMENTED:
    RST_EN
    IN_REG
    OUT_REG

CONDITION CONTROL:
    CONin

SHIFT CONTROL:
    SCld
    SCdec
```
## The input lines
```
CON (1bit)
SHIFT CONTROL n=0 (1bit)    
ADDRESSING MODE (3bits)
OPCODE (5bits)
TIME CONTROL (4bits)
```