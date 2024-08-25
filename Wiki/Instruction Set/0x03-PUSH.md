# PUSH

the SP(reg#0) is set to be the dst reg by the compiler
`PUSH` has a type 3 addressing mode

## The microcode
```text
0x0: Ra: Ra -> @SP; SP--
    3) SP -> MAR; SP-- -> Y     | RFout DSTsel DECA Yin MARin
    4) Ra -> MDR                | RFout MDRen
    5) MDR -> M[MAR]; Y -> SP   | RFin DSTsel Yout MDRen MEMsel WRsel
    6) END                      | TCend

0x1: @Ra: M[Ra] -> @SP; SP--
    3) Ra -> MAR                | RFout MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) SP -> MAR; SP-- -> Y     | RFout DSTsel Yin DECA MARin
    6) MDR -> M[MAR]            | MDRen WRsel MEMsel
    7) END                      | TCend

0x2: #N: #N -> @SP; SP--
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MD             | MDRen MEMsel
    5) SP -> MAR; SP-- -> Y     | RFout DSTsel MARin DECA Yin
    6) MDR -> M[MAR]; Y -> SP   | RFin DSTsel Yout MDRen MEMsel WRsel
    7) END                      | TCend

0x3: N: M[#N] -> @SP; SP--
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) MDR -> MAR               | MARin MDRen WRsel
    6) M[MAR] -> MDR            | MDRen MEMsel
    7) SP -> MAR; SP-- -> Y     | RFout DSTsel MARin DECA Yin
    8) MDR -> M[MAR]; Y -> SP   | RFin DSTsel You MDRen MEMsel WRsel
    9) END                      | TCend
```
