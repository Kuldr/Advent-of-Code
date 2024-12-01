# 1603498
def part1(inputStr):
    left, right = parseInput(inputStr)

    left = sorted(left)
    right = sorted(right)
    
    diffs = [abs(leftVal - rightVal) for leftVal, rightVal in zip(left, right)]
    return sum(diffs)

# 25574739
def part2(inputStr):
    left, right = parseInput(inputStr)

    from collections import Counter
    rightCount = Counter(right)

    results = [leftVal * rightCount[leftVal] for leftVal in left]
    return sum(results)

def parseInput(inputStr):
    left, right = [], []
    for line in inputStr.split("\n"):
        leftVal, rightVal = line.split("   ")
        left.append(int(leftVal))
        right.append(int(rightVal))
    
    return left, right

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
        self.assertEqual(part1(self.inputStrEx), 11)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 31)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1603498)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 25574739)