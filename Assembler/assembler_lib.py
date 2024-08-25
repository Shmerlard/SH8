import sys
import copy
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Control_logic_Programmer.sh8constants as sh8cons
import assembler_constants as ascon
from instructions import instructions

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

INSTRUCTION = "INST"
INSTRUCTION_TYPE = "INSTRUCTION_TYPE"
ARG_1 = "ARGUEMENT_1"
ARG_2 = "ARGUEMENT_2"

TYPE_REGISTER = "REG"                    # for example: MOV R2 R5
TYPE_INDIRECT_REG = "INDIRECT_REG"            # for example: PUSH @R1
TYPE_IMM = "IMM_PAR"         # for example: MOV #0x2312 R1
TYPE_LABEL_IMM = "IMM_LABEL_REF"         # for example: CALL #Func
TYPE_INDIRECT_LABEL = "INDIRECT_LABEL_REF"    # for example: CALL Func

TYPE_IMM_VALUE = "IMM_VAL"         # for example: DW 0x2312

arguements_types = {
    TYPE_REGISTER: {},
    TYPE_INDIRECT_REG: {},
    TYPE_IMM: {"LONG": True},
    TYPE_LABEL_IMM: {"LONG": True},
    TYPE_INDIRECT_LABEL: {"LONG": True}
}

registers = {
    "SP": 0,
    "SR": 1,
    "IN": 2,
    "OUT": 3
}

args_types = [
    TYPE_IMM,
    TYPE_IMM_VALUE,
    TYPE_LABEL_IMM,
    TYPE_INDIRECT_LABEL,
    TYPE_INDIRECT_REG,
    TYPE_REGISTER
]

long_arguements = [
    TYPE_IMM,
    TYPE_IMM_VALUE,
    TYPE_LABEL_IMM,
    TYPE_INDIRECT_LABEL
]

SAVED_WORD = "SAVED_WORD"
ALTERNATE_INST = "ALTERNATE_INST"
REGULAR_INST = "REGULAR_INST"

OPCODE_INST_SHIFT_AMOUNT = 12
ALTERNATE_INST_SHIFT_AMOUNT = 11
ADDRESSING_MODE_INST_SHIFT_AMOUNT = 8
SRC_REG_INST_SHIFT_AMOUNT = 4
DST_REG_INST_SHIFT_AMOUNT = 0

RET_ARG = (TYPE_INDIRECT_LABEL, 0)

TYPE_1_INST = [
    "MOV", "AND", "OR", "XOR", "SHR", "RRC", "ADD", "ADDC", "SUB"
]
TYPE_3_INST = [
    "PUSH", "POP", "CALL", "JMP"
]

script_dir = os.path.dirname(os.path.abspath(__file__))

# ############ STEP 2 ##############
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

# ############ STEP 3 ##############
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
        if label.get(LABEL) is None: continue
        if label in labels: raise Exception("Assembler Error!, duplicate declaration of labels")

        labels.append(label)

    return (labels, orgs)


def get_origin(line_num: str, line: int):
    arr = line.split()
    word = arr[0]
    if (word == ORG):
        if (len(arr) == 2) and is_valid_address(arr[1], line_num)[0]:  # add valid address
            return (line_num, int(arr[1], 16))
        raise Exception(f"origin error at line: {line_num}")
    return False


# returns a label for a line if it has one, None if not
def get_label(line_num: int, line: list):
    word = line[0]

    if is_valid_inst(word):
        return {}
    if (word.endswith(":")):
        return {
            LABEL: word[:-1],
            LINE_NUMBER: line_num,
            ADDRESS: None
        }
    raise Exception(f'Label Error in line number {line_num}maybe {word} is not a valid command')


# ############ STEP 4 ##############
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

        if line.get(IS_EMPTY): continue

        address_shift = line[LENGTH]
        current_address += address_shift
        processed_lines.append(line)

    return processed_lines


