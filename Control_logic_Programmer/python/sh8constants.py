ctrlLines_EEPROM0 = [
    "PCin",
    "PCout",
    "PCinc",
    "RFin",
    "RFout",
    "DSTsel",
    "IRin",
    "Vout"
]
ctrlLines_EEPROM1 = [
    "MARin",
    "MDRen",
    "WRsel",
    "MEMsel",
    "TCend",
    "GOTO6",
    "SCld",
    "SCdec"
]
ctrlLines_EEPROM2 = [
    "Xin",
    "Yin",
    "Yout",
    "ALUctrl[0]",
    "ALUctrl[1]",
    "ALUctrl[2]",
    "ALUctrl[3]",
    "CONin"
]

ctrlLines = [
    ctrlLines_EEPROM0,
    ctrlLines_EEPROM1,
    ctrlLines_EEPROM2,
]

allCtrlLines = []
for c in ctrlLines:
    allCtrlLines += c

aluCtrlLines = [
    "ADD",
    "ADDC",
    "SUB",
    "NOT",
    "XOR",
    "Y=B",
    "AND",
    "OR",
    "SHR",
    "SHRC",
    "Y=X",
    "INCX",
    "DECX"
]

instructionSet = [
    "MOV",
    "PUSH",
    "POP",
    "ADD",
    "ADDC",
    "SUB",
    "SHR",
    "RRC",
    "CALL",
    "RET",
    "AND",
    "OR",
    "XOR",
    "IOR",
    "IOW",
    "JMP",
]

ADDR_MODE_COUNT = 8
OPCODE_COUNT = 16
TC_T_COUNT = 16

CON_SHIFT_AMOUNT = 12
SC_SHIFT_AMOUNT = 11
ADDR_MODE_SHIFT_AMOUNT = 8
OPCODE_SHIFT_AMOUNT = 4

ADDRESS_COUNT = 32768