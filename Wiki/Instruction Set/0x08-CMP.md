# CMP
Basically its like `SUB` only that `Rb` is not updated after

```text
0x0: Ra Rb: Rb - Ra
    3) Ra -> X                  | RFout Xin
    4) Rb - X -> Y              | RFout DSTsel SUB Yin
    5) END                      | TCend

0x1: @Ra Rb: Rb - M[Ra]
    3) Ra -> MAR                | RFout MARin
    4) Rb -> X; M[MAR] -> MDR   | RFout DSTsel Xin MDRen MEMsel
    5) X - MDR -> Y             | SUB Yin MDRen WRsel 
    6) END                      | TCend

0x2: #N Rb: Rb - #N
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) MDR -> X                 | MDRen WRsel
    6) Rb - X -> Y              | SUB Yin
    7) END                      | TCend

0x4: N Rb:
    3) 
```

