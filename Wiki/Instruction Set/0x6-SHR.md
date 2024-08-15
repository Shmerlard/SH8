# SHR

```text
0x0: Ra Rb: Rb (Shifted R[Ra] times) -> Rb
    3) Ra -> n                          | RFout SCld
    4) Rb -> Y                          | RFout DSTsel Y=B Yin
    5) (n != 0): Y SHR -> Y; n--        | SHR Yout Yin SCdec
       (n  = 0): Y -> Rb                | Yout RFin DSTsel
    6) GOTO5                            | GOTO5      #### NOTFINISHED


0x1: Ra @Rb:
    3) 

0x2: @Ra Rb:
    3) 

0x3: #N Rb:
    3) 

0x4: #N, @Rb:
    3) 

0x5: N, Rb:
    3) 

0x6: Ra, N:
    3) 

0x7: SPECIAL
```

```text
0x1: Ra:
    3)

0x2: @Ra:
    3)

0x3: #N:
    3)

0x4: N:
    3)
```
