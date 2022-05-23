# 336
def part1(inputStr):
    return checkSlope(inputStr, 3, 1)

# 5522401584
def part2(inputStr):
    from functools import reduce
    results = [checkSlope(inputStr, 1, 1),
                checkSlope(inputStr, 3, 1), 
                checkSlope(inputStr, 5, 1), 
                checkSlope(inputStr, 7, 1), 
                checkSlope(inputStr, 1,2)]
    return reduce(lambda x, y: x*y, results)

def checkSlope(inputStr, right, down):
    lines = inputStr.split('\n')
    cols = len(lines[0])
    xPos = 0
    yPos = 0
    treeCount = 0

    while yPos < len(lines):
        row = lines[yPos]
        if row[xPos] == '#':
            treeCount += 1
        xPos = (xPos + right) % cols
        yPos += down

    return treeCount

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
        self.assertEqual(part1(self.inputStrEx), 7)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 336)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 289)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 5522401584)