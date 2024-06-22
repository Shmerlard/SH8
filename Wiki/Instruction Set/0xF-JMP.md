# JMP

note: this include every possible jump: JNE/JL/JLS/JZ/JH/JHS/JMP
see more: [Condition Logic](../Condition-Logic.md)

```text
0x0: Ra: if(CON): Ra -> PC
    3) 

0x1: @Ra: if(CON): M[Ra] -> PC ##MIGHT BE USELESS
    3) 

0x2: #N: if(CON): #N -> PC
    3) PC -> MAR; PC++              | PCout PCinc MARin
    4) M[MAR] -> MDR Val -> CON     | Vout CONin MDRen MEMsel
    5) (CON = 1): MDR -> PC         | MDRen WRsel PCin
       (CON = 0): NOP               |
    6) TCend                        | TCend

0x3: N: if(CON) M[N] -> PC ##MIGHT BE USELESS
    3)
```
