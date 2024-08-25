import pandas as pd
import os
import numpy as np
import json
import sys


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(script_dir, 'Instructions.xlsx')
    file_name = sys.argv[1]
    print(file_name)
    df = pd.read_excel(excel_path, dtype='object')
    df.replace({np.nan: None}, inplace=True)
    rows_num, col_num = df.shape
    instructions = {}
    for row_index in range(rows_num):
        row = df.iloc[row_index]
        if (row[0] is None): continue
        s = row[1:]
        s = s.dropna()
        instructions[row[0]] = s.to_dict()

    with open(f'{file_name}.py', 'w+') as outfile:
        # print(json.dumps(instructions, indent=4), file=outfile)
        outfile.write(f"instructions = {json.dumps(instructions, indent=4)}")
    print(df)
    print(instructions)


if __name__ == "__main__":
    main()
