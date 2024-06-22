from instruction import *

class Line:
    def __init__(self, lineNum, label = None, instruction = None):
        self.lineNum = lineNum
        self.label = label
        self.instruction = instruction

    