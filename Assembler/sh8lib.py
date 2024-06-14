ctrlLines = [
    "PCin",
    "PCout",
    "PCinc",
    "RFin",
    "RFout",
    "DSTsel",
    "IRin",
    "IRout",
    "Yin",
]

def ctrl_lines_to_binary(arr: list):
    output = 0
    for i in range(len(arr)):
        for j in range(len(ctrlLines)):
            if arr[i] == ctrlLines[j]:
                output = output + (1<<j)
    return output

def line_to_list_of_strings(line: str):
    return line.split()

##def file_to_binary('')