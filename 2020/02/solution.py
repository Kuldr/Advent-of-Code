# 655
def part1(inputStr):
    parsedList = parseInput(inputStr)

    validTally = 0
    for x in parsedList:
        count = x["password"].count(x["letter"])
        if count >= x["num1"] and count <= x["num2"] :
            validTally += 1

    return validTally

# 673
def part2(inputStr):
    parsedList = parseInput(inputStr)

    validTally = 0
    for x in parsedList:
        check1 = x["password"][x["num1"]-1] == x["letter"]
        check2 = x["password"][x["num2"]-1] == x["letter"]
        if check1 != check2: # != performs xor on boolean variables
            validTally += 1
    return validTally

def parseInput(inputStr):
    inputList = inputStr.split('\n')

    # Create a list of parsed dictionaries containing "password", "letter", "num1", "num2"
    parsedList = []
    for x in inputList:
        d = {}
        colonSplit = x.split(':')
        d["password"] = colonSplit[1][1:]
        policy = colonSplit[0].split(' ')
        d["letter"] = policy[-1]
        numbers = policy[0].split('-')
        d["num1"] = int(numbers[0])
        d["num2"] = int(numbers[1])
        parsedList.append(d)
    
    return parsedList

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
        self.assertEqual(part1(self.inputStrEx), 2)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 1)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 655)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 673)