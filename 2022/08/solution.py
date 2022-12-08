# 1708
def part1(inputStr):
	rows = len(splitInput := inputStr.split("\n"))
	cols = len(splitInput[0])
	forest = {(x,y): int(tree) 
			  for y, row in enumerate(splitInput) 
			  for x, tree in enumerate(row)}

	visible = set()

	# N->S
	for x in range(cols):
		current = -1
		for y in range(rows):
			if (next := forest[(x,y)]) > current:
				visible.add((x,y))
				current = next
	# S->N
	for x in range(cols):
		current = -1
		for y in range(rows-1, -1, -1):
			if (next := forest[(x,y)]) > current:
				visible.add((x,y))
				current = next
	# E->W
	for y in range(rows):
		current = -1
		for x in range(cols):
			if (next := forest[(x,y)]) > current:
				visible.add((x,y))
				current = next
	# W->E New
	for y in range(rows):
		current = -1
		for x in range(cols-1, -1, -1):
			if (next := forest[(x,y)]) > current:
				visible.add((x,y))
				current = next

	return len(visible)

# ANSWER
def part2(inputStr):
	rows = len(splitInput := inputStr.split("\n"))
	cols = len(splitInput[0])
	forest = {(x,y): int(tree) 
			  for y, row in enumerate(splitInput) 
			  for x, tree in enumerate(row)}

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
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)