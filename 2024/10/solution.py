# 794
def part1(inputStr):
    topoMap = parseInput(inputStr)

    trailHeads = [coord for coord, height in topoMap.items() if height == 0]

    results = []
    for trailHead in trailHeads:
        accessible = []
        scoreTrailHead(trailHead, 1, topoMap, accessible)
        results.append(len(set(accessible)))

    return sum(results)

# 1706
def part2(inputStr):
    topoMap = parseInput(inputStr)

    trailHeads = [coord for coord, height in topoMap.items() if height == 0]

    results = []
    for trailHead in trailHeads:
        accessible = []
        scoreTrailHead(trailHead, 1, topoMap, accessible)
        results.append(len(accessible))

    return sum(results)

def parseInput(inputStr):
    from collections import defaultdict
    topoMap = defaultdict(lambda: -1)
    for y, line in enumerate(inputStr.split()):
        for x, char in enumerate(line):
            if char == ".":
                char = -1
            topoMap[complex(x, y)] = int(char)

    return topoMap

def scoreTrailHead(currentPos, nextVal, topoMap, accessible):
    if topoMap[currentPos] == 9:
        accessible.append(currentPos)
        return
    
    dirs = [-1j, +1j, -1, +1]
    for dir in dirs:
        if topoMap[(nextDir := currentPos+dir)] == nextVal:
            scoreTrailHead(nextDir, nextVal+1, topoMap, accessible)

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
        cls.inputStrEx3 = importlib.resources.read_text(__package__, "inputEx3.txt")
        cls.inputStrEx4 = importlib.resources.read_text(__package__, "inputEx4.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 36)
    def testExample2Part1(self):
        self.assertEqual(part1(self.inputStrEx2), 2)
    def testExample3Part1(self):
        self.assertEqual(part1(self.inputStrEx3), 4)
    def testExample4Part1(self):
        self.assertEqual(part1(self.inputStrEx4), 3)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 81)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 794)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1706)