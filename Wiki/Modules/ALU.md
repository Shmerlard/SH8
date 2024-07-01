# The ALU

The ALU is the unit performing arithmetic and logical operations.
the ALU also contains 2 registers, X and Y. X is for the input, Y is for the output.
i used 4 74ls181 chips for the alu, but since the chip doesnt have a shifting mechanic another one is used.
in

the alu has the folowing control lines:

```text
0x0: ADD
0x1: ADDC
0x2: SUB
0x3: NOT
0x4: XOR
0x5: Y=B
0x6: AND
0x7: OR
0x8: SHR
0x9: SHRC
0xA: Y=X
0xB: INCX
0xC: DECX
```

according to the [datasheet](/Datasheets/74181.pdf) we are going to need the following:

```text
0x0: ADD : F = A PLUS  B       : S = 0x9; M = 0; ALU_Carry_EN = 0
0x1: ADDC: F = A PLUS  B PLUS C: S = 0x9; M = 0; ALU_CArry_EN = 1
0x2: SUB : F = A MINUS B       : S = 0x6; M = 0; ALU_CARRY_EN = 0
0x3: NOT : F = NOT B           : S = 0x5; M = 1;
0x4: XOR : F = A XOR   B       : S = 0x6; M = 1;
0x5: Y=B : F = B               : S = 0xA; M = 1;
0x6: AND : F = AB              : S = 0xB; M = 1;
0x7: OR  : F = A OR    B       : S = 0xE; M = 1;
0x8: SHR : Shift right         : S = 0xF; M = 1; SH_EN = 1; CYC_EN = 0
0x9: SHRC: Shift right cyclic  : S = 0xF; M = 1; SH_EN = 1; CYC_EN = 1
0xA: Y=A :                     : S = 0xF; M = 1; SH_EN = 0;
0xB: Y=INCX:                    : S = 0x0; M = 0; SH_EN = 0; %  CARRY_EN = 0 
0xC: Y=DECX:                    : S = 0xF; M = 0; SH_EN = 0; CARRY_EN = 0
```

## the shifting mechanic
