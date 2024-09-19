instructions = {
    "NOP": {
        "OPCODE": "0x00",
        "CATEGORY": "REGULAR",
        "TYPE": 0,
        "NUM_ARGS": 0
    },
    "MOV": {
        "OPCODE": "0x01",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "ST": {
        "OPCODE": "0x02",
        "CATEGORY": "REGULAR",
        "TYPE": 2,
        "NUM_ARGS": 2
    },
    "PUSH": {
        "OPCODE": "0x03",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": "@0",
        "NUM_ARGS": 1
    },
    "POP": {
        "OPCODE": "0x04",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "SRC_REG": "@0",
        "NUM_ARGS": 1
    },
    "ADD": {
        "OPCODE": "0x05",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "ADDC": {
        "OPCODE": "0x06",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "SUB": {
        "OPCODE": "0x07",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "CMP": {
        "OPCODE": "0x08",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "SHR": {
        "OPCODE": "0x09",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "SHL": {
        "OPCODE": "0x0A",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "RRC": {
        "OPCODE": "0x0B",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "RLC": {
        "OPCODE": "0x0C",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "AND": {
        "OPCODE": "0x0D",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "OR": {
        "OPCODE": "0x0E",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "XOR": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 2
    },
    "NOT": {
        "OPCODE": "0x10",
        "CATEGORY": "REGULAR",
        "TYPE": 1,
        "NUM_ARGS": 1
    },
    "CALL": {
        "OPCODE": "0x11",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "SRC_REG": "@0",
        "NUM_ARGS": 1
    },
    "RET": {
        "OPCODE": "0x12",
        "CATEGORY": "REGULAR",
        "TYPE": 0,
        "SRC_REG": "@0",
        "DST_REG": "@0",
        "NUM_ARGS": 0
    },
    "JMP": {
        "OPCODE": "0x13",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 7,
        "NUM_ARGS": 1
    },
    "HLT": {
        "OPCODE": "0x14",
        "CATEGORY": "REGULAR",
        "TYPE": 0,
        "DST_REG": 1,
        "NUM_ARGS": 0
    },
    "dw": {
        "CATEGORY": "SAVED_WORD",
        "NUM_ARGS": 1
    },
    ".org": {
        "CATEGORY": "SAVED_WORD",
        "NUM_ARGS": 1
    },
    "JH": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 1,
        "NUM_ARGS": 1
    },
    "JEQ": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 2,
        "NUM_ARGS": 1
    },
    "JHS": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 3,
        "NUM_ARGS": 1
    },
    "JL": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 4,
        "NUM_ARGS": 1
    },
    "JNE": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 5,
        "NUM_ARGS": 1
    },
    "JLS": {
        "OPCODE": "0x0F",
        "CATEGORY": "REGULAR",
        "TYPE": 3,
        "DST_REG": 6,
        "NUM_ARGS": 1
    }
}