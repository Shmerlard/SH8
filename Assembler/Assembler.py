import assembler_lib as aslib
import os
import sys
import copy

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

script_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    filename = sys.argv[1]

    input_dir = os.path.dirname(os.path.abspath(filename))
    output_filename = os.path.splitext(os.path.basename(filename))[0] + '.txt'
    output_path = os.path.join(input_dir, output_filename)

    print(f"Opening {filename}...", end="\n\n")
    with open(filename) as code_file:

        # spliting lines
        print("Splitting line:")
        lines = code_file.read().splitlines()
        print(lines, end="\n\n")

        # removing comments
        print("Removing comments and tabs:")
        lines = aslib.remove_comments(lines)
        print(lines, end="\n\n")

        # findings the labels and origins
        print("Finding labels and origins:")
        labels, orgs = aslib.find_labels_and_orgs(lines)
        print(labels, orgs, end="\n\n")

        print("Processing labels adresses and instructions length:")
        processed_lines = aslib.get_processed_lines(lines, labels, orgs)
        print(processed_lines, end="\n\n")

        print("Turning processed lines into machine code:")
        machine_code = aslib.get_machine_code(processed_lines, labels, orgs)
        aslib.write_to_file_from_array(machine_code, output_path)
        # print(machine_code, end="\n\n")


if __name__ == "__main__":
    main()
