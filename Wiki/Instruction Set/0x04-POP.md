# POP

in this command the SP (reg#0) is selected to be src reg

```text
0x0: Ra: SP++; @SP -> Ra
    3) SP++ -> Y                | RFout INCA Yin
    4) Y -> MAR : Y -> SP       | RFin Yout MARin
    5) M[MAR] -> MDR            | MDRen MEMsel
    6) MDR -> Ra                | RFin DSTsel MDRen WRsel
    7) END                      | TCend

0x1: @Ra: SP++; @SP -> @Ra
    3) SP++ -> Y                | RFout Yin INCA
    4) Y -> MAR: Y -> SP        | RFin Yout MARin
    5) M[MAR] -> MDR            | MDRen MEMsel
    6) Ra -> MAR                | RFout DSTsel MARin
    7) MDR -> M[MAR]            | MDRen WRsel MEMsel
    8) END                      | TCend

0x2: #N: SP++; @SP -> M[#N]
    3) SP++ -> Y                | RFout Yin INCA
    4) Y -> MAR: Y -> SP        | RFin Yout MARin
    5) M[MAR] -> MDR            | MDRen MEMsel
    6) MDR -> Y                 | Yin Y=A MDRen WRsel
    7) PC -> MAR; PC++          | PCout PCinc MARin
    8) M[MAR] -> MDR            | MDRen MEMsel
    9) MDR -> MAR               | MARin MDRen WRsel
   10) Y -> MDR                 | Yout MDRen
   11) MDR -> M[MAR]            | MDRen MEMsel WRsel
   12) END                      | TCend

0x3: N: SP++; @SP -> M[M[N]]
    3) END                      | TCend
```
