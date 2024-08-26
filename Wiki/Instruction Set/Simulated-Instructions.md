# Simulated instructions

```text
HLT -> OR #0x0010 SR

Set Stack Pointer
SSP #N -> MOV #N SP

CLEAR E/N/Z/C bit
CLRC -> XOR #0x0001 SR
CLRZ -> XOR #0x0002 SR
CLRN -> XOR #0x0003 SR
CLRE -> XOR #0x0004 SR

SET E/N/Z/C bit
SETC -> OR #0x0001 SR
SETZ -> OR #0x0002 SR
SETN -> OR #0x0003 SR
SETE -> OR #0x0004 SR
```
