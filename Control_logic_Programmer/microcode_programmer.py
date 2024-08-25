import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sh8lib
import sh8constants


script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, 'Microcode.xlsx')

# Read the Excel file using the constructed path
microcode = sh8lib.pd.read_excel(excel_path)
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
sh8lib.write_to_file_from_array(Arr, f'{script_dir}/outfiles')
