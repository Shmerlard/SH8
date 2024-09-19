import sys
import copy
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from instructions import instructions
import Control_logic_Programmer.sh8constants as sh8cons
import assembler_constants as ascon


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

INSTRUCTION = "INST"

TYPE_REGISTER = "REG"                    # for example: MOV R2 R5
# TYPE_INDIRECT_REG = "INDIRECT_REG"            # for example: PUSH @R1
TYPE_IMM = "IMM_PAR"         # for example: MOV #0x2312 R1
TYPE_LABEL_IMM = "IMM_LABEL_REF"         # for example: CALL #Func
TYPE_INDIRECT_LABEL = "INDIRECT_LABEL_REF"    # for example: CALL Func

TYPE_IMM_VALUE = "IMM_VAL"         # for example: DW 0x2312

registers = {
    "SP": 0,
    "SR": 1,
    "IN": 2,
    "OUT": 3
}

SAVED_WORD = "SAVED_WORD"
REGULAR_INST = "REGULAR_INST"

OPCODE_INST_SHIFT_AMOUNT = 11
ADDRESSING_MODE_INST_SHIFT_AMOUNT = 8
SRC_REG_INST_SHIFT_AMOUNT = 4
DST_REG_INST_SHIFT_AMOUNT = 0

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




# ################################################# STEP 3 ##############
def find_labels_and_orgs(lines: list):
    labels = {}
    orgs = []
    for line_num, line in enumerate(lines):
        if (len(line) == 0): continue
        origin = get_origin(line_num, line)
        if (origin is not False):
            orgs.append(origin)
            continue

        label = get_label(line_num, line.split())
        if label.get(LABEL) is None: continue
        # if label in labels: raise Exception(f"Assembler Error in line {line_num + 1}: duplicate declaration of labels")

        labels.update({label[LABEL]: None})

    return (labels, orgs)


def get_origin(line_num: str, line: int):
    arr = line.split()
    word = arr[0]
    if (word == ORG):
        if (len(arr) == 2) and is_valid_address(arr[1], line_num)[0]:  # add valid address
            return (line_num, int(arr[1], 16))
        raise Exception(f"origin error at line: {line_num + 1}")
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
    raise Exception(f'Label Error in line number {line_num + 1}maybe {word} is not a valid command')




# ################################################## STEP 4 ##############
def get_processed_lines(lines: list[str], labels: dict, orgs: list):
    current_address = 0
    address_shift = 0
    rem_orgs = copy.deepcopy(orgs)
    processed_lines = []
    for line_num, line in enumerate(lines):
        if rem_orgs and (line_num == rem_orgs[0][0]):
            current_address = rem_orgs[0][1]
            rem_orgs.pop(0)

        line = line_process(line_num, line, labels, current_address)

        if line.get(IS_EMPTY): continue

        address_shift = line[LENGTH]
        current_address += address_shift
        processed_lines.append(line)

    return processed_lines


def line_process(line_num: int, line: str, labels: dict, address: int) -> dict:
    line = line.split()
    if len(line) == 0:
        return {
            "Line_number": line_num,
            "Is_empty": True
        }

    line_label = get_label(line_num, line)
    if line_label.get(LABEL) is not None:
        labels.update({line_label.get(LABEL): address})
        # labels[labels.index(line_label)][ADDRESS] = address
        line.pop(0)

    if not line:
        raise Exception(f'error at line number {line_num + 1} only label')

    # Instrcution handling
    line_instruction = line[0]
    instruction_data = instructions.get(line_instruction)  # a dictionary conatining data
    if instruction_data is None:
        raise Exception(f'Assembler error in line number {line_num + 1}: instruction {line_instruction} is invalid')

    opcode = instruction_data.get(ascon.OPCODE)
    line_instruction_category = instruction_data.get(ascon.CATEGORY)
    line_instruction_type = instruction_data.get(ascon.TYPE)
    line.pop(0)

    # arguements handling
    line_arg_1 = None
    line_arg_2 = None

    if line:
        line_arg_1 = get_arg_type(line_num, line[0], labels)
        line.pop(0)
    if line:
        line_arg_2 = get_arg_type(line_num, line[0], labels)
        line.pop(0)
    if line:
        raise Exception(f'Assembler Error in line {line_num + 1}: Too many arguements')

    src_reg = instruction_data.get(ascon.SRC_REG)
    dst_reg = instruction_data.get(ascon.DST_REG)
    if (src_reg is None) and (dst_reg is None):
        src_reg = line_arg_1
        dst_reg = line_arg_2
    elif (src_reg is None) and (dst_reg is not None):
        dst_reg = get_implicit_register(dst_reg)
        src_reg = line_arg_1
    elif (src_reg is not None) and (dst_reg is None):
        src_reg = get_implicit_register(src_reg)
        dst_reg = line_arg_1
    else:
        src_reg = get_implicit_register(src_reg)
        dst_reg = get_implicit_register(dst_reg)

    # length handlign
    line_length = get_instruction_length(line_instruction, src_reg, dst_reg)

    return {
        LINE_NUMBER: line_num,
        LABEL: line_label.get(LABEL),
        INSTRUCTION: line_instruction,
        ascon.CATEGORY: line_instruction_category,
        ascon.SRC_REG: src_reg,
        ascon.DST_REG: dst_reg,
        ascon.ARG_1: line_arg_1,
        ascon.ARG_2: line_arg_2,
        ascon.TYPE: line_instruction_type,
        LENGTH: line_length,
        ascon.ADDRESS: address,
        ascon.OPCODE: opcode,
    }

