# 2233
def part1(inputStr):
	return puzzleNSteps(10, inputStr)

# 2884513602164
def part2(inputStr):
	return puzzleNSteps(40, inputStr)

def puzzleNSteps(n, inputStr):
	from collections import defaultdict
	sequenceCounts, swaps, firstChar, lastChar = parseInput(inputStr)
	for i in range(n):
		sequenceCounts = itterateStep(sequenceCounts, swaps)

	counts = defaultdict(lambda: 0)
	for pair, number in sequenceCounts.items():
		for char in pair:
			counts[char] += number

	# Fix double counting issues
	counts[firstChar] += 1
	counts[lastChar] += 1
	counts = {char:val//2 for char, val in counts.items()}

	return (max(counts.values()) - min(counts.values()))

def parseInput(inputStr):
	# Parse the counts
	startStr = inputStr.split('\n\n')[0]
	from collections import defaultdict
	startCounts = defaultdict(lambda: 0)
	for first, second  in zip(startStr, startStr[1:]):
		startCounts[first+second] += 1

	# Parse the swaps
	swaps = {}
	for s in inputStr.split('\n\n')[1].split('\n'):
		vals = s.split(" -> ")
		swaps[vals[0]] = (vals[0][0] + vals[1], vals[1] + vals[0][1])

	return startCounts, swaps, startStr[0], startStr[-1]

def itterateStep(initial, swaps):
	from collections import defaultdict
	newSequence = defaultdict(lambda: 0)
	for pair, number in initial.items():
		# print(pair, number)
		newSequence[swaps[pair][0]] += number
		newSequence[swaps[pair][1]] += number

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
        self.assertEqual(part2(self.inputStrReal), 2884513602164)