# 12440243
def part1(inputStr):
	from .. import intcode
	
	memory = intcode.parseIntCode(inputStr)
	memory, outputs = intcode.intCodeRun(memory, inputs= [1])
	return outputs[-1]

# 15486302
def part2(inputStr):
	from .. import intcode
	
	memory = intcode.parseIntCode(inputStr)
	memory, outputs = intcode.intCodeRun(memory, inputs= [5])
	return outputs[-1]

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 12440243)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 15486302)