def get_implicit_register(reg: str) -> dict:
    if reg == '@0':
        return ascon.IND_SP
    else:
        return {
            ascon.TYPE: ascon.TYPE_DIR_REG,
            ascon.REG_VAL: int(reg)
        }

def is_valid_inst(inst: str):
    if inst in instructions:
        return instructions.get(inst).get(ascon.CATEGORY)
    return False


def get_arg_type(line_num: int, arg: str, labels: list) -> dict:
    is_regi = is_register(line_num, arg)
    if is_regi[0]:
        return {
            ascon.TYPE: is_regi[1],
            ascon.REG_VAL: is_regi[2],
            ascon.IMM_VAL: None
        }

    imm = is_imm(line_num, arg)
    if (imm[0]):
        return {
            ascon.TYPE: imm[1],
            ascon.REG_VAL: 0,
            ascon.IMM_VAL: imm[2]
        }

    label_ref = is_label_ref(line_num, arg, labels)
    if (label_ref[0]):
        return {
            ascon.TYPE: label_ref[1],
            ascon.REG_VAL: 0,
            ascon.IMM_VAL: label_ref[2]
        }

    raise Exception(f'unknown arguemnt {arg} in line number {line_num + 1}')


def is_label_ref(line_num: int, lab: str, labels: dict):
    arg_type = ascon.TYPE_IND_LBL
    if (lab[0] == '#'):
        arg_type = ascon.TYPE_DIR_LBL
        lab = lab[1:]

    for label in labels.keys():
        if lab == label: return(True, arg_type, lab)
    return (False, arg_type, None)

# returns a tuple that indicates when the arguement is a register, an indirect register
# and the register value
def is_register(line_num, reg: str):
    arg_type = ascon.TYPE_DIR_REG
    if (reg[0] == '@'):
        reg = reg[1:]
        arg_type = ascon.TYPE_IND_REG
    if (reg[0] == 'R') and (reg[1:].isdigit()):
        if int(reg[1:]) < MAX_REGISTER: return (True, arg_type, int(reg[1:]))
        raise Exception(f'Register Too big in line number: {line_num + 1}')
    if (reg in registers.keys()):
        return (True, arg_type, registers.get(reg))
    return (False, arg_type, None)

def is_imm(line_num, imm: str):
    arg_type = ascon.TYPE_DIR_IMM  # maybe add type_ind_imm
    base = 10

    if (imm[0] == '#'):
        arg_type = ascon.TYPE_DIR_IMM
        imm = imm[1:]

    if (imm.startswith('0x')): base = 16
    try:
        x = int(imm, base)
    except ValueError:
        return (False, None)
    if x > MAX_IMM:
        raise Exception(f'Immediate value {imm} in line number {line_num + 1} is too big')
    return (True, arg_type, x)


def get_instruction_length(inst: str, arg_1: dict, arg_2: dict) -> int:
    if inst == ORG:
        return 0

    if inst == DW:
        return 1        # to be changed when i will add support for arrays
    arg_1_long = True if (arg_1 is not None) and (arg_1.get("IMM_VAL") is not None) else False
    arg_2_long = True if (arg_2 is not None) and (arg_2.get("IMM_VAL") is not None) else False

    if (arg_1_long or arg_2_long):
        return 2
    return 1


def is_valid_address(word: str, line_num: int):
    try:
        word = int(word, 16)
    except Exception:
        raise Exception(f'{word} at line {line_num + 1} is invalid')
    return (True, word)




# ################################################# STEP 5 ##############
def get_machine_code(processed_lines: dict, labels: list, orgs: list[tuple]):
    machine_code = [0] * sh8cons.ROM_ADDRESS_COUNT
    for p_line in processed_lines:
        line_code, line_address = get_processed_line_code(p_line, labels)
        while(line_code):
            machine_code[line_address] = line_code.pop(0)
            line_address += 1

    return machine_code



