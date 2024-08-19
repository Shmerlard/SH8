# XOR

```text
0x0: Ra Rb: Ra XOR Rb -> Rb
    3) Ra -> X                  | RFout Xin
    4) X XOR Rb -> Y            | RFout DSTsel XOR Yin  
    5) Y -> Rb                  | RFin DSTsel Yout
    6) END                      | TCend

0x1: @Ra Rb: M[Ra] XOR Rb -> Rb
    3) Ra -> MAR                | RFout MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X XOR MDR -> Y           | Yin XOR MDRen WRsel
    6) Y -> Rb                  | RFin DSTsel Yout
    7) END                      | TCend

0x2: #N Rb: #N XOR Rb -> Rb
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X XOR MDR -> Y           | Yin XOR MDRen WRsel
    6) Y -> Rb                  | RFin DSTsel Yout
    7) END                      | TCend

0x3: N Rb: M[#N] XOR Rb -> Rb
    3) PC -> MAR PC++           | PCout PCinc MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) MDR -> MAR               | MARin MDRen WRsel
    6) M[MAR] -> MDR            | MDRen MEMsel
    7) MDR XOR X -> Y           | Yin XOR MDRen WRsel
    8) Y -> Rb                  | RFin DSTsel Yout
    9) END                      | TCend
```
