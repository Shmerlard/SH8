# The micro code

## The control lines

the control lines are divided to 4 8-bit eeproms

### EEPROM 0

```text
PROGRAM COUNTER:
    PCin        | Reads the content of the bus to the PC
    PCout       | Output the content of the PC to the BUS
    PCinc       | increment the PC by 1

REGISTER FILE:
    RFin        | Reads the content of the bus to the selected register
    RFout       | Output the content of the selcted register to bus
    DSTsel      | if 1: select the dst reg, if 0: selects the src reg

INSTRUCTION REGISTER:
    IRin        | reads the content of the bus to the IR
    Vout        | output the last 5 bit of the IR to the bus
```

### EEPROM 1

```text
MEMORY REGISTERS:
    MARin       | reads the content of the bus to the MAR
    MDRen       | enables RD/WR to the MDR
    WRsel       | if 1: enables write to the MDR, if 0: enables read
    MEMsel      | if 1: selects the memory, if 0: selects the bus

TIMING CONTROL:
    TCend       | reset the time control to 0
    GOTO6       | sets the time control to 6

SHIFT CONTROL:
    SCld        | reads the content of the bus to the shift cotrol
    SCdec       | decrement the shift control by 1
```

### EEPROM 2

```text
ALU:
    Xin         | reads the content of the bus to X-reg
    Yin         | reads the output of the ALU to Y-reg
    Yout        | output the Y-reg to the bus, also write the flags to SR
    ALUctrl[0]  | select the alu controls
    ALUctrl[1]  
    ALUctrl[2]
    ALUctrl[3]

CONDITION CONTROL:
    CONin       | input the bus to the condition logic
```

## The input lines

```text
CON (1bit)
SHIFT CONTROL n=0 (1bit)    
ADDRESSING MODE (3bits)
OPCODE (4bits)
TIME CONTROL (4bits)
```
