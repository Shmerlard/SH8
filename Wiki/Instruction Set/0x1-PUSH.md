# PUSH

in this command the SP (reg#0) is selected to be dst reg

```text
0x0: Ra: Ra -> @SP; SP--
    3) SP -> MAR; SP -> X       | RFout MARin Xin DSTsel
    4) Ra -> MD; X-- -> Y       | RFout DECX Yin MDRen 
    5) MD -> M[MAR]; Y -> SP    | MDRen WRsel MEMsel Yout DSTsel RFin

0x1: @Ra:
    3)

0x2: #N:
    3)

0x3: N:
    3)
```