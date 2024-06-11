# The instruction register

## Instruction format
The instruction register is a 16-bit register
```
the format is XXXX-XSSS-AABB-FDDD
X = the opcode of the instruction
S = indicates the source register
A = indicates the addressing mode of the source
B = indicates the addressing mode of the destination
D = indicates the destination register

the following addressing modes are available:
00: Registor mode    | MOV R2,R3
01: Indirect mode    | MOV @R3,@R4
10: Immediate mode   | MOV #42,R1
11: UNUSED (maybe use of offset or auto increment)
```

### how fetching is obtained?
```
1) PC    -> MAR; PC++  | PCout, MARin, PCinc
2) M[MA] -> MD         | MDRwe, Msel, ??? depends on mem module
3) MD    -> IR         | MDRoe, IRin
```

#### NOP 
```
4) END
```
#### MOV
```
if Ra, Rb:
4) Ra -> Y              | RFrd, Yin, Y=B
5) Y  -> Rb             | RFwr, DSTsel, Yout, END

if #,  Rb:
4) PC -> MAR; PC++      | PCout, MARwr, PCinc
5) M[MA] -> MD          | MEMsel, MDRin
6) MD -> Rb             | MDRout, DSTsel, IRin,END

if @Ra,Rb:
4) Ra -> MAR
5) M[MA] -> MD
6) MD -> Rb

if @Ra, @Rb
4) Ra -> MAR
5) M[MA] -> MD; #might reduce if MAR is master-slave
6) Ra -> MAR
7) MD - M[MA]

if Ra, @Rb
4) Rb -> MAR
5) Ra -> MD
6) MD -> M[MAR]
```