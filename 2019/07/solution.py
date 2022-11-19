# 298586
def part1(inputStr):
	from itertools import permutations
	from .. import intcode
	
	memory = intcode.parseIntCode(inputStr)
	finalOutputs = []
	for phaseSettings in permutations(range(5)):
		previousOutput = 0
		for pX in phaseSettings:
			_, previousOutputs = intcode.intCodeRun(memory, [pX, previousOutput])
			previousOutput = previousOutputs[0]
			finalOutputs.append(previousOutput)
			
	return max(finalOutputs)

# ANSWER
def part2(inputStr):
    return "Part 2 Not Implemented"

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
	def testExamplePart1Ex1(self):
		self.assertEqual(part1("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"), 43210)
	def testExamplePart1Ex2(self):
		self.assertEqual(part1(
		"3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"),
						 54321)
	def testExamplePart1Ex3(self):
		self.assertEqual(part1(
		"3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"),
						 65210)

		
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 298586)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 0)