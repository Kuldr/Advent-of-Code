# 93436
def part1(inputStr):
    grid, start, end, maxX, maxY = parseInput(inputStr)
    dir = +1
    score = 0

    visited = set()
    toTry = [] # [(coord: complex, dir: complex, score: int, previous: [coords])]
    toTry.append((start, dir, 0, []))

    while toTry:
        toTry = [(coord, dir, score, previous) for coord, dir, score, previous in toTry if (coord, dir) not in visited]
        toTry = sorted(toTry, key=lambda x: x[2]) # Sort the list by score
        
        coord, dir, score, previous = toTry.pop(0)
        if coord == end:
            break
        
        visited.add((coord, dir))
        if grid[(newCoord := coord + dir)] != "#":
            toTry.append((newCoord, dir, score+1, previous + [coord]))
        if grid[coord + (newDir := dir*1j)] != "#":
            toTry.append((coord+newDir, newDir, score+1001, previous + [coord]))
        if grid[coord + (newDir := dir*-1j)] != "#":
            toTry.append((coord+newDir, newDir, score+1001, previous + [coord]))
    
    # for coord in previous:
    #     grid[coord] = "O"
    # printGrid(grid, maxX, maxY)
    return score

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

    return grid, start, end, x+1, y+1

def printGrid(grid, maxX, maxY):
    print()
    for y in range(maxY):
        for x in range(maxX):
            print(grid[complex(x, -y)], end="")
        print()

def calcHeuristic(coord, end):
    return abs(end.real - coord.real) + abs(end.imag - coord.imag)

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
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 45)
    # def testExample2Part2(self):
    #     self.assertEqual(part2(self.inputStrEx2), 64)

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