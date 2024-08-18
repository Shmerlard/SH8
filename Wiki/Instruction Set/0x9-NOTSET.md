# RET


in this command `SP` is set to be the `SRC` register
```text
0x0: SP++ ; @SP -> PC 
    3) SP -> X              | RFout Xin
    4) X++ -> Y             | INCX Yin
    5) Y  -> SP, Y -> MAR   | Yout RFin MARin
    6) M[MAR] -> MDR        | MDRen MEMsel WRsel
    7) MDR -> PC            | MDRen PCin
```
