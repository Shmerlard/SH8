# PUSH

although `PUSH` uses only one register it is a type 2 instruction since the SP(reg#0) is set to be the dst reg by the compiler

```text
0x0: Ra: Ra -> @SP; SP--
    3) SP -> MAR; SP -> X       | RFout MARin Xin DSTsel
    4) Ra -> MD; X-- -> Y       | RFout DECX Yin MDRen 
    5) MD -> M[MAR]; Y -> SP    | MDRen WRsel MEMsel Yout DSTsel RFin

0x1: @Ra:
    3)

0x2: #N: #N -> @SP; SP--
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MD             | MDRen WRsel MEMsel
    5) SP -> MAR; SP -> X       | DSTsel RFout MARin Xin
    6) MD -> M[MAR]; X++ -> Y   | MDRen MEMsel INCX Yin 
    7) Y -> SP                  | Yout DSTsel RFin

0x3: N:
    3)
```
