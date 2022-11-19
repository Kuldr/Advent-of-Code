# 3716293
def part1(inputStr):
	from .. import intcode

	memory = intcode.parseIntCode(inputStr)

	noun = 12
	verb = 2
	
	memory[1] = noun
	memory[2] = verb

	memory, outputs = intcode.intCodeRun(memory)

	return memory[0]

# 6429
def part2(inputStr):
	from .. import intcode
	from itertools import product
	goal = 19690720

	memory = intcode.parseIntCode(inputStr)

	for noun, verb in product(range(100), repeat=2):
		memory[1] = noun
		memory[2] = verb

		memoryO, outputs = intcode.intCodeRun(memory.copy())
		if memoryO[0] == goal:
			return 100 * noun + verb

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 3716293)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 6429)