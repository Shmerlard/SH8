# OR

```text
0x0: Ra Rb: Ra OR Rb -> Rb
    3) Ra -> X                  | RFout Xin
    4) X OR Rb -> Y             | RFout DSTsel OR Yin  
    5) Y -> Rb                  | RFin DSTsel Yout
    6) END                      | TCend

0x1: Ra @Rb:
    3)

0x2: @Ra Rb:
    3)

0x3: #N Rb: #N OR Rb -> Rb
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X OR MDR -> Y            | Yin OR MDRen WRsel
    6) Y -> Rb                  | RFin DSTsel Yout
    7) END                      | TCend

```
