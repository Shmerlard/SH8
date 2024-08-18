# CALL

the `SP` is set to be the source register and `Ra` is set to be the destination register

```text
0x0: Ra: PC -> @SP; Ra -> PC; SP-- -> SP;
    3) PC -> MDR                | PCout MDRen
    4) SP -> MAR; SP-- -> Y     | RFout Yin DECA MARin
    5) MDR -> M[MAR]; Y -> SP   | RFin Yout MDRen MEMsel WRsel
    6) Ra -> PC                 | RFout DSTsel PCin
    7) END                      | TCend

0x1: @Ra: 
    3)

0x2: #N: PC -> @SP; #N -> PC; SP-- -> SP;
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) MDR -> Y                 | Yin Y=A MDRen WRsel
    6) PC -> MDR                | PCout MDRen
    7) Y -> PC                  | Yout PCin
    8) SP -> MAR; SP-- -> Y     | RFout MARin DECA Yin
    9) MDR -> M[MAR]; Y -> SP   | RFin Yout MDRen MEMsel WRsel
   10) END                      | TCend

0x3: N:
    3)a
```
