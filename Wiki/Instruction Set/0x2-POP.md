# POP

in this command the SP (reg#0) is selected to be src reg

```text
0x0: Ra: SP++; @SP -> Ra
    3) SP++ -> Y                | RFout INCA Yin
    4) Y -> MAR : Y -> SP       | RFin Yout MARin
    5) M[MAR] -> MDR            | MDRen MEMsel
    6) MDR -> Ra                | RFin DSTsel MDRen WRsel
    7) END                      | TCend

0x1: @Ra:
    3)

0x2: #N:
    3)

0x3: N:
    3)

0x7: RET: SP++; @SP -> PC
    3) 
    
```
