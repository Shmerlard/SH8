from sh8lib import *

arr0 = [0] * ADDRESS_COUNT
arr1 = [1] * ADDRESS_COUNT
arr2 = [15] * ADDRESS_COUNT
arr3 = [255] * ADDRESS_COUNT
arr = [arr0,arr1,arr2,arr3]
#write_to_file_from_array(arr)
st = "MDRen, RFout"
print(get_code_array_from_line(st))