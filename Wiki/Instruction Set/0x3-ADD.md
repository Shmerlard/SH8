# ADD

```text
0x0: Ra Rb: Ra + Rb -> Rb
    3) Ra -> X
    4) X + Rb -> Y
    5) Y -> Rb

0x1: @Ra Rb: M[Ra] + Rb -> Rb
    3) Ra -> MAR
    4) Rb -> X; M[MAR] -> MDR
    5) X + MDR -> Y
    6) Y -> Rb

0x2: #N Rb: #N + Rb -> Rb
    3) PC -> MAR; PC++
    4) Rb -> X  ; M[MAR] -> MDR
    5) MDR + X -> Y
    6) Y -> Rb

```
