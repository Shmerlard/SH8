import assembler_lib as aslib
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    filename = sys.argv[1]

    print(f"opening {filename}...")
    with open(filename) as code_file:

        # spliting lines
        lines = code_file.read().splitlines()
        print(lines)

        # removing comments
        lines = aslib.remove_comments(lines)
        print(lines)

        print("finding labels and origins")
        labels, orgs = aslib.find_labels_and_orgs(lines)
        print(labels, orgs)

        print("calculating labels adresses and instructions length")
        current_address = 0
        address_shift = 0
        rem_orgs = orgs
        for line_num, line in enumerate(lines):
            line = aslib.line_process(line_num, line, labels)

            if line[aslib.IS_EMPTY]: continue

            if rem_orgs and line_num == rem_orgs[0][0]:
                current_address = rem_orgs[0][1]
                rem_orgs.pop(0)

            address_shift = line[aslib.LENGTH]
            line[aslib.ADDRESS] = current_address
            current_address += address_shift

        print(lines)




if __name__ == "__main__":
    main()
