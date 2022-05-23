# 517
def part1(inputStr):
    return runNTurns(list(map(int, inputStr.split(','))), 2020)

# 1047739
def part2(inputStr):
    return runNTurns(list(map(int, inputStr.split(','))), 30_000_000)

# Refactor so it doesn't need 2 values 
def runNTurns(startingNumbers, maxTurn):
	# Set up data structure for tracking numbers
	numbersSpoken = {}

	# itterate over the starting numbers
	for turn, num in enumerate(startingNumbers, start=1):
		addToSpoken(num, turn, numbersSpoken)
	recentlySpoken = num

	# Run main game loop
	for turn in range(turn+1, maxTurn+1):
		next = numbersSpoken[recentlySpoken][1]
		addToSpoken(next, turn, numbersSpoken)
		
		recentlySpoken = next
		
		if turn % int(maxTurn/100) == 0:
			print(int(turn/(maxTurn/100)), '%')

	return next

def addToSpoken(value, currentTurn, numbersSpoken):
    try:
        lastTurn = numbersSpoken[value][0]
        numbersSpoken[value] = (currentTurn, currentTurn - lastTurn)
    except KeyError:
        numbersSpoken[value] = (currentTurn, 0)

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests 
    # 0,3,6  
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 436)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 175594)
    # 1,3,2
    def testExample2Part1(self):
        self.assertEqual(part1("1,3,2"), 1)
    # def testExample2Part2(self):
    #     self.assertEqual(part2("1,3,2"), 2578)
    # 2,1,3
    def testExample3Part1(self):
        self.assertEqual(part1("2,1,3"), 10)
    # def testExample3Part2(self):
    #     self.assertEqual(part2("2,1,3"), 3544142)
    # 1,2,3
    def testExample4Part1(self):
        self.assertEqual(part1("1,2,3"), 27)
    # def testExample4Part2(self):
    #     self.assertEqual(part2("1,2,3"), 261214)
    # 2,3,1
    def testExample5Part1(self):
        self.assertEqual(part1("2,3,1"), 78)
    # def testExample5Part2(self):
    #     self.assertEqual(part2("2,3,1"), 6895259)
    # 3,2,1
    def testExample6Part1(self):
        self.assertEqual(part1("3,2,1"), 438)
    # def testExample6Part2(self):
    #     self.assertEqual(part2("3,2,1"), 18)
    # 3,1,2
    def testExample7Part1(self):
        self.assertEqual(part1("3,1,2"), 1836)
    # def testExample7Part2(self):
    #     self.assertEqual(part2("3,1,2"), 362)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 517)
    def testRealPart2(self):
      self.assertEqual(part2(self.inputStrReal), 1047739)