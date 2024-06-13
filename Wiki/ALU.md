# The ALU

the alu has the folowing control lines:
```
0:  ADD
1:  SUB
2:  NOT
3:  XOR
4:  Y=B
5:  AND
6:  OR
```
according to the [datasheet](/Datasheets/74181.pdf) we are going to need the following:
```
ADD: F = A PLUS  B : S = 0x9; M = 0; 
SUB: F = A MINUS B : S = 0x6; M = 0; Cin = 0
NOT: F = NOT B     : S = 0x5; M = 1;
XOR: F = A XOR   B : S = 0x6; M = 1;
Y=B: F = B         : S = 0xA; M = 1;
AND: F = AB        : S = 0xB; M = 1;
OR : F = A OR    B : S = 0xE; M = 1;
```