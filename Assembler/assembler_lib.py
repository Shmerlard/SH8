import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Control_logic_Programmer.sh8constants as sh8cons

COMMENT_CHAR = '%'
MAX_REGISTER = 16
MAX_IMM = 65536

LINE_NUMBER = "Line_number"
LABEL = "Label"
CONTENT = "Content"
LENGTH = "Length"
IS_EMPTY = "Is_empty"
ADDRESS = "Line_address"

ORG = ".org"
saved_words = [
    ORG,
    "dw"
]

code_types = [
    "SAVED_WORD",
    "LABEL",
    "INSTRUCTION",
    "COMMENT",
    "REGISTER",
    "IMM_HEX",
    "IMM_DEC",
    "LABEL_REF"
]
REGISTER = "REG"
IMMEDIATE = "IMM"
LABEL_REF = "LABEL_REF"
DIRECT_REF = "DIR_REF"

args_types = [
    IMMEDIATE,
    REGISTER,
    LABEL_REF,
    DIRECT_REF
]
# returns a label for a line if it has one, None if not
def get_label(line_num: int, line: str):
    word = line.split()[0]

    if (word in saved_words) or (word in sh8cons.instructionSet) or (word in sh8cons.simulated_instructions): return None
    if (word.endswith(":")):
        return {
            LABEL: word[:-1],
            LINE_NUMBER: line_num,
            ADDRESS: None
        }
    raise Exception(f'Label Error in line number {line_num}maybe {word} is not a valid command')



def line_process(line_num: int, line: str, labels):
    if len(line) == 0:
        return {
            "Line_number": line_num,
            "Is_empty": True
        }

    label = get_label(line_num, line)
    if label is not None:
        line = line.split(None, 1)[1]
    content = content_process(line_num, line, labels)

    if (content["INSTRUCTION"] == ".org"):
        return {
            LINE_NUMBER: line_num,
            ADDRESS: content["ARGUEMENT_1"],
            CONTENT: content,
            LENGTH: 0,
            IS_EMPTY: False
        }
    length = get_instruction_length(content)

    return {
        LINE_NUMBER: line_num,
        LABEL: label,
        CONTENT: content,
        LENGTH: length,
        IS_EMPTY: False,
        ADDRESS: None
    }

def content_process(line_num: int, content: str, labels):
    arr = content.split()

    if (len(arr) >= 4):
        raise Exception(f'{content} in line number {line_num} is too long')

    cont_inst = None
    cont_arg_1 = None
    cont_arg_2 = None

    if (not is_valid_inst(arr[0])):
        raise Exception(f"{content} in line number {line_num} doesn't have a valid instruction")
    cont_inst = arr[0]

    if (cont_inst == ORG):
        return{
            "INSTRUCTION": cont_inst,
            "ARGUEMENT_1": int(arr[1], 16),
            "ARGUEMENT_2": None
        }
    try:
        cont_arg_1 = get_arg_type(line_num, arr[1], labels)
    except IndexError:
        pass

    try:
        cont_arg_2 = get_arg_type(line_num, arr[2], labels)
    except IndexError:
        pass


    return {
        "INSTRUCTION": cont_inst,
        "ARGUEMENT_1": cont_arg_1,
        "ARGUEMENT_2": cont_arg_2
    }

def get_instruction_length(content: dict):
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    arg_1_imm = False if content["ARGUEMENT_1"] is None or content["ARGUEMENT_1"][0] != IMMEDIATE else True
    arg_2_imm = False if content["ARGUEMENT_2"] is None or content["ARGUEMENT_2"][0] != IMMEDIATE else True

    arg_1_labref = False if content["ARGUEMENT_1"] is None or content["ARGUEMENT_1"][0] != LABEL_REF else True
    arg_2_labref = False if content["ARGUEMENT_2"] is None or content["ARGUEMENT_2"][0] != LABEL_REF else True
    if arg_1_imm or arg_2_imm:
        return 2
    if arg_1_labref or arg_2_labref:
        return 2
    return 1



def is_valid_inst(inst: str):
    if (inst in sh8cons.simulated_instructions) or (inst in sh8cons.instructionSet) or (inst in saved_words):
        return True
    return False


def get_arg_type(line_num, arg: str, labels: list):
    register = is_register(line_num, arg)
    if register[0]:
        return (register[1], register[2])

    imm = is_imm(line_num, arg)
    if (imm[0]):
        return (IMMEDIATE, imm[1])

    label_ref = is_label_ref(line_num, arg, labels)
    if (label_ref[0]):
        return (LABEL_REF, label_ref[1])

    raise Exception(f'unknown arguemnt {arg} in line number {line_num}')



def is_label_ref(line_num: int, lab: str, labels: list[str]):
    for label in labels:
        if lab == label[LABEL]: return(True, lab)
    return (False, None)

def is_imm(line_num, imm: str):
    if (imm[0] == '#'):
        try:
            x = int(imm[1:])
        except ValueError:
            try:
                x = int(imm[1:], 16)
            except Exception:
                raise Exception(f'Immediate value {imm} in line number {line_num} is invalid')
        if x > MAX_IMM:
            raise Exception(f'Immediate value {imm} in line number {line_num} is too big')
        return (True, x)
    return (False, None)

# returns a tuple that indicates when the arguement is a register, an indirect register
# and the register value
def is_register(line_num, reg: str):
    type = REGISTER
    if (reg[0] == '@'):
        reg = reg[1:]
        type = DIRECT_REF
    if (reg[0] == 'R') and (reg[1:].isdigit()):
        if int(reg[1:]) < MAX_REGISTER: return (True, type, int(reg[1:]))
        raise Exception(f'Register Too big in line number: {line_num}')
    return (False, type, None)

def is_valid_address(word: str, line_num: int):
    try:
        word = int(word, 16)
    except Exception:
        raise Exception(f'{word} at line {line_num} is invalid')
    return (True, word)


# removes comments
def remove_comments(lines: list[str]):
    arr = []
    for line in lines:
        line = line.strip()
        first_occ = line.find('%')
        if first_occ == -1:
            arr.append(line)
            continue
        arr.append(line[:first_occ])
    return arr




def get_origin(line_num: str, line: int):
    arr = line.split()
    word = arr[0]
    if (word == ORG):
        if (len(arr) == 2) and is_valid_address(arr[1], line_num)[0]:  # add valid address
            return (line_num, int(arr[1], 16))
        raise Exception(f"origin error at line: {line_num}")
    return False


# returns a list of all of the labels, and raise an Exception if a label is defined twice
def find_labels_and_orgs(lines: list):
    labels = []
    orgs = []
    for line_num, line in enumerate(lines):
        if (len(line) == 0): continue
        origin = get_origin(line_num, line)
        if (origin is not False):
            orgs.append(origin)
            continue

        label = get_label(line_num, line)
        if label is None: continue
        if label in labels: raise Exception("Assembler Error!, duplicate declaration of labels")

        labels.append(label)

    return labels, orgs
