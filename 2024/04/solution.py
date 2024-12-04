# 2599
def part1(inputStr):
    grid, xMax, yMax = parseInput(inputStr)

    count = 0
    for y in range(yMax+1):
        for x in range(xMax+1):
            words = getWords(grid, x, y)
            count += words.count("XMAS")

    return count  
    
# 1948
def part2(inputStr):
    grid, xMax, yMax = parseInput(inputStr)

    count = 0
    for y in range(yMax+1):
        for x in range(xMax+1):
            words = getCross(grid, x, y)
            count += words.count("MASMS")

    return count  

def parseInput(inputStr):
    from collections import defaultdict

    grid = defaultdict(lambda : ".")
    for y, line in enumerate(inputStr.split("\n")):
        for x, character in enumerate(line):
            grid[x+y*1j] = character

    return grid, x, y

def getWords(grid, x, y):
    # Optimisation to break early
    if grid[(coord := x+y*1j)] != "X":
        return []

    dirs = [-1-1j, 0-1j, 1-1j,
            -1+0j,       1+0j,
            -1+1j, 0+1j, 1+1j]
    
    words = []

    for dir in dirs:
        word = grid[x+y*1j] + grid[coord+dir] + grid[coord+2*dir] + grid[coord+3*dir]
        words.append(word)

    return words

def getCross(grid, x, y):
    # Optimisation to break early
    if grid[(coord := x+y*1j)] != "A":
        return []
    
    words = [grid[coord-1-1j] + grid[coord] + grid[coord+1+1j] + grid[coord+1-1j] + grid[coord-1+1j],
             grid[coord-1-1j] + grid[coord] + grid[coord+1+1j] + grid[coord-1+1j] + grid[coord+1-1j],
             grid[coord+1+1j] + grid[coord] + grid[coord-1-1j] + grid[coord-1+1j] + grid[coord+1-1j],
             grid[coord+1+1j] + grid[coord] + grid[coord-1-1j] + grid[coord+1-1j] + grid[coord-1+1j]]

    return words

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
        self.assertEqual(part1(self.inputStrEx), 18)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 9)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2599)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1948)