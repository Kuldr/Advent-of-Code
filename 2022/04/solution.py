# 515
def part1(inputStr):
    count = 0
    for pairs in inputStr.split("\n"):
        elf1, elf2 = pairs.split(",")
        elf1Lower, elf1Upper = map(int, elf1.split("-"))
        elf2Lower, elf2Upper = map(int, elf2.split("-"))
        elf1Set = set(range(elf1Lower, elf1Upper+1))
        elf2Set = set(range(elf2Lower, elf2Upper+1))

        if elf1Set.issubset(elf2Set) or elf2Set.issubset(elf1Set):
            count += 1

    return count

# 883
def part2(inputStr):
    count = 0
    for pairs in inputStr.split("\n"):
        elf1, elf2 = pairs.split(",")
        elf1Lower, elf1Upper = map(int, elf1.split("-"))
        elf2Lower, elf2Upper = map(int, elf2.split("-"))
        elf1Set = set(range(elf1Lower, elf1Upper+1))
        elf2Set = set(range(elf2Lower, elf2Upper+1))

        overlap = elf1Set.intersection(elf2Set)

        if len(overlap) > 0:
            count += 1

    return count

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
        self.assertEqual(part2(self.inputStrEx), 4)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 515)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 883)