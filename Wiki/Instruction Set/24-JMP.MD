# JMP

&&&&&& need to add addrssing modes for single operand

```text
0: Ra Rb    |
    3) PC -> MAR        | PCout MARin
    4) M[MAR] -> MDR    | MDRen MEMsel 
    5) MDR -> PC        | MDRen WRsel PCin
    6) END              | TCend

1: Ra @Rb   | 
    3)

2: @Ra Rb   |
    3)

3: @Ra @Rb  |
    3)

4: #N Rb    |
    3)

5: #N, @Rb  |
    3)

6: N, Rb    |
    3)

7: Ra, N    |
    3)
```
