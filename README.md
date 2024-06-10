# The shmerlard 16
an 8 bit cpu

## Specs
- a common 16-bit data and address bus 
- 4 GP register

## Contents
1) [Registers](/Wiki/Register-File.md)
2) [Instruction Register](/Wiki/Instruction-Register.md)
3) [ALU](/Wiki/ALU.md)
4) [Control Unit](/Wiki/ControlUnit.md)
5) [Memory Registers](/Wiki/Memory-Registers.md)

## Instruction set
```
0x00:  NOP
0x01:  MOV  Ra/#, Rb       | Ra/# -> Rb
0x02:  LD   Ra/#, Rb       | M[Ra/#] -> Rb
0x03:  ST   Ra,   Rb/#     | Ra -> M[Rb/#]
0x04:  PUSH Ra/#           | SP - 2 -> SP; Ra/# -> @SP
0x05:  POP  Ra             | @SP -> Ra; SP + 2 -> SP
--- Arithmetic instructions ---
0x06:  ADD  Ra/#, Rb       | Ra/# + Rb -> Rb
0x07:  ADDC Ra/#, Rb       | Ra/# + Rb + c -> Rb
0x08:  SUB  Ra/#, Rb       | Rb - Ra/#-> Rb
0x09:  RRA  Ra/#, Rb       | RRA Rb (Ra/# times) -> Rb
0x0A:  RRC  Ra/#, Rb       | RRC Rb (Ra/# times) -> Rb
--- Jumps and Subroutiness  ---
0x0B:  CALL DST            | SP - 2 -> SP; PC -> @SP; DST -> PC;   
0x0C:  RET                 | @SP -> PC; SP + 2  -> SP;             
0x0D:  CMP  Ra/#, Rb       | Rb - Ra/#                             
0x0E:  JMP  DST            | DST -> PC                             
0x0F:  JEQ  DST            | (Z = 1): DST -> PC                        
0x10:  JHS  DST            | (C = 1): DST -> PC                        
--- Logical operations      ---
0x11:  AND  Ra/#, Rb       | Ra/# AND Rb -> Rb
0x12:  OR   Ra/#, Rb       | Ra/# OR  Rb -> Rb                  
0x13:  XOR  Ra/#, Rb       | Ra/# XOR Rb -> Rb
--- Input and output        ---
0x14:  IOR  Ra             | IOR -> Ra
0x15:  IOW  Ra/#           | Ra  -> IOR
0x16:           
0x17:         
0x18:                

(*) : FLAGS register is affected

Other Instructions that has to be simulated
INC  Ra                         | Ra + 1 -> Ra | ADD #0x1   Ra
DEC  Ra                         | Ra - 1 -> Ra | SUB Ra     #0x1
INCD Ra                         | Ra + 2 -> Ra | ADD #2     Ra
DECD Ra                         | Ra - 2 -> Ra | SUB Ra     #2
NOT  Ra Rb                      | NOT Ra -> Rb | XOR #0xFF  Ra

PUSH Ra/imm8                 | SP-- ; Ra/imm8    -> M[SP]
POP  Ra                      | M[SP] -> Ra ; SP++

CALL        RET         JZ      JLO     JH      JC      JEQ     JGE
SET(CZVN)   CLR(CZVN)   INC        NOT     JMP     shc shl shr     
```
## Registers
```
0: SP       : STACK Pointer
1: REG A    : GP
2: REG B    : GP
3: REG C    : GP
4: REG D    : GP
5: REG L    : LOW address register
6: REG H    : HIGH address register
7: REG F    : FLAGS register
```
## [Memory](/Wiki/Memory-Registers.md)
the memory ranges from `0x0000` to `0xFFFF` since the adress is 16-bit.
the memory is mapped in the following way:
```
0x0000 - 0x7FFF: GP ROM              (32KiB    ROM)
0x8000 - 0xBFFF: GP RAM              (16KiB     RAM) 
0xC000 - 0xCFFF: VRAM                (16KiB    RAM) #CURRENTLY NOT IN USE#
0xD000 - 0xFDFF: NOT IN USE          (11.5KiB UNUSED)
0xFE00 - 0xFEFF: STACK               (256B    STACK)
0xFF00 - 0xFFFF: UNUSED              (256B    UNUSED)

```

## Instruction format
The instruction register is a 16-bit register
```
the format is XXXXX-SSS-DDD-AA-D-FF
XXXX = the opcode of the instruction
Y    = indicates if the instruction uses immediate addressing mode 
       0 if not; 1 if yes
ZZZ  = indicates the dst register
A-S  = indicates the source value or register; dependes on the Y bit.

```

# Full diagram
![text](Diagrams/Main-Diagram.png)
