SIMULATED_INST = "SIMULATED"

OPCODE = "OPCODE"
ADDRESS = "ADDRESS"
CATEGORY = "CATEGORY"
TYPE = "TYPE"
SRC_REG = "SRC_REG"
DST_REG = "DST_REG"
ARG_1 = "ARG_1"
ARG_2 = "ARG_2"
NUM_ARGS = "NUM_ARGS"

# types of arguements
TYPE_DIR_REG = "T_DIR_REG"          # PUSH R1
TYPE_IND_REG = "T_IND_REG"          # PUSH @R1
TYPE_DIR_IMM = "T_DIR_IMM"          # PUSH #0x523
TYPE_DIR_LBL = "T_DIR_LBL"          # CALL #FUNC
TYPE_IND_LBL = "T_IND_LBL"          # PUSH num1

IMM_VAL = "IMM_VAL"
REG_VAL = "REG_VAL"
LONG_ARG = "LONG_ARG"

IND_SP = {
    TYPE: TYPE_IND_REG,
    REG_VAL: 0,
}

"""
arguement = {
    TYPE: ~~~,
    REG_VAL: ~~~,
    IMM_VAL: ~~~k
}
"""
# arguements = {
#     "arg_1": {
#         "TYPE": None,
#         "REG_VAL": None,
#         "LONG": False
#     },
#     "arg_2": {
#         "TYPE": None,
#         "REG_VAL": None,
#         "LONG": False
#     },
# }
