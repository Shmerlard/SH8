from sh8lib import *

microcode = pd.read_excel('/home/elad/Desktop/elad/SH8/Assembler/Microcode.xlsx')
rowsNum, colNum = microcode.shape

arr0 = [0] * (ADDRESS_COUNT)
arr1 = [0] * (ADDRESS_COUNT)
arr2 = [0] * (ADDRESS_COUNT)
arr3 = [0] * (ADDRESS_COUNT)

Arr = [arr0, arr1, arr2, arr3]

for rowIdx in range(rowsNum):
    row = microcode.iloc[rowIdx]
    row = get_valid_row_from_row(row,rowIdx)
    if row == -1:
        continue
    write_to_arrays_from_address(row,Arr)
    # print(get_valid_row_from_row(row))
    # print(row)
    # print(type(row))
write_to_file_from_array(Arr)


# print(get_opcode_from_instruction("RRC"))
#     opcodeItem = None if pd.isna(row[0]) else int(get_opcode_from_instruction(row[0]))
#     modeItem = None if pd.isna(row[1]) else int(row[1])
#     timeItem = None if pd.isna(row[2]) else int(row[2])
#     conItem = None if pd.isna(row[3]) else int(row[3])
#     scItem = None if pd.isna(row[4]) else int(row[4])
#     line = [] if pd.isna(row[5]) else row[5]

#     data = str_to_bin(line,check) 
#     write_to_array_from_address(empty_arr, conItem, scItem, modeItem, opcodeItem, timeItem, data)
# write_to_file_from_array(empty_arr)