import itertools

# 987339
def part1(inputStr):
    inputList = map(int, inputStr.split('\n'))
    combinations = itertools.combinations(inputList, 2)
    return [x*y for x,y in combinations if x+y == 2020][0]

# 259521570
def part2(inputStr):
    inputList = map(int, inputStr.split('\n'))
    combinations = itertools.combinations(inputList, 3)
    return [x*y*z for x,y,z in combinations if x+y+z == 2020][0]

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
        self.assertEqual(part1(self.inputStrEx), 514579)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 241861950)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 987339)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 259521570)