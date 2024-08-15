# POP

in this command the SP (reg#0) is selected to be src reg

```text
0x0: Ra: @SP -> Ra; SP++
    3) SP -> MAR; SP -> X       | RFout MARin Xin
    4) M[MAR] -> MD; X++ -> Y   | MDRen WRsel MEMsel INCX Yin
    5) MD -> Ra                 | MDRen RFin DSTsel
    6) Y -> SP                  | Yout  RFin 

0x1: @Ra:
    3)

0x2: #N:
    3)

0x3: N:
    3)
```
