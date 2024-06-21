# PUSH

in this command the SP (reg#0) is selected to be src reg

```text
0x1: Ra: Ra -> @SP; SP--
    3) SP -> MAR; SP -> X       | RFout MARin Xin
    4) Ra -> MD; X-- -> Y       | RFout DSTsel DECX Yin MDRen 
    5) MD -> M[MAR]; Y -> SP    | MDRen WRsel MEMsel Yout DSTsel RFin

0x2: @Ra:
    3)

0x3: #N:
    3)

0x4: N:
    3)
```
