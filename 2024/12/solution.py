# 1304764
def part1(inputStr):
    plots, maxX, maxY = parseInput(inputStr)

    regions = findRegions(plots, maxX, maxY)

    return sum([fenceCost(region) for region in regions])

# 811148
def part2(inputStr):
    plots, maxX, maxY = parseInput(inputStr)

    regions = findRegions(plots, maxX, maxY)

    return sum([fenceCostDiscount(region) for region in regions])

def parseInput(inputStr):
    from collections import defaultdict
    plots = defaultdict(lambda : "")
    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            plots[complex(x, -y)] = char

    return plots, x, y

def findRegions(plots, maxX, maxY):
    regions = []
    visited = set()

    dirs = [+1j, -1j, +1, -1]
    for x in range(maxX + 1):
        for y in range(0, -maxY - 1, -1):
            curr = complex(x, y)
            if curr not in visited and plots[curr] != "":
                visited.add(curr)
                toSearch = [curr + dir for dir in dirs]
                currVal = plots[curr]
                region = [curr]

                for coord in toSearch:
                    if plots[coord] == currVal and coord not in visited:
                        visited.add(coord)
                        region.append(coord)
                        for dir in dirs:
                            toSearch.append(coord + dir)
                
                regions.append(region)
    
    return regions

def fenceCost(region):
    area = len(region)

    perimeter = 0
    dirs = [+1j, -1j, +1, -1]
    for coord in region:
        for dir in dirs:
            if coord + dir not in region:
                perimeter += 1

    return area * perimeter

def fenceCostDiscount(region):
    area = len(region)
    sides = 0

    # Check Left sides
    visited = set()
    dir = -1 # Left
    for coord in region:
        if coord in visited:
            continue
        visited.add(coord)

        if coord + dir not in region:
            sides += 1
            # Check for side continuation
            newCoord = coord
            while (newCoord := newCoord + 1j) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break
            newCoord = coord
            while (newCoord := newCoord - 1j) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break

    # Check Right sides
    visited = set()
    dir = +1 # Right
    for coord in region:
        if coord in visited:
            continue
        visited.add(coord)

        if coord + dir not in region:
            sides += 1
            # Check for side continuation
            newCoord = coord
            while (newCoord := newCoord + 1j) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break
            newCoord = coord
            while (newCoord := newCoord - 1j) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break

    # Check Up sides
    visited = set()
    dir = +1j # Up
    for coord in region:
        if coord in visited:
            continue
        visited.add(coord)

        if coord + dir not in region:
            sides += 1
            # Check for side continuation
            newCoord = coord
            while (newCoord := newCoord + 1) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break
            newCoord = coord
            while (newCoord := newCoord - 1) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break
        
    # Check Down sides
    visited = set()
    dir = -1j # Down
    for coord in region:
        if coord in visited:
            continue
        visited.add(coord)

        if coord + dir not in region:
            sides += 1
            # Check for side continuation
            newCoord = coord
            while (newCoord := newCoord + 1) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break
            newCoord = coord
            while (newCoord := newCoord - 1) in region:
                visited.add(newCoord)
                if newCoord + dir in region:
                    break

    return area * sides

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
        self.assertEqual(part1(self.inputStrEx), 140)
    def testExample2Part1(self):
        self.assertEqual(part1(self.inputStrEx2), 772)
    def testExample3Part1(self):
        self.assertEqual(part1(self.inputStrEx3), 1930)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 80)
    def testExample2Part2(self):
        self.assertEqual(part2(self.inputStrEx2), 436)
    def testExample3Part2(self):
        self.assertEqual(part2(self.inputStrEx3), 1206)
    def testExample4Part2(self):
        self.assertEqual(part2(self.inputStrEx4), 368)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1304764)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 811148)

if __name__ == "__main__":
    import runpy
    import os
    import sys

    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.getcwd())
    sys.path.insert(0, os.path.join(parent_dir, 'Advent-of-Code'))

    # Run the script
    runpy.run_path("main.py")