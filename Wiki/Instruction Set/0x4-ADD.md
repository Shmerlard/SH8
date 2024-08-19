# ADD

```text
0x0: Ra Rb: Ra + Rb -> Rb
    3) Ra -> X                  | Xin RFout
    4) X + Rb -> Y              | RFout DSTsel ADD Yin
    5) Y -> Rb                  | RFin DSTsel Yout
    6) END                      | TCend

0x1: @Ra Rb: M[Ra] + Rb -> Rb
    3) Ra -> MAR                | RFout MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X + MDR -> Y             | ADD Yin MDRen WRsel
    6) Y -> Rb                  | Yout RFin DSTsel
    7) END                      | TCend

0x2: #N Rb: #N + Rb -> Rb
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X  ; M[MAR] -> MDR | RFout DSTsel Xin MDRen MEMsel
    5) MDR + X -> Y             | ADD Yin MDRen WRsel
    6) Y -> Rb                  | Yout RFin DSTsel
    7) END                      | TCend

0x3: N Rb: M[#N] + Rb -> Rb
    3) END                      | TCend

```
