# The register File

the register file contains the following registers:
```
0   : SP        : The stack pointer is an 8-bit register for
                  Holding the current address of the stack.
                  we only need 8-bit and not 16 because of
                  the way we arrange the stack in the memory

1-4 : REG A-D   : 4 general purpose 8-bit registers.
5-6 : REG L,H   : 2 8-bit registers for the MAR since we only 
                  have 8-bit bus for a 16-bit addresses.
7   : REG F     : The flags register containing the 4 following flags:
                  (C) the carry flag 
                  (Z) the zero flag 
                  (N) the negative flag
                  (V) the overflow flag
```

