# Count the pairs???

# 2233
def part1(inputStr):
	start, swaps = parseInput(inputStr)
	sequence = start
	for i in range(10):
		sequence = itterateStep(sequence, swaps)

	counts = {char:sequence.count(char) for char in set(sequence)}
	return max(counts.values()) - min(counts.values())

# ANSWER
def part2(inputStr):
	start, swaps = parseInput(inputStr)
	sequence = start
	for i in range(40):
		sequence = itterateStep(sequence, swaps)
		print(i)

	counts = {char:sequence.count(char) for char in set(sequence)}
	return max(counts.values()) - min(counts.values())

def parseInput(inputStr):
	start = inputStr.split('\n\n')[0]
	swaps = {}
	for s in inputStr.split('\n\n')[1].split('\n'):
		vals = s.split(" -> ")
		swaps[vals[0]] = vals[0][0] + vals[1] #+ vals[0][1]

	return start, swaps

def itterateStep(initial, swaps):
	newSequence = ""
	for first, second in zip(initial, initial[1:]):
		newSequence += swaps[first + second]

	newSequence += initial[-1]
	return newSequence

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
        self.assertEqual(part1(self.inputStrEx), 1588)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 2188189693529)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2233)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 0)