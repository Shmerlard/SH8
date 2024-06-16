from sh8lib import *
import os, sys

microcode = pd.read_excel('../Microcode.xlsx')
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
write_to_file_from_array(Arr)
