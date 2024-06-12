#### MOV
```
0: Ra Rb:
4) Ra -> Y              | RFrd, Yin, Y=B
5) Y  -> Rb             | RFwr, DSTsel, Yout, END

1: Ra @Rb:
4) Rb -> MAR
5) Ra -> MD
6) MD -> M[MAR]

2: @Ra Rb:
4) Ra -> MAR
5) M[MA] -> MD
6) MD -> Rb

3: @Ra @Rb
4) Ra -> MAR
5) M[MA] -> MD; #might reduce if MAR is master-slave
6) Ra -> MAR
7) MD - M[MA]

4: #N Rb:
4) PC -> MAR; PC++      | PCout, MARwr, PCinc
5) M[MA] -> MD          | MEMsel, MDRin
6) MD -> Rb             | MDRout, DSTsel, IRin,END

5: #N, @Rb:
4) PC -> MAR; PC++
5) M[MAR] -> MD; Rb -> MAR*
6) MD -> M[MAR]
(^) caution: MAR has to be Master slave

6: N, Rb:
4) PC -> MAR; PC++
5) M[MAR] -> MD
6) MD -> MAR
7) M[MAR] -> MD
8) MD -> Rb

7: Ra, N:
4) PC -> MAR; PC++
5) M[MAR] -> MD
6) MD -> MAR
7) Ra -> MD
8) MD -> M[MAR]
```