def line_process(line_num: int, line: str, labels: list, address: int):
    line = line.split()
    if len(line) == 0:
        return {
            "Line_number": line_num,
            "Is_empty": True
        }

    line_label = get_label(line_num, line)
    if line_label.get(LABEL) is not None:
        labels[labels.index(line_label)][ADDRESS] = address
        line.pop(0)

    if not line:
        raise Exception(f'error at line number {line_num + 1} only label')

    # Instrcution handling
    line_instruction = line[0]
    instruction_val = instructions.get(line_instruction)
    if instruction_val is None:
        raise Exception(f'Assembler error in line number {line_num}: instruction {line_instruction} is invalid')

    opcode = instruction_val.get(ascon.OPCODE)
    line_instruction_type = instruction_val.get(ascon.TYPE)
    line.pop(0)

    # alternate bit handling
    inst_category = instructions.get(line_instruction).get(ascon.CATEGORY)
    alternate_bit = True if inst_category == ascon.ALTERNATE_INST else False

    # arguemnts handling
    def_src_reg = {}
    line_arg_1 = {}
    line_arg_2 = {}
    if line:
        line_arg_1 = get_arg_type(line_num, line[0], labels)
        line.pop(0)
    if line:
        line_arg_2 = get_arg_type(line_num, line[0], labels)
        line.pop(0)
    if line:
        raise Exception(f'too many arguemnts in line number {line_num}')

    # src,dst reg handling


    line_length = get_instruction_length(line_instruction, line_arg_1, line_arg_2)

    return {
        LINE_NUMBER: line_num,
        LABEL: line_label.get(LABEL),
        INSTRUCTION: line_instruction.get(INSTRUCTION),
        INSTRUCTION_TYPE: line_instruction_type,
        ARG_1: line_arg_1,
        ARG_2: line_arg_2,
        LENGTH: line_length,
        ADDRESS: address,
        "OPCODE": opcode,
        "ALT_BIT": alternate_bit,
    }


def is_valid_inst(inst: str):
    if inst in instructions:
        return instructions.get(inst).get(ascon.CATEGORY)
    return False


def get_arg_type(line_num: int, arg: str, labels: list):
    is_regi = is_register(line_num, arg)
    if is_regi[0]:
        return (is_regi[1], is_regi[2])

    imm = is_imm(line_num, arg)
    if (imm[0]):
        return (imm[1], imm[2])

    label_ref = is_label_ref(line_num, arg, labels)
    if (label_ref[0]):
        return (label_ref[1], label_ref[2])

    raise Exception(f'unknown arguemnt {arg} in line number {line_num}')


def is_label_ref(line_num: int, lab: str, labels: list[str]):
    arg_type = TYPE_INDIRECT_LABEL
    if (lab[0] == '#'):
        arg_type = TYPE_LABEL_IMM
        lab = lab[1:]

    for label in labels:
        if lab == label[LABEL]: return(True, arg_type, lab)
    return (False, arg_type, None)

# returns a tuple that indicates when the arguement is a register, an indirect register
# and the register value
def is_register(line_num, reg: str):
    arg_type = TYPE_REGISTER
    if (reg[0] == '@'):
        reg = reg[1:]
        arg_type = TYPE_INDIRECT_REG
    if (reg[0] == 'R') and (reg[1:].isdigit()):
        if int(reg[1:]) < MAX_REGISTER: return (True, arg_type, int(reg[1:]))
        raise Exception(f'Register Too big in line number: {line_num}')
    if (reg in registers.keys()):
        return (True, arg_type, registers.get(reg))
    return (False, arg_type, None)

def is_imm(line_num, imm: str):
    arg_type = TYPE_IMM
    base = 10

    if (imm[0] == '#'):
        imm = imm[1:]

    if (imm.startswith('0x')): base = 16
    try:
        x = int(imm, base)
    except ValueError:
        return (False, None)
    if x > MAX_IMM:
        raise Exception(f'Immediate value {imm} in line number {line_num} is too big')
    return (True, arg_type, x)


def get_instruction_length(inst: str, arg_1, arg_2):
    if inst == ORG:
        return 0

    if inst == DW:
        return 1        # to be changed when i will add support for arrays

    # arg_1_long = True if (arg_1 is not None) and (arg_1[0] in long_arguements) else False
    # arg_2_long = True if (arg_2 is not None) and (arg_2[0] in long_arguements) else False
    arg_1_long = True if (arg_1 is not None) and (arguements_types.get(arg_1[0]).get("LONG")) else False
    arg_2_long = True if (arg_2 is not None) and (arguements_types.get(arg_2[0]) is not None) and (arguements_types.get(arg_2[0]).get("LONG")) else False
    if arg_1_long or arg_2_long:
        return 2
    return 1


