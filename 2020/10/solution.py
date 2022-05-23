# 2263
def part1(inputStr):
    adapters = parseInput(inputStr)
    differences = [y - x for x, y in zip(adapters, adapters[1:])]
    return differences.count(1)*differences.count(3)

# 396857386627072
def part2(inputStr):
    global knownJumps
    knownJumps = {}
    adapters = parseInput(inputStr)   
    return possibleNextPaths(0, adapters[-1], adapters)

def parseInput(inputStr):
    adapters = [0] + sorted(list(map(int, inputStr.split('\n'))))
    laptopRating = adapters[-1]+3
    adapters.append(laptopRating)
    return adapters

def possibleNextPaths(current, goal, adapters):
        global knownJumps
        if current == goal:
            return 1
        elif current in knownJumps:
            return knownJumps[current]
        
        temp = 0
        if current + 1 in adapters:
            temp = temp + possibleNextPaths(current + 1, goal, adapters)
        if current + 2 in adapters:
            temp = temp + possibleNextPaths(current + 2, goal, adapters)
        if current + 3 in adapters:
            temp = temp + possibleNextPaths(current + 3, goal, adapters)

        knownJumps[current] = temp
        return temp

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
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 35)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 8)

    # Example tests 2   
    def testExample2Part1(self):
        self.assertEqual(part1(self.inputStrEx2), 220)
    def testExample2Part2(self):
        self.assertEqual(part2(self.inputStrEx2), 19208)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2263)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 396857386627072)