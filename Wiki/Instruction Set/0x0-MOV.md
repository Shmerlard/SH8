# MOV

```text
0x0: Ra Rb: Ra -> Rb
    3) Ra -> Y              | RFout Yin Y=B
    4) Y  -> Rb             | RFin DSTsel Yout
    5) END                  | TCend

0x1: Ra @Rb: Ra -> M[Rb]
    3) Rb -> MAR            | RFout DSTsel MARin
    4) Ra -> MDR            | RFout MDRen 
    5) MDR-> M[MAR]         | MDRen MEMsel WRsel
    6) END                  | TCend

0x2: @Ra Rb: M[Ra] -> Rb
    3) Ra -> MAR            | RFout MARin
    4) M[MAR] -> MD         | MDRen MEMsel
    5) MDR -> Rb            | RFin DSTsel MDRen WRsel
    6) END                  | TCend

0x3: #N Rb: #N -> Rb
    3) PC -> MAR; PC++      | PCout  MARin PCinc
    4) M[MAR] -> MDR        | MEMsel MDRen
    5) MDR -> Rb            | RFin   RFin  DSTsel MDRen WRsel
    6) END                  | TCend

```
