# The micro code

## The control lines
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

ALU:
    Yin
    Yout
    Xin
    ALUctrl[0]
    ALUctrl[1]
    ALUctrl[2]

MEMORY REGISTERS:
    MARin
    MDRin
    MDout
    MEMsel
    WRsel

TIMING CONTROL:
    TCend

CONDITION CONTROL:
    CONin

OPTIONAL (not yet implemnted):
    HLT
    IOR
    IOW

```