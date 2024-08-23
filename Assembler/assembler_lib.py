import sys
import copy
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
DW = 'dw'
saved_words = [
    ORG,
    DW
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
INSTRUCTION = "INST"
INSTRUCTION_TYPE = "INSTRUCTION_TYPE"
ARG_1 = "ARGUEMENT_1"
ARG_2 = "ARGUEMENT_2"

IMMEDIATE_PARAM = "IMM_PAR"         # for example: MOV #0x2312 R1
IMMEDIATE_VALUE = "IMM_VAL"         # for example: DW 0x2312
LABEL_REF = "LABEL_REF"             # for example: CALL FUNC
DIRECT_REF = "DIR_REF"              # for example: PUSH @R1
REGISTER = "REG"                    # for example: MOV R2 R5

registers = {
    "SP": 0,
    "SR": 1,
    "IN": 2,
    "OUT": 3
}

args_types = [
    IMMEDIATE_PARAM,
    IMMEDIATE_VALUE,
    LABEL_REF,
    DIRECT_REF,
    REGISTER
]

SAVED_WORD = "SAVED_WORD"
SIMULATED_INST = "SIMULATED_INST"
ALTERNATE_INST = "ALTERNATE_INST"
REGULAR_INST = "REGULAR_INST"

instruction_types = [
    SAVED_WORD,
    SIMULATED_INST,
    ALTERNATE_INST,
    REGULAR_INST
]

OPCODE_INST_SHIFT_AMOUNT = 12
ALTERNATE_INST_SHIFT_AMOUNT = 11
ADDRESSING_MODE_INST_SHIFT_AMOUNT = 8
SRC_REG_INST_SHIFT_AMOUNT = 4
DST_REG_INST_SHIFT_AMOUNT = 0

# removes comments and tabs
def remove_comments(lines: list[str]):
    arr = []
    for line in lines:
        # line = line.expandtabs(1)
        # line = line.strip()
        line = " ".join(line.split())
        first_occ = line.find('%')
        if first_occ == -1:
            arr.append(line)
            continue
        arr.append(line[:first_occ].strip())
    return arr


# returns a label for a line if it has one, None if not
def get_label(line_num: int, line: list):
    word = line[0]

    if is_valid_inst(word): return None
    if (word.endswith(":")):
        return {
            LABEL: word[:-1],
            LINE_NUMBER: line_num,
            ADDRESS: None
        }
    raise Exception(f'Label Error in line number {line_num}maybe {word} is not a valid command')


def line_process(line_num: int, line: str, labels: list, address: int):
    line = line.split()
    if len(line) == 0:
        return {
            "Line_number": line_num,
            "Is_empty": True
        }

    line_label = get_label(line_num, line)
    if line_label is not None:
        line_label[ADDRESS] = address
        line.pop(0)
    # content = content_process(line_num, line, labels)

    if not line:
        raise Exception(f'error at line number {line_num + 1} only label')

    valid_inst = is_valid_inst(line[0])
    if (valid_inst):
        line_instruction = line[0]                  # the string, ex: 'MOV'
        line_instruction_type = valid_inst[1]       # the type, ex: 'REGULAR_INST'
        line.pop(0)

    line_arg_1 = None
    line_arg_2 = None
    if line:
        line_arg_1 = get_arg_type(line_num, line[0], labels)
        line.pop(0)
    if line:
        line_arg_2 = get_arg_type(line_num, line[0], labels)
        line.pop(0)
    if line:
        raise Exception(f'too many arguemnts in line number {line_num}')

    line_length = get_instruction_length(line_instruction, line_arg_1, line_arg_2)

    return {
        LINE_NUMBER: line_num,
        LABEL: line_label,
        INSTRUCTION: line_instruction,
        INSTRUCTION_TYPE: line_instruction_type,
        ARG_1: line_arg_1,
        ARG_2: line_arg_2,
        LENGTH: line_length,
        IS_EMPTY: False,
        ADDRESS: address
    }


# to be deleted
def content_process(line_num: int, content: str, labels):
    arr = content.split()

    if (len(arr) >= 4):
        raise Exception(f'{content} in line number {line_num} is too long')

    cont_inst = None
    cont_inst_type = is_valid_inst(arr[0])
    cont_arg_1 = None
    cont_arg_2 = None
    if (not cont_inst_type):
        raise Exception(f"{content} in line number {line_num} doesn't have a valid instruction")
    cont_inst = arr[0]

    try:
        cont_arg_1 = get_arg_type(line_num, arr[1], labels)
    except IndexError:
        pass

    try:
        cont_arg_2 = get_arg_type(line_num, arr[2], labels)
    except IndexError:
        pass


    return {
        INSTRUCTION: cont_inst,
        INSTRUCTION_TYPE: cont_inst_type[1],
        "ARGUEMENT_1": cont_arg_1,
        "ARGUEMENT_2": cont_arg_2
    }


def get_instruction_length(inst: str, arg_1, arg_2):
    if inst == ORG:
        return 0

    if inst == DW:
        return 1        # to be changed when i will add support for arrays
    arg_1_long = False
    arg_1_long = True if (arg_1 is not None) and ((arg_1[0] == IMMEDIATE_PARAM) or (arg_1[0] == LABEL_REF) or (arg_1[0] == IMMEDIATE_VALUE)) else False
    arg_2_long = True if (arg_2 is not None) and ((arg_2[0] == IMMEDIATE_PARAM) or (arg_2[0] == LABEL_REF) or (arg_2[0] == IMMEDIATE_VALUE)) else False

    if arg_1_long or arg_2_long:
        return 2
    return 1


def get_arg_type(line_num, arg: str, labels: list):
    register = is_register(line_num, arg)
    if register[0]:
        return (register[1], register[2])

    imm = is_imm(line_num, arg)
    if (imm[0]):
        return (imm[1], imm[2])

    label_ref = is_label_ref(line_num, arg, labels)
    if (label_ref[0]):
        return (LABEL_REF, label_ref[1])

    raise Exception(f'unknown arguemnt {arg} in line number {line_num}')


def is_valid_inst(inst: str):
    if (inst in sh8cons.simulated_instructions):
        return (True, SIMULATED_INST)
    if (inst in sh8cons.instructionSet):
        return (True, REGULAR_INST)
    if (inst in saved_words):
        return (True, SAVED_WORD)
    if (inst in sh8cons.alternative_instructions):
        return (True, ALTERNATE_INST)
    return False


def is_label_ref(line_num: int, lab: str, labels: list[str]):
    for label in labels:
        if lab == label[LABEL]: return(True, lab)
    return (False, None)


def is_imm(line_num, imm: str):
    arg_type = IMMEDIATE_VALUE
    base = 10

    if (imm[0] == '#'):
        arg_type = IMMEDIATE_PARAM
        imm = imm[1:]
    if (imm.startswith('0x')): base = 16
    try:
        x = int(imm, base)
    except ValueError:
        return (False, None)
    if x > MAX_IMM:
        raise Exception(f'Immediate value {imm} in line number {line_num} is too big')
    return (True, arg_type, x)


# returns a tuple that indicates when the arguement is a register, an indirect register
# and the register value
def is_register(line_num, reg: str):
    arg_type = REGISTER
    if (reg[0] == '@'):
        reg = reg[1:]
        arg_type = DIRECT_REF
    if (reg[0] == 'R') and (reg[1:].isdigit()):
        if int(reg[1:]) < MAX_REGISTER: return (True, arg_type, int(reg[1:]))
        raise Exception(f'Register Too big in line number: {line_num}')
    if (reg in registers.keys()):
        return (True, arg_type, registers.get(reg))
    return (False, arg_type, None)


def is_valid_address(word: str, line_num: int):
    try:
        word = int(word, 16)
    except Exception:
        raise Exception(f'{word} at line {line_num} is invalid')
    return (True, word)


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

        label = get_label(line_num, line.split())
        if label is None: continue
        if label in labels: raise Exception("Assembler Error!, duplicate declaration of labels")

        labels.append(label)

    return (labels, orgs)


def get_processed_lines(lines: list[str], labels: list, orgs: list):
    current_address = 0
    address_shift = 0
    rem_orgs = copy.deepcopy(orgs)
    processed_lines = []
    for line_num, line in enumerate(lines):
        if rem_orgs and line_num == rem_orgs[0][0]:
            current_address = rem_orgs[0][1]
            rem_orgs.pop(0)

        line = line_process(line_num, line, labels, current_address)

        if line[IS_EMPTY]: continue

        address_shift = line[LENGTH]
        # line[ADDRESS] = current_address
        # if line[LABEL] is not None:
        #     line[LABEL][ADDRESS] = current_address

        current_address += address_shift
        processed_lines.append(line)

    return processed_lines


def get_instruction_code(line_num: int, instruction: tuple, arg_1: tuple, arg_2: tuple):
    inst_name = instruction[0]
    inst_type = instruction[1]

    if inst_name == ORG:
        return []
    if inst_name == DW:
        return [arg_1[1]]

    if (inst_type == SIMULATED_INST) or (inst_type == ALTERNATE_INST):
        inst_name, arg_1, arg_2 = get_real_instruction(inst_name, arg_1, arg_2)
    opcode = sh8cons.instructionSet.index(inst_name)
    alternate = True if inst_type == ALTERNATE_INST else False
    addressing_mode = get_addressing_mode(inst_name, arg_1, arg_2)
    source_reg, dest_reg = get_src_dst_regs(inst_name, arg_1, arg_2)

    code = 0
    code = code + (opcode << OPCODE_INST_SHIFT_AMOUNT)
    code = code + (alternate << ALTERNATE_INST_SHIFT_AMOUNT)
    code = code + (addressing_mode << ADDRESSING_MODE_INST_SHIFT_AMOUNT)
    code = code + (source_reg << SRC_REG_INST_SHIFT_AMOUNT)
    code = code + (dest_reg << DST_REG_INST_SHIFT_AMOUNT)

    imm = get_imm_code(arg_1, arg_2)
    if imm is None:
        return [code]
    return [code, imm]

# translates between the real instruction and the simulated ones
def get_real_instruction(instruction_name: str, arg_1: tuple, arg_2: tuple):
    if instruction_name == "HLT":
        return "OR", (IMMEDIATE_VALUE, 0x0010), (REGISTER, 0x1)

def get_addressing_mode(instruction_name: str, arg_1: tuple, arg_2: tuple):
    pass

def get_src_dst_regs(instruction_name: str, arg_1: tuple, arg_2: tuple):
    pass

def get_imm_code(arg_1: tuple, arg_2: tuple):
    pass

def get_jmp_command(instruction_name: str):
    pass
