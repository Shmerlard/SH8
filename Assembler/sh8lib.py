from sh8const import *
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

def str_to_bin(line: str, eeprom: int):
    arr = line_to_list_of_strings(line)
    arr = ctrl_lines_from_list(arr)
    arr = ctrl_lines_to_binary(arr)
    return arr[eeprom]

######
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

def write_to_file_from_array(arr: list):
    with open("out.txt",'w+') as outfile:
        outfile.write("v3.0 hex words addressed\n")
        for i in range(LAST_ADDRESS + 1):
            if(i % 16 == 0):
                outfile.write(f'{i:04x}: ')
            outfile.write(f'{arr[i]:04x} ')
            if(i % 16 == 15):
                outfile.write("\n")

def write_to_array_from_address(arr: list,
                                con: bool,
                                sc: bool,
                                mode: int,
                                opcode: int,
                                time: int,
                                data):
    if con == None: conList = [0,1]
    else: conList = [con]
    if sc == None: scList = [0,1]
    else: scList = [sc]
    if mode == None: modeList = [*range(ADDR_MODE_MAX+1)]
    else: modeList = [mode]
    if opcode == None: opcodeList = [*range(OPCODE_MAX + 1)]
    else: opcodeList = [opcode]
    if time == None: timeList = [*range(TC_T_MAX + 1)]
    else: timeList = [time]
    for conItem in conList:
        for scItem in scList:
            for modeItem in modeList:
                for opcodeItem in opcodeList:
                    for timeItem in timeList:
                        addressItem = get_address_from_input(conItem,scItem,modeItem,opcodeItem,timeItem)
                        arr[addressItem] = data
