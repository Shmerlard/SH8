# The register File

the register file contains the following registers:
```
0   : SP        | The stack pointer is a 16-bit register for
                  Holding the current address of the stack.

1   : SR REG    | Status register contains the following from LSB to MSB
                  0: (C) Carry flag
                  1: (Z) Zero flag
                  2: (N) Negative flag
                  3: (E) Even flag

2-3 : INPUT OUTPUT REGISTERS

4-15: GP Registers
```
