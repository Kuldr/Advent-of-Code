# 5632
def part1(inputStr):
	coords = parseCoords(inputStr)
	
	from collections import defaultdict
	vents = defaultdict(lambda: 0)

	# Parse the input
	# Horizontal and vertical only
	for coord in coords:
		(x1, y1), (x2, y2) = coord
		if x1 == x2:
			if y2<y1: y2,y1 = y1,y2
			ys = range(y1, y2+1)
			xs = [x1] * len(ys)
		elif y1 == y2:
			if x2<x1: x2,x1 = x1,x2
			xs = range(x1, x2+1)
			ys = [y1] * len(xs)
		else:
			xs, ys = [], []

		for (x, y) in zip(xs, ys):
			vents[(x, y)] += 1
	
	return sum([1 for i in vents.values() if i > 1])

# 22213
def part2(inputStr):
	coords = parseCoords(inputStr)
	
	from collections import defaultdict
	vents = defaultdict(lambda: 0)

	# Parse the input
	for coord in coords:
		(x1, y1), (x2, y2) = coord
		if y1 < y2:
			ys = range(y1, y2+1)
		else:
			ys = range(y1, y2-1, -1)
		if x1 < x2:
			xs = range(x1, x2+1)
		else:
			xs = range(x1, x2-1, -1)

		from itertools import cycle
		if len(xs) < len(ys):
			xs = cycle(xs)
		elif len(ys) < len(xs):
			ys = cycle(ys)

		for (x, y) in zip(xs, ys):
			vents[(x, y)] += 1

	return sum([1 for i in vents.values() if i > 1])

def parseCoords(inputStr):
	coords = []
	lines = inputStr.split('\n')
	for line in lines:
		left, right = line.split(' -> ')
		left = tuple(int(i) for i in left.split(','))
		right = tuple(int(i) for i in right.split(','))
		coords.append((left, right))
	return coords

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
        self.assertEqual(part1(self.inputStrEx), 5)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 12)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 5632)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 22213)