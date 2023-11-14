# 6745
def part1(inputStr):
	return simulateRope(inputStr, 2)

# 2793
def part2(inputStr):
	return simulateRope(inputStr, 10)

def simulateRope(inputStr, nodes):
	commands = parseMovements(inputStr)
	knots = [0+0j] * nodes
	visited = {knots[-1]}
	for dir, num in commands:
		for _ in range(num):
			knots[0] += dir
			for index, coords in enumerate(zip(knots, knots[1:])):				
				knots[index+1] = calculateNewCoord(*coords)

			visited.add(knots[-1])
			
	return len(visited)

def calculateNewCoord(prev, current):
	diff = prev-current
	if abs(diff) > 2**0.5:
		if diff.real >= +1:
			current += 1
		elif diff.real <= -1:
			current += -1
		if diff.imag >= +1:
			current += 1j
		elif diff.imag <= -1:
			current += -1j
			
	return current

def parseMovements(inputStr):
	commands = []
	translateDirs = {"U": +1j, "R": +1, "D": -1j, "L": -1}
	for command in inputStr.split("\n"):
		dir, num = command.split(" ")
		commands.append((translateDirs[dir], int(num)))

	return commands

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
		cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
	def testExample1Part1(self):
		self.assertEqual(part1(self.inputStrEx), 13)
	def testExample1Part2(self):
		self.assertEqual(part2(self.inputStrEx), 1)
	def testExample2Part2(self):
		self.assertEqual(part2(self.inputStrEx2), 36)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 6745)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 2793)