# 6,7,5,2,1,3,5,1,7
def part1(inputStr):
    registerA, registerB, registerC, program = parseInput(inputStr)

    return runProgram(registerA, registerB, registerC, program)

# 216549846240877
# All valid: 234142032285375, 234142032285293, 216549846240959, 216549846240877
def part2(inputStr):
    _, registerB, registerC, program = parseInput(inputStr)
    programStr = ",".join(map(str, program))

    valid = []
    toSearch = [str(i) for i in range(0,8)]
    for octStr in toSearch:
        resultProgStr = runProgram(int(octStr, 8), registerB, registerC, program, target=programStr)
        if resultProgStr == programStr:
            valid.append(int(octStr, 8))

        if programStr.endswith(resultProgStr[-len(octStr):]) and len(octStr) < len(program):
            toSearch.extend([octStr + str(i) for i in range(0,8)])

    return sorted(valid)[0]
    
    # registerA = 0
    # numChars = 1
    # lastProg = ""
    # while lastProg != programStr:
    #     lastProg = runProgram(registerA, registerB, registerC, program)
    #     if lastProg == programStr:
    #         if runProgram(registerA - 1, registerB, registerC, program) == programStr:
    #             return registerA - 1
    #         else:
    #             return registerA
    #     elif programStr.endswith(lastProg[-numChars:]):
    #         # print(f"{numChars:02d}", oct(registerA))
    #         registerA = (registerA << 3)
    #         numChars += 2
        
    #     registerA +=1
        
def parseInput(inputStr):
    import re

    nums = re.compile(r"(\d+)").findall(inputStr)
    nums = list(map(int, nums))
    registerA, registerB, registerC = nums[0], nums[1], nums[2]
    program = nums[3:]

    return registerA, registerB, registerC, program

def runProgram(registerA, registerB, registerC, program, target = ""):
    instructionPtr = 0
    output = ""
    
    while instructionPtr < len(program):
        if target and output[:-1] not in target:
            break
        opcode = program[instructionPtr]

        operandLiteral = program[instructionPtr+1]
        match operandLiteral:
            case 0 | 1 | 2 | 3:
                operandCombo = operandLiteral
            case 4: 
                operandCombo = registerA
            case 5: 
                operandCombo = registerB
            case 6: 
                operandCombo = registerC
            case 7:
                raise NotImplementedError("Combo Operand of 7 Encountered")

        match opcode:
            case 0: # adv
                registerA = registerA // (2 ** operandCombo)
                instructionPtr += 2
            case 1: # bxl
                registerB = registerB ^ operandLiteral
                instructionPtr += 2
            case 2: # bst
                registerB = operandCombo % 8
                instructionPtr += 2
            case 3: # jnz
                if registerA == 0:
                    instructionPtr += 2
                else:
                    instructionPtr = operandLiteral
            case 4: # bxc
                registerB = registerB ^ registerC
                instructionPtr += 2
            case 5: # out
                output += str(operandCombo % 8) + ","
                instructionPtr += 2
            case 6: # bdv
                registerB = registerA // (2 ** operandCombo)
                instructionPtr += 2
            case 7: # cdv
                registerC = registerA // (2 ** operandCombo)
                instructionPtr += 2 
    
    return output[:-1]

def hardCodedInputProgram(a):
    output = ""
    target = "2,4,1,3,7,5,1,5,0,3,4,1,5,5,3,0"

    while a != 0:# and target.startswith(output):
        output += str((((a%8)^3)^5)^(a // (2 ** ((a%8)^3))) % 8) + ","
        a = a//8

    return output[:-1]

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), "4,6,3,5,6,3,5,2,1,0")
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx2), 117440)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), "6,7,5,2,1,3,5,1,7")
    def testRealPart1NOT(self):
        self.assertNotEqual(part1(self.inputStrReal), "5,6,4,2,1,2,2,1,0")
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 216549846240877)

    # Other Test
    def testHardCodedInput(self):
        self.assertEqual(hardCodedInputProgram(21539243), runProgram(*parseInput(self.inputStrReal)))
        
# Run Main ------------------------------------------
if __name__ == "__main__":
    import runpy
    import os
    import sys

    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.getcwd())
    sys.path.insert(0, os.path.join(parent_dir, 'Advent-of-Code'))

    # Run the script
    runpy.run_path("main.py")