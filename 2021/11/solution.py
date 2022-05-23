# 1637
def part1(inputStr):
	octos = parseInput(inputStr)
	flashes = 0
	for i in range(100):
		# if i < 11:
		# 	print("Step ", i)
		# 	print(octos)
		# 	print()
		newFlashes, octos = itterateStep(octos)
		flashes += newFlashes
	return flashes

# 242
def part2(inputStr):
	octos = parseInput(inputStr)
	step = 1
	while True:
		newFlashes, octos = itterateStep(octos)
		if newFlashes == 100:
			return step
		step += 1

def parseInput(inputStr):
	octos = {}
	lines = inputStr.split('\n')
	for y, line in enumerate(lines):
		for x, level in enumerate(line):
			octos[(x, y)] = (int(level), False) # Level, flashed
	return octos

def itterateStep(octos, length=10):
	from itertools import product

	# Add 1 to all
	for coord in product(list(range(length)), list(range(length))):
		level, flashed = octos[coord]
		octos[coord] = (level+1, False)


	# Flashing
	toFlashAdj = []
	newFlashes = 0
	# Find all over 9 and set to flash
	for coord in product(list(range(length)), list(range(length))):
		level, flashed = octos[coord]
		if level > 9:
			octos[coord] = (level, True)
			newFlashes += 1
			toFlashAdj.append(coord)

	while len(toFlashAdj) > 0:
		x, y = toFlashAdj.pop()
		diffs = list(product([-1, 0, +1], [-1, 0, +1]))
		diffs.remove((0,0))
		for xdiff, ydiff in diffs:
			try:
				currentCoord = (x + xdiff, y + ydiff)
				level, flashed = octos[currentCoord]
				level += 1
				if level > 9 and not flashed:
					toFlashAdj.append(currentCoord)
					newFlashes += 1
					flashed = True
				octos[currentCoord] = (level, flashed)
			except KeyError:
				pass

	# Set flashed to 0
	for coord in product(list(range(length)), list(range(length))):
		level, flashed = octos[coord]
		if flashed:
			octos[coord] = (0, flashed)
		else:
			octos[coord] = (level, flashed)

	return newFlashes, octos


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
		self.assertEqual(part1(self.inputStrEx), 1656)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx), 195)

	# Basic Itterate 1 step
	def testExampleItterate(self):
		inputStr = "11111\n19991\n19191\n19991\n11111"
		octos = parseInput(inputStr)
		newFlashes, octos = itterateStep(octos, length = 5)
		self.assertEqual(newFlashes, 9, msg = octos)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 1637)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 242)