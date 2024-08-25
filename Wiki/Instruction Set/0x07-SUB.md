# SUB

```text
0x0: Ra Rb: Rb - Ra -> Rb
    3) Ra -> X              | RFout Xin
    4) Rb - X -> Y          | RFout DSTsel SUB Yin
    5) (ALT = 0): Y -> Rb   | RFin DSTsel Yout 
    6) END                  | TCend

0x1: @Ra Rb:
    3)

0x2: #N Rb: Rb - #N -> Rb
    3) PC -> MAR; PC++      | PCout PCinc MARin
    4) M[MAR] -> MDR        | MDRen MEMsel
    5) MDR -> X             | MDRen WRsel
    6) Rb - X -> Y          | SUB Yin
    7) Y -> Rb              | RFin DSTsel Yout
    8) END                  | TCend

0x4: N Rb:
    3) 
```
