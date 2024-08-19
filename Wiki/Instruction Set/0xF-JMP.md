# JMP

note: this include every possible jump: JEQ/JNE/JL/JLS/JH/JHS/JMP
see more: [Condition Logic](../Condition-Logic.md)
the register A is set to be the source register by the assembler

```text
0x0: Ra: if(CON): Ra -> PC
    3) Val -> CON                   | Vout CONin
    4) (CON = 1): Ra -> PC          | RFout PCin
       (CON = 0): NOP               | NOP
    5) END                          | TCend

0x1: @Ra: if(CON): M[Ra] -> PC
    3) 

0x2: #N: if(CON): #N -> PC
    3) PC -> MAR; PC++              | PCout PCinc MARin
    4) M[MAR] -> MDR ;Val -> CON    | Vout CONin MDRen MEMsel
    5) (CON = 1): MDR -> PC         | MDRen WRsel PCin
       (CON = 0): NOP               |
    6) END                          | TCend

0x3: N: if(CON) M[N] -> PC ##MIGHT BE USELESS
    3)
```
