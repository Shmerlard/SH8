from sh8lib import *

ctrlTest = [
    "PCin",
    "DSTsel"
]
print(ctrl_lines_to_binary(ctrlTest))

test = "PCin DSTsel Yin"
print(ctrl_lines_to_binary(line_to_list_of_strings(test)))