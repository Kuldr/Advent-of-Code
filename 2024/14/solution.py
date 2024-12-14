# 222901875
def part1(inputStr):
    grid, maxX, maxY = parseInput(inputStr)

    for _ in range(100):
        grid = itterateGrid(grid, maxX, maxY)

    safetyFactor = 1
    for xRange, yRange in [(range(0, maxX//2), range(0, maxY//2)),
                           (range(maxX//2+1, maxX), range(0, maxY//2)),
                           (range(0, maxX//2), range(maxY//2+1, maxY)),
                           (range(maxX//2+1, maxX), range(maxY//2+1, maxY))]:
        currentScore = 0
        for x in xRange:
            for y in yRange:
                currentScore += len(grid[y][x])
        
        safetyFactor *= currentScore
                
    return safetyFactor

# 6243
def part2(inputStr):
    grid, maxX, maxY = parseInput(inputStr)
    file = open("2024/14/EasterEgg.txt", "w")
    for i in range(1, 101*103+1):
        grid = itterateGrid(grid, maxX, maxY)
        # print(f"{i/(101*103)*100}%")
        string = gridStr(grid)
        file.write(f"\n\n{i}\n")
        file.write(string)
        if "########" in string:
            return i

    print(i)
    file.close()

def parseInput(inputStr):
    import re

    guardsRE = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

    # (pX, pY, vX, vY)
    guards = guardsRE.findall(inputStr)
    guards = [(int(pX), int(pY), int(vX), int(vY)) for (pX, pY, vX, vY) in guards]
    
    if len(guards) == 12: # Example
        maxY = 7
        maxX = 11
    else: # Real
        maxY = 103
        maxX = 101

    grid = [[[] for _ in range(maxX)] for _ in range(maxY)]

    for (pX, pY, vX, vY) in guards:
        grid[pY][pX].append((vX, vY))

    return grid, maxX, maxY

def itterateGrid(grid, maxX, maxY):
    newGrid = [[[] for _ in range(maxX)] for _ in range(maxY)]
    for y, line in enumerate(grid):
        for x, guards in enumerate(line):
            for vX, vY in guards:
                newGrid[(y+vY)%maxY][(x+vX)%maxX].append((vX, vY))

    return newGrid

def gridStr(grid):
    string = ""
    for line in grid:
        for guards in line:
            if guards == []:
                string += "."
            else:
                string += "#"
        string += "\n"

    return string

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
        self.assertEqual(part1(self.inputStrEx), 12)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 222901875)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 6243)

if __name__ == "__main__":
    import runpy
    import os
    import sys

    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.getcwd())
    sys.path.insert(0, os.path.join(parent_dir, 'Advent-of-Code'))

    # Run the script
    runpy.run_path("main.py")