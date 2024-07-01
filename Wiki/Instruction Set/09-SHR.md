# SHR

**only 4lsb bits

```text
0: Ra Rb    | (Rb>>Ra) -> Rb
    4) Ra -> n                      | RFout SCld
    5) Rb -> Y,X                    | RFout DSTsel Yin Xin Y=B
    6) (n = 0) : Y -> Rb END        | Yout DSTsel RFin TCend
       (n != 0): Y>>1 -> X, n-1 -> n| Xin SHR Yout SCdec
    7) X -> Y, 6 -> tc              | Yin GOTO6 Y=X

1: Ra @Rb   | (M[Rb]>>Ra) -> M[Rb]
    4)

2: @Ra Rb   | (Rb>>M[Ra]) -> Rb 
    4)

3: @Ra @Rb  | 
    4)

4: #N Rb    | (Rb>>N) -> Rb
    4) 

5: #N, @Rb  |
    4)

6: N, Rb    |
    4)

7: Ra, N    |
    4)

```
