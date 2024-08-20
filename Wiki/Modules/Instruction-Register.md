# The instruction register

The instruction register is a 16-bit register

## Instruction format

there is only one type of instruction formats
```text
the format is XXXX-AUMM-SSSS-DDDD
X = the opcode of the instruction
A = indicates if instrucion is alternate
U = Currently not in use
M = indicates the addressing mode
S = indicates the source register
D = indicates the destination register
```

## Addressing modes

each addressing mode is represented by 2 bits for a total of 4 adressing modes for each type
there are 3 types of addressing modes

### Type 1 addressing mods
this type is used by `MOV`,`AND`,`OR`,`XOR`,`SHR`,`RRC`, `ADD`,`ADDC` and SUB.

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
0x2: #N  @Rb            | ST #N #K: #N -> M[#K]
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
^note 2: the `POP N` is implemented in the CPU as `RET`.

### how fetching is obtained?

```text
T0) PC     -> MAR; PC++  | PCout, MARin, PCinc
T1) M[MAR] -> MDR        | MDRen, MEMsel, 
T2) MDR    -> IR         | MDRen, IRin WRsel
```

## Altenate mode
WIP

### RTN

```text
(Rx)  Refers to the data inside register x
(M[Rx]) Refers to the data at the with the address Rx

(A ->  B) A is moving to B
(A &   B) A bitwise AND B
(A ||  B) A bitwise OR B
(NOT A  ) A bitwise NOT
(A XOR B) A bitwise XOR B
(A >>  B) A is shifted right bitwise B times (MSB of A becomes 0 each shift)
(A <<  B) A is shifted left bitwise B times (LSB of A becomes 0 each shift)
(A RR  B) A is rotated right B times
(A RL  B) A is rotated left B times

```
