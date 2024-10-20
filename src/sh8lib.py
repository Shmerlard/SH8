import sh8constants as sh8cons
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from instructions import instructions

# returns a code for every string
def get_code_array_from_line(line: str, lineNum: int = 0):
    # Splitting the string to an array of ctrl lines and removing commas
    if (line == "NOP"): return [0, 0, 0]

    line = line.replace(',', '')
    arr = line.split()
    # validating that the line and translating alu instructions
    for item in arr:
        if item in sh8cons.aluCtrlLines:
            inx = sh8cons.aluCtrlLines.index(item)
            matching = []
            if inx % 2 == 1: matching.append("ALUctrl[0]")
            if (inx >> 1) % 2 == 1: matching.append("ALUctrl[1]")
            if (inx >> 2) % 2 == 1: matching.append("ALUctrl[2]")
            if (inx >> 3) % 2 == 1: matching.append("ALUctrl[3]")
            arr += matching
            arr.remove(item)

    # returning an array with 3 elements with the code for each eeprom
    output = []
    for ctrl in sh8cons.ctrlLines:
        tmp = 0
        for i in range(len(arr)):
            for j in range(len(ctrl)):
                if arr[i] == ctrl[j]:
                    tmp = tmp + (1 << j)
        output.append(tmp)
    return output

# matches the address to the line
def get_address_from_input(con: bool,
                           sc: bool,
                           mode: int,
                           opcode: int,
                           time: int):
    addr = 0
    addr = addr + (con    << sh8cons.CON_SHIFT_AMOUNT)
    addr = addr + (sc     << sh8cons.SC_SHIFT_AMOUNT)
    addr = addr + (mode   << sh8cons.ADDR_MODE_SHIFT_AMOUNT)
    addr = addr + (opcode << sh8cons.OPCODE_SHIFT_AMOUNT)
    addr = addr + time
    return addr

# create a file with the format for each array
def write_to_file_from_array(arr_of_arr: list, path_to_outfiles_dir: str):
    for count, arr in enumerate(arr_of_arr):
        outfile_path = os.path.join(path_to_outfiles_dir, f'out{count}.txt')
        with open(outfile_path, 'w+') as outfile:
            outfile.write("v3.0 hex words addressed\n")
            for i in range(sh8cons.ADDRESS_COUNT):
                if(i % 16 == 0):
                    outfile.write(f'{i:04x}: ')
                if(i % 16 != 15):
                    outfile.write(f'{arr[i]:02x} ')
                else:
                    outfile.write(f'{arr[i]:02x}\n')
        print(f'out{count}.txt is done')
    print("all done!")

def get_opcode_from_instruction(st: str, lineNum: int = 0):
    inst = instructions.get(st)
    if inst is None:
        raise Exception(f'The instruction {st} in line {lineNum} is invalid')
    return inst.get("OPCODE")


def get_valid_row_from_row(row: pd.Series, lineNum: int = 0):
    opcode = None if pd.isna(row.iloc[0]) else int(get_opcode_from_instruction(row.iloc[0]), 16)
    mode = None if pd.isna(row.iloc[1]) else int(row.iloc[1])
    time = None if pd.isna(row.iloc[2]) else int(row.iloc[2])
    con = None if pd.isna(row.iloc[3]) else int(row.iloc[3])
    sc = None if pd.isna(row.iloc[4]) else int(row.iloc[4])
    arr = [con, sc, mode, opcode, time]

    if pd.isna(row.iloc[5]):
        if all(v is None for v in arr):
            return -1
        raise Exception(f'the control lines {row[5]} at line:{lineNum} are invalid')
    else:
        arr.append(get_code_array_from_line(row.iloc[5]))
    return arr


def write_to_arrays_from_address(input: list, arr_of_arrays: list):
    con, sc, mode, opcode, time, data = input
    conList = [0, 1] if con is None else [con]
    scList = [0, 1]  if sc is None else [sc]
    modeList = [*range(sh8cons.ADDR_MODE_COUNT)] if mode is None else [mode]
    opcodeList = [*range(sh8cons.OPCODE_COUNT)] if opcode is None else [opcode]
    timeList = [*range(sh8cons.TC_T_COUNT)] if time is None else [time]

    for conItem in conList:
        for scItem in scList:
            for modeItem in modeList:
                for opcodeItem in opcodeList:
                    for timeItem in timeList:
                        addressItem = get_address_from_input(conItem, scItem, modeItem, opcodeItem, timeItem)
                        for inx, arr in enumerate(arr_of_arrays):
                            arr[addressItem] = data[inx]

# noqa
