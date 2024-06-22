class Instruction():
    def __init__(self, opcode, addrMode, src, dst, numberOfBytes, immValue = None):
        self.opcode = opcode
        self.addrMode = addrMode
        self.src = src
        self.dst = dst
        self.numberOfBytes = numberOfBytes
        self.immValue = immValue

        