# 1521
def part1(inputStr):
    depths = [int(i) for i in inputStr.split('\n')]
    zippedDepths = zip(depths[0:], depths[1:])
    diffDepths = [b - a for (a, b) in zippedDepths]

    return sum([1 for diff in diffDepths if diff > 0])

# 1543
def part2(inputStr):
    depths = [int(i) for i in inputStr.split('\n')]
    depths3 = [sum(t) for t in zip(depths[0:], depths[1:], depths[2:])]

    zippedDepths = zip(depths3[0:], depths3[1:])
    diffDepths = [b - a for (a, b) in zippedDepths]

    return sum([1 for diff in diffDepths if diff > 0])

# 1521
def part1OLD(inputStr):
    depths = [int(i) for i in inputStr.split('\n')]

    lastDepth = depths[0]

    increase = 0
    for depth in depths:
        if depth > lastDepth:
            increase += 1
        lastDepth = depth

    return increase

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
        self.assertEqual(part2(self.inputStrEx), 5)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1521)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1543)