# input: processed line, output: (line_code, line address)
# line_code: a list of the codes to insert
# line_address: the address of the first code
def get_processed_line_code(p_line: dict, labels: dict) -> tuple:
    inst_name = p_line.get(INSTRUCTION)
    inst_type = p_line.get(ascon.TYPE)
    src_reg = p_line.get(ascon.SRC_REG)
    dst_reg = p_line.get(ascon.DST_REG)
    line_num = p_line.get(LINE_NUMBER)


    x = src_reg.get(ascon.IMM_VAL) if (src_reg is not None) else None
    if (type(x) is not int) and (x is not None):
        new_address = labels.get(x)
        src_reg.update({ascon.IMM_VAL: new_address})

    x = dst_reg.get(ascon.IMM_VAL) if (dst_reg is not None) else None
    if (type(x) is not int) and (x is not None):
        new_address = labels.get(x)
        dst_reg.update({ascon.IMM_VAL: new_address})

    p_line_address = p_line.get(ascon.ADDRESS)


    if inst_name == ORG:
        return ([], None)
    if inst_name == DW:
        return ([src_reg.get(ascon.IMM_VAL)], p_line_address)



    opcode = int(p_line.get(ascon.OPCODE), 16)
    src_dst_type = (src_reg.get(ascon.TYPE), dst_reg.get(ascon.TYPE))
    arg_1_arg_2_type = (p_line.get(ascon.ARG_1), p_line.get(ascon.ARG_2))
    p_line_ad_mode = get_addressing_mode(line_num, inst_type, src_dst_type, arg_1_arg_2_type)
    # source_reg, dest_reg = get_src_dst_regs(inst_name, arg_1, arg_2)
    #
    code = 0
    code = code + (opcode << OPCODE_INST_SHIFT_AMOUNT)
    code = code + (p_line_ad_mode << ADDRESSING_MODE_INST_SHIFT_AMOUNT)
    code = code + (src_reg.get(ascon.REG_VAL) << SRC_REG_INST_SHIFT_AMOUNT)
    code = code + (dst_reg.get(ascon.REG_VAL) << DST_REG_INST_SHIFT_AMOUNT)

    imm = get_imm_code(src_reg.get(ascon.IMM_VAL), dst_reg.get(ascon.IMM_VAL))
    if imm is None:
        return ([code], p_line_address)
    return ([code, imm], p_line_address)
    #

def get_addressing_mode(line_num: int, instruction_type: int, src_dst_type: tuple, arg_1_arg_2_type: tuple):

    exc_err = f'Error at line number {line_num + 1}'

    match instruction_type:
        case 0:
            return 0
        case 1:
            if src_dst_type[1] != ascon.TYPE_DIR_REG:
                raise Exception(exc_err, ' type 1 instructions must have direct register as destination, use ST instead')
            match src_dst_type[0]:
                case ascon.TYPE_DIR_REG:
                    return 0
                case ascon.TYPE_IND_REG:
                    return 1
                case ascon.TYPE_DIR_IMM:
                    return 2
                case ascon.TYPE_IND_LBL:
                    return 3
                case _:
                    raise Exception(exc_err)
        case 2:
            match src_dst_type:
                case (ascon.TYPE_DIR_REG, ascon.TYPE_IND_REG):
                    return 0
                case (ascon.TYPE_DIR_REG, ascon.TYPE_DIR_IMM):
                    return 1
                case (ascon.TYPE_DIR_IMM, ascon.TYPE_IND_REG):
                    return 2
                case (ascon.TYPE_DIR_REG, ascon.TYPE_IND_LBL):
                    return 3
                case _:
                    raise Exception(exc_err)
        case 3:
            match arg_1_arg_2_type[0].get(ascon.TYPE):
                case ascon.TYPE_DIR_REG:
                    return 0
                case ascon.TYPE_IND_REG:
                    return 1
                case ascon.TYPE_DIR_IMM:
                    return 2
                case ascon.TYPE_DIR_LBL:
                    return 2
                case ascon.TYPE_IND_LBL:
                    return 3
                case _:
                    raise Exception(exc_err)
        case _:
            raise Exception(exc_err)


def get_imm_code(arg_1: int | None, arg_2: int | None):
    if arg_1 is not None:
        return arg_1
    elif arg_2 is not None:
        return arg_2
    else:
        return None

def write_to_file_from_array(arr: list, outfile_path: str):
    with open(outfile_path, 'w+') as outfile:
        outfile.write("v3.0 hex words addressed\n")
        for i in range(sh8cons.ROM_ADDRESS_COUNT):
            if(i % 16 == 0): outfile.write(f'{i:04x}: ')
            if(i % 16 != 15): outfile.write(f'{arr[i]:04x} ')
            else: outfile.write(f'{arr[i]:04x}\n')
    print("all done!")

