# 415
def part1(inputStr):
	return dijkstra(parseInput(inputStr))

# 2864
def part2(inputStr):
	return dijkstra(modifyInput(parseInput(inputStr)))

def parseInput(inputStr):
	return {(x, y): int(risk) for y, line in enumerate(inputStr.split('\n')) for x, risk in enumerate(line)}

def dijkstra(riskLevels):
	minCoord = min(riskLevels.keys(), key = lambda x:x[0])[0]
	maxCoord = max(riskLevels.keys(), key = lambda x:x[0])[0]
	start = (minCoord, minCoord)
	end = (maxCoord, maxCoord) # Known to be square
	possibleDirs = [(0,+1), (0,-1), (+1,0), (-1,0)]
	coordsNext = [(0, start)]
	queued = set([start])
	from heapq import heappop, heappush

	while end not in queued:
		lowestRisk, lowest = heappop(coordsNext)
		lowX, lowY = lowest
		for xDir, yDir in possibleDirs:
			coordToAttempt = (lowX+xDir, lowY+yDir)
			try:
				riskSoFar = lowestRisk+riskLevels[coordToAttempt]
				if coordToAttempt == end:
					return riskSoFar
				elif coordToAttempt not in queued:
					heappush(coordsNext, (riskSoFar, coordToAttempt))
					queued.add(coordToAttempt)
			except KeyError:
				pass

def modifyInput(riskLevelsInitial):
	maxCoord = max(riskLevelsInitial.keys(), key = lambda x:x[0])[0]+1
	riskLevels = {}

	riskLoop = [1,2,3,4,5,6,7,8,9]
	riskChanges = {(x,y): x+y for x in range(5) for y in range(5)}
	for coord, risk in riskLevelsInitial.items():
		x, y = coord
		for coordDif, riskAdd in riskChanges.items():
			xDiff, yDiff = coordDif
			riskLevels[(x+xDiff*maxCoord, y+yDiff*maxCoord)] = riskLoop[(risk+riskAdd-1)%9]

	return riskLevels
			
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
        self.assertEqual(part1(self.inputStrEx), 40)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 315)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 415)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 2864)