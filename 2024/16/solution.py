# 93436
def part1(inputStr):
    grid, start, end = parseInput(inputStr)
    dir = +1
    score = 0

    visited = set() #set((start, dir))
    toTry = [] # [(coord: complex, dir: complex, score: int)]
    toTry.append((start, dir, 0))

    while toTry:
        toTry = [(coord, dir, score) for coord, dir, score in toTry if (coord, dir) not in visited]
        toTry = sorted(toTry, key=lambda x: x[2]) # Sort the list by score
        
        coord, dir, score = toTry.pop(0)
        if coord == end:
            return score
        
        visited.add((coord, dir))
        if grid[coord + dir] != "#":
            toTry.append((coord+dir, dir, score+1))
        if grid[coord + dir*1j] != "#":
            toTry.append((coord+dir*1j, dir*1j, score+1001))
        if grid[coord + dir*-1j] != "#":
            toTry.append((coord+dir*-1j, dir*-1j, score+1001))

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseInput(inputStr):
    start = complex(0,0)
    end = complex(0,0)
    from collections import defaultdict
    grid = defaultdict(lambda: "#")

    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            grid[complex(x, -y)] = char
            if char == "S":
                start = complex(x, -y)
            elif char == "E":
                end = complex(x, -y)

    return grid, start, end

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
        self.assertEqual(part1(self.inputStrEx), 7036)
    def testExample2Part1(self):
        self.assertEqual(part1(self.inputStrEx2), 11048)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 45)
    def testExample2Part2(self):
        self.assertEqual(part2(self.inputStrEx2), 64)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 93436)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)

# Run Main ------------------------------------------
if __name__ == "__main__":
    import runpy
    import os
    import sys

    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.getcwd())
    sys.path.insert(0, os.path.join(parent_dir, 'Advent-of-Code'))

    # Run the script
    runpy.run_path("main.py")