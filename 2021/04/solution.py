# 440088
def part1(inputStr):
	from numpy import transpose
	numbers, boards = parseInput(inputStr)

	foundWinning = False
	currentNums = []
	for i, num in enumerate(numbers):
		currentNums.append(num)
		for board in boards:
			# Check rows
			for row in board:
				if set(row) <= set(currentNums):
					foundWinning = True
					break
			if foundWinning: break
			# Check cols
			for col in transpose(board):
				if set(col) <= set(currentNums):
					foundWinning = True
					break
			if foundWinning: break
		if foundWinning:
			winningNumber = num
			winningBoard = board
			winningCalls = currentNums
			break

	winningBoard = [i for l in winningBoard for i in l]
	missingNumbers = [i for i in winningBoard if i not in winningCalls]
	
	return sum(missingNumbers) * winningNumber

# 23670
def part2(inputStr):
	from numpy import transpose
	numbers, boards = parseInput(inputStr)

	currentNums = []
	for i, num in enumerate(numbers):
		currentNums.append(num)
		boardsToRemove = []
		for board in boards:
			# Check rows
			for row in board:
				if set(row) <= set(currentNums):
					boardsToRemove.append(board)
			# Check cols
			for col in transpose(board):
				if set(col) <= set(currentNums):
					boardsToRemove.append(board)
		
		# Remove all winning boards
		for board in list(boardsToRemove):
			try: boards.remove(board)
			except ValueError: pass

		# Check if losing board has been found
		if len(boards) == 1:
			losingBoard = boards[0]
			break

	foundWinning = False
	currentNums = []
	for i, num in enumerate(numbers):
		currentNums.append(num)
		# Check rows
		for row in losingBoard:
			if set(row) <= set(currentNums):
				foundWinning = True
				break
		if foundWinning: break
		# Check cols
		for col in transpose(losingBoard):
			if set(col) <= set(currentNums):
				foundWinning = True
				break
			if foundWinning: break
		if foundWinning:
			winningNumber = num
			winningBoard = losingBoard
			winningCalls = currentNums
			break
		
	winningBoard = [i for l in winningBoard for i in l]
	missingNumbers = [i for i in winningBoard if i not in winningCalls]
	
	return sum(missingNumbers) * winningNumber

def parseInput(inputStr):
	splitLines = inputStr.split('\n\n')
	
	numbers = [int(i) for i in splitLines[0].split(',')]

	boards = []
	for boardText in splitLines[1:]:
		board = []
		for rowText in boardText.split('\n'):
			row = rowText.split(' ')
			row = list(filter(lambda x: x != '', row))
			row = list(map(int, row))
			board.append(row)
		boards.append(board)

	return numbers, boards

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
        self.assertEqual(part1(self.inputStrEx), 4512)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 1924)

    # # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 44088)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 23670)