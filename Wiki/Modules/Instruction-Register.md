# The instruction register

The instruction register is a 16-bit register

## Instruction format

there is only one type of instruction formats
```text
the format is XXXX-XUMM-SSSS-DDDD
X = the opcode of the instruction
U = Currently not in use
M = indicates the addressing mode
S = indicates the source register
D = indicates the destination register
```

## Addressing modes

each addressing mode is represented by 2 bits for a total of 4 adressing modes for each type
there are 4 types of addressing modes

### Type 0 addressing mod
this type is used by `NOP`, `HLT`, `RET`
they dont have any arguements

### Type 1 addressing mod
this type is used by `MOV`,`AND`,`OR`,`XOR`,`SHR`,`RRC`, `ADD`,`ADDC`, `SUB` and `CMP`.

```text
0x0: Ra  Rb             | MOV Ra  Rb: Ra    -> Rb
0x1: @Ra Rb             | MOV @Ra Rb: M[Ra] -> Rb
0x2: #N  Rb             | MOV #N  Rb: #N    -> Rb
0x3: N   Rb             | MOV N   Rb: M[N]  -> Rb
```

### Type 2 addressing mods
this type is used by `ST`

```text
0x0: Ra  @Rb            | ST Ra @Rb: Ra -> M[Rb]
0x1: Ra  #N             | ST Ra #N: Ra -> M[#N]
0x2: #N  @Rb            | ST #N @Rb: #N -> M[M[Rb]]
0x3: Ra  N              | ST Ra N: Ra -> M[M[#N]]
```

### Type 3 addressing mods
this type is used by `PUSH`,`POP`,`CALL` and `JMP`

```text
0x0: Ra                 | POP Ra: @SP -> Ra
0x1: @Ra                | POP @Ra: @SP -> @Ra
0x2: #N                 | POP #N: @SP -> M[#N]
0x3: N                  | PUSH N: M[M[#N]] -> @SP
```
^note 1: in the examples above there are also `SP++` steps which I didnt include here.

### how fetching is obtained?

```text
T0) PC     -> MAR; PC++  | PCout, MARin, PCinc
T1) M[MAR] -> MDR        | MDRen, MEMsel, 
T2) MDR    -> IR         | MDRen, IRin WRsel
```
