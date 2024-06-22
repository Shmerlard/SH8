# SUB

```text
0x0: Ra Rb: (Rb - Ra -> Rb)
    3) Rb -> X          | RFout DSTsel Xin
    4) X - Ra -> Y      | RFout SUB Yin
    5) Y -> Rb          | Yout RFin DSTsel

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

0x6: #N, Rb: (CMP #N Rb) Rb - #N -> Y
    3) PC -> MAR; PC++          | PCout PCinc MARin
    4) Rb -> X; M[MAR] -> MD    | RFout DSTsel Xin MDRen MEMsel
    5) X - MD -> Y              | SUB Yin RFout MDRen WRsel

0x7: Rb - Ra -> Y (CMP Ra Rb)
    3) Rb -> X          | RFout DSTsel Xin
    4) X - Ra -> Y      | RFout SUB Yin
```
