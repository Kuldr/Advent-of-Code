# 2572
def part1(inputStr):
	from collections import defaultdict
	houses = defaultdict(lambda: 0)
	
	return len(deliverPresents(inputStr, houses))

def deliverPresents(inputStr, houses):
	x = 0
	y = 0

	houses[(x, y)] += 1

	for char in inputStr:
		if char == "^":
			y += 1
		elif char == "v":
			y -= 1
		elif char == ">":
			x += 1
		elif char == "<":
			x -= 1

		houses[(x, y)] += 1

	return houses

# 2631
def part2(inputStr):
	from collections import defaultdict
	houses = defaultdict(lambda: 0)

	houses = deliverPresents(inputStr[::2], houses)
	return len(deliverPresents(inputStr[1::2], houses))
	
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
        self.assertEqual(part1("^v^v^v^v^v"), 2)
    def testExamplePart2(self):
        self.assertEqual(part2("^v^v^v^v^v"), 11)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2572)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 2631)