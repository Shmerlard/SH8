# ADD

```text
0x0: Ra Rb: Ra + Rb -> Rb
    3) Ra -> X                  | Xin RFout
    4) X + Rb -> Y              | DSTsel RFout ADD Yin
    5) Y -> Rb                  | DSTsel RFin Yout

0x1: @Ra Rb: M[Ra] + Rb -> Rb
    3) Ra -> MAR                | RFout MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen WRsel MEMsel
    5) X + MDR -> Y             | ADD MDRen Yin
    6) Y -> Rb                  | Yout RFin DSTsel

0x2: #N Rb: #N + Rb -> Rb
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X  ; M[MAR] -> MDR | RFout DSTsel Xin MDRen MEMsel WRsel
    5) MDR + X -> Y             | ADD Yin MDRen
    6) Y -> Rb                  | Yout RFin DSTsel

```
