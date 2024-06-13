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
1) PC    -> MAR; PC++  | PCout, MARin, PCinc
2) M[MA] -> MD         | MDRwe, Msel, ??? depends on mem module
3) MD    -> IR         | MDRoe, IRin
```

#### NOP 
```
4) END
```
