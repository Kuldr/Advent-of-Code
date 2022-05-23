# 539
def part1(inputStr):
	heightMap = parseInput(inputStr)
	riskLevels = []
	for (x,y), height in heightMap.items():
		neighbours = [
			isHigher(heightMap, x, y-1, height),
			isHigher(heightMap, x, y+1, height),
			isHigher(heightMap, x-1, y, height),
			isHigher(heightMap, x+1, y, height)
		]
		if all(neighbours):
			riskLevels.append(height+1)
	return sum(riskLevels)

# 736920
def part2(inputStr):
	heightMap = parseInput(inputStr)
	lowPoints = []
	for (x,y), height in heightMap.items():
		neighbours = [
			isHigher(heightMap, x, y-1, height),
			isHigher(heightMap, x, y+1, height),
			isHigher(heightMap, x-1, y, height),
			isHigher(heightMap, x+1, y, height)
		]
		if all(neighbours):
			lowPoints.append((x, y))

	basinSizes = [numNeighboursBasin(heightMap, x, y, set()) for x, y in lowPoints]
	basinSizes.sort()
	from math import prod
	return prod(basinSizes[-3:])

def parseInput(inputStr):
	heightMap = {}
	lines = inputStr.split('\n')
	for y, line in enumerate(lines):
		for x, height in enumerate(line):
			heightMap[(x, y)] = int(height)
	return heightMap

def isHigher(heightMap, x, y, height):
	try:
		if heightMap[(x, y)] > height:
			return True
		else:
			return False
	except KeyError:
		return True

def numNeighboursBasin(heightMap, x, y, pointsAccessed):
	diffs = [(0,-1),(0,+1),(-1,0),(+1,0)]
	neighboursTotal = []
	for xdiff, ydiff in diffs:
		try:
			xNew = x+xdiff
			yNew = y+ydiff
			if heightMap[(xNew, yNew)] != 9 and (xNew, yNew) not in pointsAccessed:
				pointsAccessed.add((xNew, yNew))
				neighboursTotal.append(1 + numNeighboursBasin(heightMap, xNew, yNew, pointsAccessed))
			else:
				neighboursTotal.append(0)
		except KeyError:
			neighboursTotal.append(0)

	return sum(neighboursTotal)
	

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
        self.assertEqual(part1(self.inputStrEx), 15)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 1134)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 539)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 736920)