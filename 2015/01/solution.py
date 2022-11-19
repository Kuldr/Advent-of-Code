# 280
def part1(inputStr):
	floor = 0
	UPFLOOR = "("
	DOWNFLOOR = ")"

	for char in inputStr:
		if char == UPFLOOR:
			floor += 1
		elif char == DOWNFLOOR:
			floor -= 1

	return floor

# 1797
def part2(inputStr):
	floor = 0
	UPFLOOR = "("
	DOWNFLOOR = ")"

	for x, char in enumerate(inputStr):
		if char == UPFLOOR:
			floor += 1
		elif char == DOWNFLOOR:
			floor -= 1

		if floor == -1:
			return x + 1

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExample1Part1(self):
        self.assertEqual(part1("(())"), 0)
    def testExamplePart2(self):
        self.assertEqual(part2("()())"), 5)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 280)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1797)