# SUB

```text
0x0: Ra Rb: (Rb - Ra -> Rb)
    3) Ra -> X          | RFout Xin
    4) Rb - X -> Y      | RFout DSTsel SUB Yin
    5) Y -> Rb          | RFin DSTsel Yout 
    6) END              | TCend

0x1: Ra @Rb:
    3) 

0x2: @Ra Rb:
    3) 

0x3: #N Rb:
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) MDR -> X                 | MDRen WRsel
    6) Rb - X -> Y              | SUB Yin
    7) Y -> Rb                  | RFin DSTsel Yout
    8) END                      | TCend

0x4: #N, @Rb:
    3) 

0x5: N, Rb:
    3) 

0x6: #N, Rb: (CMP #N Rb) Rb - #N -> Y
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) MDR -> X                 | MDRen WRsel
    6) Rb - X -> Y              | SUB Yin
    7) END                      | TCend

0x7: Rb - Ra -> Y :(CMP Ra Rb)
    3) Ra -> X                  | RFout Xin
    4) Rb - X -> Y              | RFout DSTsel SUB Yin
    5) END                      | TCend
```
