# The condition logic

the condition logic control wheter the condition is satisfied or not:
the condition is a 3bit value.

```text
the condition format is XYZ
X - if 1: <
Y - if 1: =
Z - if 1: >
```

```text
0b000:     - dont jump              # a better solution need to be implemented
0b001: JH  - jump if higher
0b010: JEQ - jump if equal
0b011: JHS - jump if higher or same
0b100: JL  - jump if lower
0b101: JNE - jump if not equal
0b110: JLS - jump if lower or same
0b111: JMP - always jump
```
