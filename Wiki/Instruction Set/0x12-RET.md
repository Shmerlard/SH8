# RET
the SP (reg#0) is selected to be `SRC` register

```text
0x0: RET: SP++; @SP -> PC
    3) SP++ -> Y                | RFout INCA Yin
    4) Y -> MAR : Y -> SP       | RFin Yout MARin
    5) M[MAR] -> MDR            | MDRen MEMsel
    6) MDR -> PC                | PCin MDRen WRsel
    7) END                      | TCend

0x1: NOP
    3) END                      | TCend

0x2: NOP
    3) END                      | TCend

0x3: NOP
    3) END                      | TCend
```



