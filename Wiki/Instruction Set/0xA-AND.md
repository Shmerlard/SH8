# AND

```text
0x0: Ra Rb: Ra AND Rb -> Rb
    3) Ra -> X                  | RFout Xin
    4) X AND Rb -> Y            | RFout DSTsel AND Yin  
    5) Y -> Rb                  | RFin DSTsel Yout
    6) END                      | TCend

0x1: Ra @Rb:
    3)

0x2: @Ra Rb:
    3)

0x3: #N Rb: #N AND Rb -> Rb
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X AND MDR -> Y           | Yin AND MDRen WRsel
    6) Y -> Rb                  | RFin DSTsel Yout
    7) END                      | TCend

```
