# ADDC

`ADDC` is a type 2 instruction that adds two numbers with carry

```text
0x0: Ra Rb: Ra + Rb + c -> Rb
    3) Ra -> X                  | RFout Xin
    4) X + Rb + c -> Y          | RFout DSTsel ADDC Yin
    5) Y -> Rb                  | RFin DSTsel Yout
    6) END                      | TCend

0x1: @Ra Rb: M[Ra] + Rb + c -> Rb
    3) Ra -> MAR                | RFout MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X + MDR + c -> Y         | ADDC Yin MDRen WRsel
    6) Y -> Rb                  | RFin DSTsel Yout
    7) END                      | TCend

0x2: #N Rb: #N + Rb + c -> Rb
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X  ; M[MAR] -> MDR | RFout DSTsel Xin MDRen MEMsel
    5) MDR + X + c -> Y         | ADDC Yin MDRen WRsel
    6) Y -> Rb                  | Yout RFin DSTsel
    7) END                      | TCend

0x3: N Rb:
    3) 
```
