# 1708
def part1(inputStr):
	rows, cols, forest = parseTrees(inputStr)

	visible = set()

	# N->S
	for x in range(cols):
		current = -1
		for y in range(rows):
			if (next := forest[x+y*1j]) > current:
				visible.add(x+y*1j)
				current = next
	# S->N
	for x in range(cols):
		current = -1
		for y in range(rows-1, -1, -1):
			if (next := forest[x+y*1j]) > current:
				visible.add(x+y*1j)
				current = next
	# E->W
	for y in range(rows):
		current = -1
		for x in range(cols):
			if (next := forest[x+y*1j]) > current:
				visible.add(x+y*1j)
				current = next
	# W->E New
	for y in range(rows):
		current = -1
		for x in range(cols-1, -1, -1):
			if (next := forest[x+y*1j]) > current:
				visible.add(x+y*1j)
				current = next

	return len(visible)

# 504000
def part2(inputStr):
	_, _, forest = parseTrees(inputStr)

	scenicScores = {coord: scenicScore(coord, forest)
					for coord in forest.keys()}
	
	return max(scenicScores.values())

def scenicScore(coord, forest):
	maxHeight = forest[coord]
	treesInDir = []
	for direction in [-1j, -1, +1j, +1]:
		trees = 0
		while (testCoord := coord+(trees+1)*direction) in forest:
			if forest[testCoord] < maxHeight:
				trees += 1
			else:
				trees += 1
				break
		treesInDir.append(trees)

	from math import prod
	return prod(treesInDir)

def parseTrees(inputStr):
	rows = len(splitInput := inputStr.split("\n"))
	cols = len(splitInput[0])
	forest = {x+y*1j: int(tree) 
			  for y, row in enumerate(splitInput) 
			  for x, tree in enumerate(row)}

	return rows, cols, forest

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
        self.assertEqual(part1(self.inputStrEx), 21)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 8)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1708)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 504000)