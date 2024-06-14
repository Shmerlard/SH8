# The instruction register

## Instruction format
The instruction register is a 16-bit register
```
the format is XXXX-XAAA-SSSS-DDDD
X = the opcode of the instruction
A = indicates the addressing mode 
S = indicates the source register
D = indicates the destination register
```

## Addressing modes 
```
000: Ra  Rb  | Reg - Reg Addressing            | Ra -> Rb
001: Ra  @Rb | Reg - Indirect Addressing       | R[Ra] -> M[Rb]
010: @Ra Rb  | Indirect - Reg Addressing       | M[Ra] -> Rb
011: @Rb @Rb | Indirect - Inderect Addressing  | M[Ra] -> M[Rb]
100: #N  Rb  | Immediate - Register Addressing | N -> Rb
101: #N  @Rb | Immediate - Indirect Addressing | N -> M[Rb]
110: N   Rb  | Direct - Register Addressing    | M[N] -> Rb
111: Ra  N   | Register - Direct Addressing    | Ra -> M[N]
```
### how fetching is obtained?
```
T0) PC    -> MAR; PC++  | PCout, MARin, PCinc
T1) M[MA] -> MD         | MDRen, MEMsel, 
T2) MD    -> IR         | MDRen, IRin WRsel
```

### RTN
```
(Rx)  Referce to the data inside register x
(M[Rx]) Referce to the data at the with the address Rx

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
#### NOP 
```
4) END
```
