# CMP

pretty much like the `SUB` but without inserting to `Rb`
```text

0x0: Rb Ra: Rb - Ra -> Y
    3) Ra -> X                  | RFout Xin
    4) Rb - X -> Y              | RFout DSTsel SUB Yin
    5) END                      | TCend

0x1: @Ra Rb:
    3)

0x2: #N Rb: Rb - #N -> Y
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) M[MAR] -> MDR            | MDRen MEMsel
    5) MDR -> X                 | MDRen WRsel
    6) Rb - X -> Y              | SUB Yin
    7) END                      | TCend

0x3: N Rb:
    3)
```
