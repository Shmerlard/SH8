ctrlLines_EEPROM0 = [
    "PCin",
    "PCout",
    "PCinc",
    "RFin",
    "RFout",
    "DSTsel",
    "IRin",
    "IRout"
]
ctrlLines_EEPROM1 = [
    "MARin",
    "MDRen",
    "WRsel",
    "MEMsel",
    "TCend",
    "GOTO6",
    "HLT",
    "UNDEFINED17"
]
ctrlLines_EEPROM2 = [
    "Xin",
    "Yin",
    "Yout",
    "ALUctrl[0]",
    "ALUctrl[1]",
    "ALUctrl[2]",
    "ALUctrl[3]",
    "UNDEFINED27"
]
ctrlLines_EEPROM3 = [
    "RST_EN",
    "IN_REG",
    "OUT_REG",
    "CONin",
    "SCld",
    "SCdec",
    "UNDEFINED36",
    "UNDEFINED37"
]

ctrlLines = [
    ctrlLines_EEPROM0,
    ctrlLines_EEPROM1,
    ctrlLines_EEPROM2,
    ctrlLines_EEPROM3
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
    "NOP",
    "MOV",
    "LD",
    "ST",
    "PUSH",
    "POP",
    "ADD",
    "ADDC",
    "SUB",
    "SHR",
    "RRC",
    "CALL",
    "RET",
    "CMP",
    "UNDEFINED14",
    "UNDEFINED15",
    "UNDEFINED16",
    "AND",
    "OR",
    "XOR",
    "NOT",
    "IOR",
    "IOW",
    "UNDEFINED23",
    "JMP",
    "JEQ",
    "JNE",
    "JHS",
    "JH",
    "JLS",
    "JL",
    "UNDEFINED31"

]

ADDR_MODE_COUNT = 8
OPCODE_COUNT = 32
TC_T_COUNT = 16

CON_SHIFT_AMOUNT = 13
SC_SHIFT_AMOUNT = 12
ADDR_MODE_SHIFT_AMOUNT = 9
OPCODE_SHIFT_AMOUNT = 4

ADDRESS_COUNT = 32768