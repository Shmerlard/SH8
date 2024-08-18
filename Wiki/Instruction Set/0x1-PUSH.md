# PUSH

although `PUSH` uses only one register it is a type 2 instruction since the SP(reg#0) is set to be the dst reg by the compiler

```text
0x0: Ra: Ra -> @SP; SP--
    3) SP -> MAR; SP-- -> Y     | RFout DSTsel DECA Yin MARin
    4) Ra -> MDR                | RFout MDRen
    5) MDR -> M[MAR]; Y -> SP   | RFin DSTsel Yout MDRen MEMsel WRsel
    6) END                      | TCend

0x1: @Ra:
    3)

0x2: #N: #N -> @SP; SP--
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MD             | MDRen MEMsel
    5) SP -> MAR; SP-- -> Y     | RFout DSTsel MARin DECA Yin
    6) MDR -> M[MAR]; Y -> SP   | RFin DSTsel Yout MDRen MEMsel WRsel
    7) END                      | TCend

0x3: N:
    3)
```
