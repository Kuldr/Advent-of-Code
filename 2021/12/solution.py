# 4186
def part1(inputStr):
	caveMap = parseInput(inputStr)
	global count
	count = 0
	computePossiblePaths(caveMap, "start", set(["start"]), True)
	return count

# 92111
def part2(inputStr):
	caveMap = parseInput(inputStr)
	global count
	count = 0
	computePossiblePaths(caveMap, "start", set(["start"]), False)
	return count

def parseInput(inputStr):
	caveMap = {} # currentCave:set(connections)
	for line in inputStr.split('\n'):
		current, too = line.split('-')
		try:
			caveMap[current].add(too)
		except KeyError:
			caveMap[current] = set()
			caveMap[current].add(too)
		too, current = current, too
		try:
			caveMap[current].add(too)
		except KeyError:
			caveMap[current] = set()
			caveMap[current].add(too)
	
	return caveMap

# Don't like a global count
def computePossiblePaths(caveMap, startNode, visited, twice):
	for cave in caveMap[startNode]:
		if cave == "end":
			global count
			count += 1
		elif cave.isupper():
			newVisited = visited.copy()
			computePossiblePaths(caveMap, cave, newVisited, twice)
		elif cave == "start":
			pass
		elif cave in visited and twice == True:
			pass
		elif cave in visited and twice == False:
			newVisited = visited.copy()
			computePossiblePaths(caveMap, cave, newVisited, True)
		elif cave.islower():
			newVisited = visited.copy()
			newVisited.add(cave)
			computePossiblePaths(caveMap, cave, newVisited, twice)
		
		else:
			raise ValueError("Unknown cave", caveMap, cave, visited)

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
		cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
		cls.inputStrEx3 = importlib.resources.read_text(__package__, "inputEx3.txt")
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
	def testExample1Part1(self):
		self.assertEqual(part1(self.inputStrEx), 10)
	def testExample1Part2(self):
		self.assertEqual(part2(self.inputStrEx), 36)
	def testExample2Part1(self):
		self.assertEqual(part1(self.inputStrEx2), 19)
	def testExample2Part2(self):
		self.assertEqual(part2(self.inputStrEx2), 103)
	def testExample3Part1(self):
		self.assertEqual(part1(self.inputStrEx3), 226)
	def testExample3Part2(self):
		self.assertEqual(part2(self.inputStrEx3), 3509)


    # # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 4186)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 92111)