# 689
def part1(inputStr):
	paper, instructions = parseInput(inputStr)

	newPaper = foldPaper(paper, instructions[0][0], instructions[0][1])
	return len(newPaper)

# RLBCJGLU
def part2(inputStr):
	paper, instructions = parseInput(inputStr)

	for instruction in instructions:
		paper = foldPaper(paper, instruction[0], instruction[1])

	paperStr = stringPaper(paper)
	printPaper(paperStr)

	return paperStr

def parseInput(inputStr):
	coords, folds = inputStr.split("\n\n")

	# Parse paper
	paper = set()
	for coord in coords.split('\n'):
		coord = coord.split(',')
		x = int(coord[0])
		y = int(coord[1])
		paper.add((x,y))

	# Parse folds
	instructions = []
	for fold in folds.split('\n'):
		fold = fold[11:].split('=')
		axis = fold[0]
		num = int(fold[1])
		instructions.append((axis, num))

	return paper, instructions

def foldPaper(paper, axis, value):
	newPaper = set()

	for x, y in paper:
		if axis == "x":
			if x < value:
				newX = x
			elif x == value:
				pass
			else:
				newX = value - (x - value)
			newY = y
		else:
			newX = x
			if y < value:
				newY = y
			elif y == value:
				pass
			else:
				newY = value - (y - value)
		newPaper.add((newX, newY))

	return newPaper

def printPaper(paperStr):
	print("\n" + paperStr)

def stringPaper(paper):
	maxX = max(map(lambda x: x[0], paper))
	maxY = max(map(lambda x: x[1], paper))
	finalString = ""
	for y in range(maxY+1):
		for x in range(maxX+1):
			if (x, y) in paper:
				finalString += "⬜"
			else:
				finalString += "⬛"
		finalString += "\n"
	return finalString

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
		self.assertEqual(part1(self.inputStrEx), 17)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx),
		"⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬜\n⬜⬛⬛⬛⬜\n⬜⬛⬛⬛⬜\n⬜⬜⬜⬜⬜")

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 689)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), "RLBCJGLU")