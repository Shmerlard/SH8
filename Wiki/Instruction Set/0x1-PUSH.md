# PUSH

although `PUSH` uses only one register it is a type 2 instruction since the SP(reg#0) is set to be the dst reg by the compiler

```text
0x0: Ra: Ra -> @SP; SP--
    3) SP -> MAR; SP-- -> Y     | RFout DSTsel DECA Y=A Yin MARin
    4) Ra -> MD                 | RFout MDRen WRsel
    5) MD -> M[MAR]; Y -> SP    | RFin DSTsel Yin MDRen MEMsel

0x1: @Ra:
    3)

0x2: #N: #N -> @SP; SP--
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MD             | MDRen WRsel MEMsel
    5) SP -> MAR; SP-- -> Y     | RFout DSTsel MARin DECA Y=A Yin
    6) MD -> M[MAR]; Y -> SP    | RFin DSTsel Yin MDRen MEMsel

0x3: N:
    3)
```
