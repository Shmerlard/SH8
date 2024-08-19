# ST

```text
0x0: #N #K: #N -> M[#K]
    3) END                  | TCend

0x1: Ra @Rb: Ra -> M[Rb]
    3) Rb -> MAR            | RFout DSTsel MARin
    4) Ra -> MDR            | RFout MDRen
    5) MDR -> M[MAR]        | MDRen WRsel MEMsel
    6) END                  | TCend

0x2: Ra #N: Ra -> M[#N]
    3) END                  | TCend

0x1: Ra N: Ra -> M[M[#N]]
    3) END                  | TCend

```
