# 557
def part1(inputStr):
	positions = parseInput(inputStr)
	
	return sorted([abs(x) + abs(y) for (x, y), (wire, _) in positions.items() if wire == 'X'])[0]

# 56410
def part2(inputStr):
	positions = parseInput(inputStr)
	
	return sorted([steps for (wire, steps) in positions.values() if wire == 'X'])[0]

def parseInput(inputStr):
	wire1, wire2 = inputStr.split('\n')
	wire1List = wire1.split(',')
	wire2List = wire2.split(',')
	
	x = 0
	y = 0
	positions = {}
	
	mapWiresWStep(wire1List, positions, '1')
	mapWiresWStep(wire2List, positions, '2')
	return positions

def mapWiresWStep(wireList, positions, identifier):
	x = 0
	y = 0
	step = 0

	for i in wireList:
		d = i[0]
		n = int(i[1:])

		for j in range(n):
			if d == 'U':
				y += 1
			elif d == 'D':
				y -= 1
			elif d == 'R':
				x += 1
			elif d == 'L':
				x -= 1
			step += 1
		
			if (x, y) in positions:
				if positions[(x, y)][0] != identifier:      
					positions[(x, y)] = ('X', positions[(x, y)][1] + step)
			else:
				positions[(x, y)] = (identifier, step)

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx1 = importlib.resources.read_text(__package__, "inputEx1.txt")
		cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
		cls.inputStrEx3 = importlib.resources.read_text(__package__, "inputEx3.txt")
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
	def testExample1Part1(self):
		self.assertEqual(part1(self.inputStrEx1), 6)
	def testExample1Part2(self):
		self.assertEqual(part2(self.inputStrEx1), 30)
	def testExample2Part1(self):
		self.assertEqual(part1(self.inputStrEx2), 159)
	def testExample2Part2(self):
		self.assertEqual(part2(self.inputStrEx2), 610)
	def testExample3Part1(self):
		self.assertEqual(part1(self.inputStrEx3), 135)
	def testExample3Part2(self):
		self.assertEqual(part2(self.inputStrEx3), 410)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 557)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 56410)