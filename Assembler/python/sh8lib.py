from sh8constants import *

# returns a code for every string
def get_code_array_from_line(line: str, lineNum: int = 0):
    # Splitting the string to an array of ctrl lines and removing commas
    line = line.replace(',', '')
    arr = line.split()
    
    # validating that the line and translating alu instructions
    for item in arr:
        if item in allCtrlLines:
            if item in aluCtrlLines:
                inx = aluCtrlLines.index(item)
                matching = []
                if inx % 2 == 1: matching.append("ALUctrl[0]")
                if (inx>>1) % 2 == 1: matching.append("ALUctrl[1]")
                if (inx>>2) % 2 == 1: matching.append("ALUctrl[2]")
                if (inx>>3) % 2 == 1: matching.append("ALUctrl[3]")
                arr += matching
                arr.remove(item)
            else:
                break
        else: 
            raise Exception(f'the control line "{item}" not found in line number {lineNum}')
    
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
        with open(f'out{count}.txt','w+') as outfile:
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