def is_valid_address(word: str, line_num: int):
    try:
        word = int(word, 16)
    except Exception:
        raise Exception(f'{word} at line {line_num} is invalid')
    return (True, word)


def get_real_instruction(line_num: int, instruction_name: str, arg_1: tuple, arg_2: tuple):
    if instruction_name == "HLT":
        return "OR", (TYPE_IMM_VALUE, 0x0010), (TYPE_REGISTER, 0x1)
    if instruction_name == "NOT":
        if arg_2 is not None:
            raise Exception(f'Error at line number: {line_num}, arguement 2 is not valid for NOT instruction')
        return "XOR", (TYPE_IMM_VALUE, 0xFFFF), arg_1
    if instruction_name == "RET":
        return "POP", RET_ARG, (None, None)

# ############ STEP 5 ##############
def get_machine_code(processed_lines: list, labels: list, orgs: list[tuple]):
    machine_code = [0] * sh8cons.ROM_ADDRESS_COUNT
    for line in processed_lines:
        line_code, line_address = get_instruction_code(line)
        while(line_code):
            machine_code[line_address] = line_code[0]
            line_address += 1

    return machine_code



# input: processed line, output: (line_code, line address)
# line_code: a list of the codes to insert
# line_address: the address of the first code
def get_instruction_code(processed_line: dict):
    inst_name = processed_line[INSTRUCTION]
    inst_type = processed_line[INSTRUCTION_TYPE]
    arg_1 = processed_line[ARG_1]
    arg_2 = processed_line[ARG_2]
    address = processed_line[ADDRESS]
    line_num = processed_line[LINE_NUMBER]

    if inst_name == ORG:
        return ([], None)
    if inst_name == DW:
        return ([ARG_1], address)

    alternate = True if inst_type == ALTERNATE_INST else False
    alternate = 0
    if inst_type == ALTERNATE_INST:
        alternate = 1
        inst_name = sh8cons.alternative_instructions.get(inst_name)

    opcode = sh8cons.instructionSet.index(inst_name)
    addressing_mode = get_addressing_mode(line_num, inst_name, arg_1[0], arg_2[0])
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


def get_addressing_mode(line_number: int, instruction_name: str, arg_1_type: str | None, arg_2_type: str | None):

    exc_err = f'Error at line number {line_number}'

    if (instruction_name == "POP") and (arg_1_type == RET_ARG): return 3

    # Type 1
    elif instructions.get(instruction_name).get("Type") == 1:
        if arg_2_type != TYPE_REGISTER:
            raise Exception(exc_err + 'second arguement is valid for type 1 instruction')

        if arg_1_type == TYPE_REGISTER: return 0
        elif arg_1_type == TYPE_INDIRECT_REG: return 1
        elif arg_1_type == TYPE_IMM or arg_1_type == TYPE_LABEL_IMM: return 2
        elif arg_1_type == TYPE_INDIRECT_LABEL: return 3
        else:
            raise Exception(exc_err + " arguement 1 is invalid")

    # Type 2
    elif instruction_name == "ST":
        if arg_1_type == TYPE_REGISTER:
            if arg_2_type == TYPE_INDIRECT_REG: return 0
            elif arg_2_type == TYPE_IMM: return 1
            elif arg_2_type == TYPE_INDIRECT_LABEL: return 3
            else: raise Exception(exc_err + ' arguement is invalid for type 2 instruction')

        elif arg_1_type == TYPE_IMM:
            if arg_2_type == TYPE_INDIRECT_REG: return 2
            else: raise Exception(exc_err + ' arguemet 2 is invalid')

    # Type 3
    elif instruction_name in TYPE_3_INST:
        if arg_1_type  == TYPE_REGISTER: return 0
        elif arg_1_type == TYPE_INDIRECT_REG: return 1
        elif arg_1_type == TYPE_IMM: return 2
        elif arg_1_type == TYPE_INDIRECT_LABEL: return 3
        else: raise Exception(exc_err)

    else:
        raise Exception(exc_err)

def get_src_dst_regs(instruction_name: str, arg_1: tuple, arg_2: tuple):
    default_src_reg = instructions.get(instruction_name).get("SRC_REG")
    default_dst_reg = instructions.get(instruction_name).get("DST_REG")

    pass

def get_imm_code(arg_1: tuple, arg_2: tuple):
    pass

def get_jmp_command(instruction_name: str):
    pass

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
