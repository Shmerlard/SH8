# NOT

```text
0x0: Ra Rb: ¬Ra -> Rb
    3) ¬Ra -> Y         | RFout NOT Yin
    4) Y -> Rb          | RFin DSTsel Yout
    5) END              | TCend

0x1: @Ra Rb: ¬M[Ra] -> Rb
    3) Ra -> MAR        | RFout MARin
    4) M[MAR] -> MDR    | MDRen MEMsel
    5) ¬MDR -> Y        | NOT Yin MDRen WRsel
    6) Y -> Rb          | RFin DSTsel Yout

0x2: #N Rb: ¬#N -> Rb
    3) PC -> MAR; PC++  | PCout PCinc MARin
    4) M[MAR] -> MDR    | MDRen MEMsel
    5) ¬MDR -> Y        | NOT Yin MDRen WRsel
    6) Y -> Rb          | RFin DSTsel Yout
    7) END              | TCend

0x3: N Rb:
    3)
```
