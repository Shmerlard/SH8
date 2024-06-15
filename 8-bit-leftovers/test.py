from sh8lib import *

ctrlTest = [
    "PCin",
    "DSTsel",
    "MEMsel",
    "Yout",
    "Yin",
    "OR",
]
# str1 = "Yin DSTsel OR RFout"
# print(str1)
# arr1 = line_to_list_of_strings(str1)
# print(arr1)
# arr2 = ctrl_lines_from_list(arr1)
# # print(arr2)
# # arr3 = ctrl_lines_to_binary(arr2)
# # print(arr3)
# # h_arr3 = [hex(num) for num in arr3]
# print(h_arr3)
# # print(hex(59))

# print(get_address_from_input(True,True,7,31,15))
empty_arr = [0] * (LAST_ADDRESS + 1 )
write_to_array_from_address(empty_arr,None,None,None,None,None,5)
print(empty_arr)
write_to_file_from_array(empty_arr)
