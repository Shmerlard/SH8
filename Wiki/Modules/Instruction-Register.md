# The instruction register

The instruction register is a 16-bit register

## Instruction format

there are 2 types of instruction formats one is for 1 operand and the other is for 2 operands

### Type 1 format

```text
the format is XXXX-SSSS-FFFF-FFFF
X = the opcode of the instruction
S = indicates the source register
F = UNUSED
```

### Type 2 format

```text
the format is XXXX-SSSS-FAAA-DDDD
X = the opcode of the instruction
S = indicates the source register
A = indicates the addressing mode
D = indicates the destination register
F = UNUSED
```

## Addressing modes

```text
000: Ra  Rb  | Reg - Reg Addressing            | Ra -> Rb
001: Ra  @Rb | Reg - Indirect Addressing       | R[Ra] -> M[Rb]
010: @Ra Rb  | Indirect - Reg Addressing       | M[Ra] -> Rb
011: #N  Rb  | Immediate - Register Addressing | N -> Rb
100: #N  @Rb | Immediate - Indirect Addressing | N -> M[Rb]
101: N   Rb  | Direct - Register Addressing    | M[N] -> Rb 
110: Ra  N   | Register - Direct Addressing    | Ra -> M[N]
111: SPECIAL | depneds on the opcode
```

### how fetching is obtained?

```text
T0) PC     -> MAR; PC++  | PCout, MARin, PCinc
T1) M[MAR] -> MDR        | MDRen, MEMsel, 
T2) MDR    -> IR         | MDRen, IRin WRsel
```

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
