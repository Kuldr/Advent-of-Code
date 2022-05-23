# 880
def part1(inputStr):
    return calcSeatIDs(inputStr)[-1]   

# 731
def part2(inputStr):
    seatIDs = calcSeatIDs(inputStr)

    for x in range(seatIDs[0], seatIDs[-1]+1):
        if x not in seatIDs:
            return x

def calcSeatIDs(inputStr):
    return sorted(
        map(lambda b: int(b, base = 2), 
        map(lambda s: s.translate(str.maketrans(
            {'B':'1', 'F':'0', 'R':'1', 'L':'0'}))
        , inputStr.split("\n"))))

def calcSeatIDsOLD(inputStr):
    inputList = inputStr.split("\n")

    seatIDs = []
    for ticket in inputList:       
        #Row calculator
        r = allocation(ticket[:7], 'F', 'B')

        # Column Calculator
        c = allocation(ticket[7:], 'L', 'R')

        seatIDs.append(r*8 +c)

    seatIDs.sort()
    return seatIDs
    
def allocation(string, lowerChar, upperChar):
    import math
    lower = 0
    upper = 2 ** len(string) -1
    for i in string:
        lowerMid = math.floor((lower+upper)/2)
        upperMid = math.ceil((lower+upper)/2)
        if i == upperChar:
            lower = upperMid
        elif i == lowerChar:
            upper = lowerMid
    return lower

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
        self.assertEqual(part1(self.inputStrEx), 820)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 880)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 731)