from sh8constants import *
import pandas as pd

# returns a code for every string
def get_code_array_from_line(line: str, lineNum: int = 0):
    # Splitting the string to an array of ctrl lines and removing commas
    line = line.replace(',', '')
    arr = line.split()
    
    # validating that the line and translating alu instructions
    for item in arr:
        if item in aluCtrlLines:
            inx = aluCtrlLines.index(item)
            matching = []
            if inx % 2 == 1: matching.append("ALUctrl[0]")
            if (inx>>1) % 2 == 1: matching.append("ALUctrl[1]")
            if (inx>>2) % 2 == 1: matching.append("ALUctrl[2]")
            if (inx>>3) % 2 == 1: matching.append("ALUctrl[3]")
            arr += matching
            arr.remove(item)
            ## break

        #else: 
        #    raise Exception(f'the control line "{item}" not found in line number {lineNum}')
    
    # returning an array with 4 elements with the code for each eeprom
    output = []
    for ctrl in ctrlLines:
        tmp = 0
        for i in range(len(arr)):
            for j in range(len(ctrl)):
                if arr[i] == ctrl[j]:
                    tmp = tmp + (1<<j)
        output.append(tmp)
    
    return output

# matches the address to the line
def get_address_from_input(con: bool,
                           sc: bool,
                           mode: int,
                           opcode: int,
                           time: int):
    addr = 0
    addr = addr + (con    << CON_SHIFT_AMOUNT)
    addr = addr + (sc     << SC_SHIFT_AMOUNT)
    addr = addr + (mode   << ADDR_MODE_SHIFT_AMOUNT)
    addr = addr + (opcode << OPCODE_SHIFT_AMOUNT)
    addr = addr + time
    return addr

# create a file with the format for each array
def write_to_file_from_array(arr_of_arr: list):
    for count, arr in enumerate(arr_of_arr):
        with open(f'outfiles/out{count}.txt','w+') as outfile:
            outfile.write("v3.0 hex words addressed\n")
            for i in range(ADDRESS_COUNT):
                if(i % 16 == 0):
                    outfile.write(f'{i:04x}: ')
                if(i % 16 != 15):
                    outfile.write(f'{arr[i]:02x} ')
                else:
                    outfile.write(f'{arr[i]:02x}\n')
        print(f'out{count}.txt is done')
    print("all done!")

def get_opcode_from_instruction(st: str,lineNum: int = 0):
    try: 
        inx = instructionSet.index(st)
    except:
        raise Exception(f'The instruction {st} in line {lineNum} is invalid')
    else:
        return inx


def get_valid_row_from_row(row: pd.Series, lineNum: int = 0):
    opcode = None if pd.isna(row[0]) else int(get_opcode_from_instruction(row[0]))
    mode = None if pd.isna(row[1]) else int(row[1])
    time = None if pd.isna(row[2]) else int(row[2])
    con = None if pd.isna(row[3]) else int(row[3])
    sc = None if pd.isna(row[4]) else int(row[4])
    
    arr = [con, sc, mode, opcode, time]

    if pd.isna(row[5]):
        if all(v is None for v in arr):
            return -1
        raise Exception(f'the control lines {row[5]} at line:{lineNum} are invalid')
    else:
        arr.append(get_code_array_from_line(row[5]))
    return arr 


def write_to_arrays_from_address(input: list, arr_of_arrays: list):
    con, sc, mode, opcode, time, data = input
    conList = [0,1] if con == None else [con]
    scList = [0,1]  if sc  == None else [sc]
    modeList = [*range(ADDR_MODE_COUNT)] if mode == None else [mode]
    opcodeList = [*range(OPCODE_COUNT)] if opcode == None else [opcode]
    timeList = [*range(TC_T_COUNT)] if time == None else [time]

    for conItem in conList:
        for scItem in scList:
            for modeItem in modeList:
                for opcodeItem in opcodeList:
                    for timeItem in timeList:
                        addressItem = get_address_from_input(conItem,scItem,modeItem,opcodeItem,timeItem)
                        for inx, arr in enumerate(arr_of_arrays):
                            arr[addressItem] = data[inx]
