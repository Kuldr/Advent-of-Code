# 2512
def part1(inputStr):
    return sum([game for game, gameStr in enumerate(inputStr.split("\n"), 1) if gamePossible(gameStr)])

# 67335
def part2(inputStr):
    from math import prod
    return sum([prod(minPossible(gameStr).values()) for gameStr in inputStr.split("\n")])

def minPossible(gameStr):
    import re
    regex = re.compile("(?:(\d*) (red|green|blue))[;, ]*")
    results = regex.findall(gameStr)

    minBalls = {"red":0, "green":0, "blue":0}
    for num, colour in results:
        if minBalls[colour] < (num := int(num)):
            minBalls[colour] = num
    
    return minBalls

def gamePossible(gameStr):
    maxValues = {"red":12, "green":13, "blue":14}
    minBalls = minPossible(gameStr)

    for colour in maxValues.keys():
        if minBalls[colour] > maxValues[colour]:
            return False
    return True

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
        self.assertEqual(part1(self.inputStrEx), 8)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 2286)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2512)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 67335)