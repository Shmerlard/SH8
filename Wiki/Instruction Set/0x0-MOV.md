# MOV

```text
0x0: Ra Rb:
    3) Ra -> Y              | RFout, Yin, Y=B
    4) Y  -> Rb             | RFin, DSTsel, Yout, END

0x1: Ra @Rb:
    3) Rb -> MAR
    4) Ra -> MD
    5) MD -> M[MAR]

0x2: @Ra Rb:
    3) Ra -> MAR
    4) M[MA] -> MD
    5) MD -> Rb

0x3: #N Rb:
    3) PC -> MAR; PC++      | PCout, MARwr, PCinc
    4) M[MA] -> MD          | MEMsel, MDRin
    5) MD -> Rb             | MDRout, DSTsel, IRin,END

0x4: #N, @Rb:
    3) PC -> MAR; PC++
    4) M[MAR] -> MD; Rb -> MAR*
    5) MD -> M[MAR]

0x5: N, Rb:
    4) PC -> MAR; PC++
    5) M[MAR] -> MD
    6) MD -> MAR
    7) M[MAR] -> MD
    8) MD -> Rb

0x6: Ra, N:
    4) PC -> MAR; PC++
    5) M[MAR] -> MD
    6) MD -> MAR
    7) Ra -> MD
    8) MD -> M[MAR]

0x7: SPECIAL
```
