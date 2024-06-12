#### MOV
```
if Ra, Rb: (0x0)
4) Ra -> Y              | RFrd, Yin, Y=B
5) Y  -> Rb             | RFwr, DSTsel, Yout, END

if Ra, @Rb (0x1)
4) Rb -> MAR
5) Ra -> MD
6) MD -> M[MAR]

if @Ra,Rb: (0x4)
4) Ra -> MAR
5) M[MA] -> MD
6) MD -> Rb

if @Ra, @Rb (0x5)
4) Ra -> MAR
5) M[MA] -> MD; #might reduce if MAR is master-slave
6) Ra -> MAR
7) MD - M[MA]

if #,  Rb:  (0x8)
4) PC -> MAR; PC++      | PCout, MARwr, PCinc
5) M[MA] -> MD          | MEMsel, MDRin
6) MD -> Rb             | MDRout, DSTsel, IRin,END

if #, @Rb: (0x9)
```