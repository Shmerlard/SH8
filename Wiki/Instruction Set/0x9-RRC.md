# RRC

```text
0x0: Ra Rb: Rb (Shifted R[Ra]<3...0> times) -> Rb
    3) Ra -> n                                  | RFout SCld
    4) Rb -> Y                                  | RFout DSTsel Y=A Yin
    5) NOP                                      | NOP 
    6) (n != 0 AND ALT = 0): Y SHR -> Y; n--    | RRC Yout Yin SCdec GOTO6
       (n != 0 AND ALT = 1): Y SHL -> Y; n--    | RLC Yout Yin SCdec GOTO6
       (n  = 0): Y -> Rb                        | Yout RFin DSTsel
    7) END                                      | TCend

0x1: @Ra Rb:
    3) 

0x2: #N Rb: Rb (Shifted #N times) -> Rb
    3) PC -> MAR; PC++                          | PCout MARin PCinc
    4) M[MAR] -> MD; Rb -> Y                    | RFout DSTsel Y=A Yin MDRen MEMsel
    5) MD -> n                                  | MDRen WRsel SCld
    6) (n != 0 AND ALT = 0): Y SHR -> Y; n--    | Yout Yin RRC SCdec GOTO6
       (n != 0 AND ALT = 1): Y SHL -> Y; n--    | Yout Yin RLC SCdec GOTO6
       (n  = 0): Y -> Rb                        | RFin DSTsel Yout
    7) END                                      | TCend

0x3: N, @Rb:
    3) 
```



