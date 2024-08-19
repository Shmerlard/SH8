# ADDC

`ADDC` is a type 2 instruction that adds two numbers with carry

```text
0x0: Ra Rb: Ra + Rb + c -> Rb
    3) Ra -> X                  | RFout Xin
    4) X + Rb + c -> Y          | RFout DSTsel ADDC Yin
    5) Y -> Rb                  | RFin DSTsel Yout
    6) END                      | TCend

0x1: @Ra Rb:
    3) 

0x2: #N Rb:
    3) 

0x3: N Rb:
    3) 
```
