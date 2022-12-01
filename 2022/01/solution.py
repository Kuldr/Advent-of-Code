# 71300
def part1(inputStr):
    inputStr = inputStr[:-1]
    elves = inputStr.split("\n\n")
    elvesCalories = [sum(map(int, elf.split("\n"))) for elf in elves]

    return max(elvesCalories)

# 209691
def part2(inputStr):
    inputStr = inputStr[:-1]
    elves = inputStr.split("\n\n")
    elvesCalories = [sum(map(int, elf.split("\n"))) for elf in elves]

    return sum(sorted([elvesCalories])[-3:])

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
        self.assertEqual(part1(self.inputStrEx), 24000)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 45000)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 71300)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 209691)