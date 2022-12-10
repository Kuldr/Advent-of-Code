# 14780
def part1(inputStr):
    instructions = parseInstructions(inputStr)
    registerX = 1
    cycle = 1
    signalStrengths = []
    for opCode, operand in instructions:
        if opCode == "addx":
            cycle = runCyclePart1(cycle, signalStrengths, registerX)
        cycle = runCyclePart1(cycle, signalStrengths, registerX)
        registerX += operand

    return sum(signalStrengths)

def runCyclePart1(cycle, signalStrengths, registerX):
    if (cycle+20) % 40 == 0:
        signalStrengths.append(cycle*registerX)     
    return cycle + 1

# ANSWER
def part2(inputStr):
    instructions = parseInstructions(inputStr)
    registerX = 1
    cycle = 0
    crt = "\n"
    for opCode, operand in instructions:
        if opCode == "addx":
            cycle, crt = runCyclePart2(cycle, crt, registerX)
        cycle, crt = runCyclePart2(cycle, crt, registerX)
        registerX += operand

    print(crt)
    return crt

def runCyclePart2(cycle, crt, registerX):
    if (registerX - 1) == cycle or (registerX) == cycle or (registerX + 1) == cycle:
        crt += "⬛"
    else:
        crt += "⬜"
    
    cycle += 1
    if cycle % 40 == 0:
        crt += "\n"
        cycle = 0

    return cycle, crt

def parseInstructions(inputStr):
    instructions = []
    for line in inputStr.split("\n"):
        ops = line.split(" ")
        if ops[0] == "noop":
            instructions.append(("noop", 0))
        elif ops[0] == "addx":
            instructions.append(("addx", int(ops[1])))
        else:
            raise ValueError(f"Unknown Opcode {ops[0]}")
    
    return instructions

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 13140)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 14780)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 0)