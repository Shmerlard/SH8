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

## Instruction set (DEPRECTED)
```
0: MOV  Ra/imm8     Rb          | Ra/imm8           -> Rb
1: LDW  HL/imm16    Rb          | M[HL/imm16]       -> Rb
2: STW  Ra          HL/imm16    | Ra                -> M[HL/imm16]
3: LDA  imm16                   | imm16             -> HL       
4: CMP* ra          rb          | Rb - Ra           
5: JNZ                          | (z != 0) : HL     -> PC   
6: INB  ra                      | inr               -> Ra   
7: OUTB ra                      | ra                -> OUTR 
8: ADD* Ra/imm8     Rb          | Ra/imm8 + Rb      -> Rb   
9: ADC* Ra/imm8     Rb          | Ra/imm8 + Rb + C  -> Rb   
    A: SUB* Ra/imm8     Rb          | Rb - Ra/imm8      -> Rb   
B: AND  Ra/imm8     Rb          | Ra AND Rb         -> Rb   
C: OR   Ra/imm8     Rb          | Ra OR  Rb         -> Rb   
D: XOR  Ra/imm8     Rb          | Ra XOR Rb         -> Rb 
E: 
F: NOP    

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
