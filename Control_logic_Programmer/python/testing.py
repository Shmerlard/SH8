import sh8lib
import sh8constants
import os
import sys

current_file_directory = os.path.dirname(os.path.abspath(__file__))

microcode = sh8lib.pd.read_excel('../Microcode.xlsx')
rowsNum, colNum = microcode.shape

arr0 = [0] * (sh8constants.ADDRESS_COUNT)
arr1 = [0] * (sh8constants.ADDRESS_COUNT)
arr2 = [0] * (sh8constants.ADDRESS_COUNT)

Arr = [arr0, arr1, arr2]

for rowIdx in range(rowsNum):
    row = microcode.iloc[rowIdx]
    row = sh8lib.get_valid_row_from_row(row, rowIdx)
    if row == -1:
        continue
    sh8lib.write_to_arrays_from_address(row, Arr)
sh8lib.write_to_file_from_array(Arr)