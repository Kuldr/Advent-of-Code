import itertools

# 324
def part1(inputStr):
    conwayGrid = {}
    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            if char == "#":
                conwayGrid[(x, y, 0)] = True
            else:
                conwayGrid[(x, y, 0)] = False 

    for i in range(6):
        newGrid = {}
        keys = conwayGrid.keys()
        minX = min(keys)[0]
        maxX = max(keys)[0]
        rangeOfCoords = range(minX-1, maxX+2)
        combinations = list(itertools.product(rangeOfCoords, rangeOfCoords, rangeOfCoords))
        for a, b, c in combinations:
            activeNeighbours = numActiveNeighbours(a, b, c, conwayGrid)
            if (a,b,c) in conwayGrid and conwayGrid[(a, b, c)]:
                if not(activeNeighbours == 2 or activeNeighbours == 3):
                    newGrid[(a, b, c)] = False
                else:
                    newGrid[(a, b, c)] = True
            else:
                if activeNeighbours == 3:
                    newGrid[(a, b, c)] = True
                else:
                    newGrid[(a, b, c)] = False
        conwayGrid = newGrid

    return sum(conwayGrid.values())

# 1836
def part2(inputStr):
    conwayGrid = {}
    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            if char == "#":
                conwayGrid[(x,y,0,0)] = True
            else:
                conwayGrid[(x,y,0,0)] = False

    for i in range(6):
        newGrid = {}
        keys = conwayGrid.keys()
        minX = min(keys)[0]; maxX = max(keys)[0]
        minY = min(keys)[1]; maxY = max(keys)[1]
        minZ = min(keys)[2]; maxZ = max(keys)[2]
        minW = min(keys)[3]; maxW = max(keys)[3]
        combinations = list(itertools.product(range(minX-1, maxX+2),
                                            range(minY-1, maxY+2), 
                                            range(minZ-1, maxZ+2),
                                            range(minW-1, maxW+2)))
        for a, b, c, d in combinations:
            activeNeighbours = numActiveNeighbours2(a,b,c,d,conwayGrid)
            if (a,b,c,d) in conwayGrid and conwayGrid[(a, b, c, d)]:
                if not(activeNeighbours == 2 or activeNeighbours == 3):
                    newGrid[(a, b, c, d)] = False
                else:
                    newGrid[(a, b, c, d)] = True
            else:
                if activeNeighbours == 3:
                    newGrid[(a, b, c, d)] = True
                else:
                    newGrid[(a, b, c, d)] = False
        conwayGrid = newGrid

    return sum(conwayGrid.values())

def numActiveNeighbours(x,y,z,conwayGrid):
    numActive = 0
    combinations = list(itertools.product([x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1]))
    combinations.remove((x, y, z))
    for i, j, k in combinations:
        if (i, j, k) in conwayGrid and conwayGrid[(i, j, k)]:
            numActive += 1
    return numActive

def numActiveNeighbours2(x,y,z,w,conwayGrid):
    numActive = 0
    combinations = list(itertools.product([x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1], [w-1,w,w+1]))
    combinations.remove((x, y, z, w))
    for i, j, k, l in combinations:
        if (i, j, k, l) in conwayGrid and conwayGrid[(i, j, k, l)]:
            numActive += 1
    return numActive

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
        self.assertEqual(part1(self.inputStrEx), 112)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 848)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 324)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1836)