# 490
def part1(inputStr):
    return lengthShortestPath(*parseInput(inputStr))
    
# 488
def part2(inputStr):
    _, goal, heightMap = parseInput(inputStr)

    possibleStarts = [coord for coord, height in heightMap.items() if height == 0]
    partialShortestPath = lambda start: lengthShortestPath(start, goal, heightMap)

    return min(map(partialShortestPath, possibleStarts))

def lengthShortestPath(start, goal, heightMap):
    visited = set()
    queue = [(start, 0)]

    found = False
    while not found and len(queue) > 0:
        # Pop the next element
        current, step = queue.pop(0)
        if current == goal:
            return step 
        elif current not in visited: 
            visited.add(current)

            # Add neighbours
            for dir in [+1, -1, +1j, -1j]:
                if (next := current+dir) not in visited and heightMap[next] <= heightMap[current]+1:
                    queue.append((next, step+1))

    return 100000 #Not sure how to initialise better

def parseInput(inputStr):
    from collections import defaultdict
    start = None
    goal = None
    heightMap = defaultdict(lambda: 100) # Large value should never appear

    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            coord = x + y*1j
            if char == "S":
                start = coord
                heightMap[coord] = ord("a") - ord("a")
            elif char == "E":
                goal = coord
                heightMap[coord] = ord("z") - ord("a")
            else:
                heightMap[coord] = ord(char) - ord("a")

    return start, goal, heightMap

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
        self.assertEqual(part1(self.inputStrEx), 31)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 29)

    #Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 490)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 488)