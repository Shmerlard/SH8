# AND

```text
0x0: Ra Rb: Ra AND Rb -> Rb
    3) Ra -> X                  | RFout Xin
    4) X AND Rb -> Y            | RFout DSTsel AND Yin  
    5) Y -> Rb                  | RFin DSTsel Yout

0x1: @Ra Rb: M[Ra] AND Rb -> Rb
    3) Ra -> MAR                | RFout MARin
    4) M[MAR] -> MDR, Rb -> X   | RFout DSTsel Xin MDRen MEMsel
    5) MDR AND X -> Y           | MDRen WRsel AND Yin
    6) Y -> Rb                  | Yout RFin DSTsel

0x2: #N Rb:
    3) PC -> MAR;PC++           | PCout PCinc MARin
    4) M[MAR] -> MDR; Rb -> X   | RFout DSTsel Xin MDRen MEMsel
    5) MDR AND X -> Y           | MDRen WRsel AND Yin
    6) Y -> Rb                  | Yout RFin DSTsel

```
