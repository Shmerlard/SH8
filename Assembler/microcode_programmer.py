import pandas as pd
from sh8lib import *

check = 3
microcode = pd.read_excel('Microcode.xlsx')
rowsNum, colNum = microcode.shape
# print(microcode)
# print(rowsNum,colNum)
empty_arr = [0] * (LAST_ADDRESS + 1)
for rowIdx in range(rowsNum):
    row = microcode.iloc[rowIdx]
    if row[0] == "nan":
        opcodeItem = None
    else:
        opcodeItem = row[0]
    opcodeItem = None if pd.isna(row[0]) else row[0]
    modeItem = None if pd.isna(row[1]) else row[1]
    timeItem = None if pd.isna(row[2]) else row[2]
    conItem = None if pd.isna(row[3]) else row[3]
    scItem = None if pd.isna(row[4]) else row[4]
    line = [] if pd.isna(row[5]) else row[5]
    data = str_to_bin(line,check) 
    write_to_array_from_address(empty_arr, conItem, scItem, modeItem, opcodeItem, timeItem, data)
write_to_file_from_array(empty_arr)