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

# return the binary coded for 
def ctrl_lines_to_binary(arr: list):
    output = [];
    for ctrl in ctrlLines:
        tmp = 0;
        for i in range(len(arr)):
            for j in range(len(ctrl)):
                if arr[i] == ctrl[j]:
                    tmp = tmp + (1<<j)

        output.append(tmp)
    return output

# return a list from string
def line_to_list_of_strings(line: str):
    return line.split()

# return the matching alu ctrl lines 
def get_matching_ctrl_lines_from_string(st: str):
    matching = []
    try: 
        inx = aluCtrlLines.index(st)
    except:
        return -1
    else:
        if inx % 2 == 1: matching.append("ALUctrl[0]")
        if (inx>>1) % 2 == 1: matching.append("ALUctrl[1]")
        if (inx>>2) % 2 == 1: matching.append("ALUctrl[2]")
        if (inx>>3) % 2 == 1: matching.append("ALUctrl[3]")
    return  matching

# gets a list of ctrl lines and replaces alu ctrllines
def ctrl_lines_from_list(arr:list):
    for item in arr:
        tmp = get_matching_ctrl_lines_from_string(item)
        if tmp == -1: continue
        arr = arr + get_matching_ctrl_lines_from_string(item)
        arr.remove(item)
    return arr

def get_address_from_input(con: bool,
                           sc: bool,
                           mode: int,
                           opcode: int,
                           time: int):
    addr = 0
    addr = addr + (con<<13)
    addr = addr + (sc<<12)
    addr = addr + (mode<<9)
    addr = addr + (opcode<<4)
    addr = addr + time
    return addr