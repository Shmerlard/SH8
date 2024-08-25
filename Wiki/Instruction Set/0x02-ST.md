# ST

```text
0x0: Ra @Rb: Ra -> M[Rb]
    3) Rb -> MAR            | RFout DSTsel MARin
    4) Ra -> MDR            | RFout MDRen
    5) MDR -> M[MAR]        | MDRen WRsel MEMsel
    6) END                  | TCend

0x1: Ra #N: Ra -> M[#N]
    3) PC -> MAR; PC++      | PCout PCinc MARin
    4) M[MAR] -> MDR        | MDRen MEMsel
    5) MDR -> MAR           | MARin MDRen WRsel
    6) Ra -> MDR            | RFout MDRenk
    7) MDR -> M[MAR]        | MDRen WRsel MEMsel
    8) END                  | TCend

0x2: #N @Rb: #N -> M[Rb]
    3) PC -> MAR; PC++      | PCout PCinc MARin
    4) M[MAR] -> MDR        | MDRen MEMsel
    5) Rb -> MAR            | RFout DSTsel MARin
    6) MDR -> M[MAR]        | MDRen WRsel MEMsel
    7) END                  | TCend

0x3: Ra N: Ra -> M[M[#N]]
    3) PC -> MAR; PC++      | PCout PCinc MARin
    4) M[MAR] -> MDR        | MDRen MEMsel
    5) MDR -> MAR           | MARin MDRen WRsel
    6) M[MAR] -> MDR        | MDRen MEMsel
    7) MDR -> MAR           | MARin MDRen WRsel
    8) Ra -> MDR            | RFout MDRen
    9) MDR -> M[MAR]        | MDRen WRsel MEMsel
   10) END                  | TCend

```
