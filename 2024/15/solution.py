# 1448589
def part1(inputStr):
    grid, moves, maxX, maxY = parseInput(inputStr, True)
    grid = itterateRobot(grid, moves)

    return gpsSum(grid)
    
# 1472235
def part2(inputStr):            
    grid, moves, maxX, maxY = parseInput(inputStr, False)
    grid = itterateRobot(grid, moves)

    return gpsSum(grid)

def gpsSum(grid):
    gpsCoords = [100 * coord.imag + coord.real for coord, char in grid.items() if char == "[" or char == "O"]
    
    return sum(gpsCoords)

def itterateRobot(grid, moves):
    robotCoord = [coord for coord, char in grid.items() if char == "@"][0]

    dirs = {"^": -1j, "v": +1j, "<": -1, ">": +1}
    for move in moves:
        canSwap, toSwap = gridMove(grid, robotCoord, (dir := dirs[move]), {})
        if canSwap:
            robotCoord += dir # Move the robot pointer
            for coord in toSwap.keys(): # Replace the old tiles
                grid[coord-dir] = "."
            for coord, char in toSwap.items(): # Add the new tiles
                grid[coord] = char
    
    return grid

def printGrid(grid, maxX, maxY):
    print()
    for y in range(maxY):
        for x in range(maxX):
            print(grid[complex(x, y)], end="")
        print()

def parseInput(inputStr, part1):
    gridStr, movesStr = inputStr.split("\n\n")

    moves = movesStr.replace("\n", "")
    
    grid = {}
    for y, line in enumerate(gridStr.split("\n")):
        for x, char in enumerate(line):
            if part1:
                grid[complex(x, y)] = char
            else:
                match char:
                    case "#":
                        grid[complex(2*x, y)] = "#"
                        grid[complex(2*x+1, y)] = "#"
                    case "O":
                        grid[complex(2*x, y)] = "["
                        grid[complex(2*x+1, y)] = "]"
                    case ".":
                        grid[complex(2*x, y)] = "."
                        grid[complex(2*x+1, y)] = "."
                    case "@":
                        grid[complex(2*x, y)] = "@"
                        grid[complex(2*x+1, y)] = "."

    
    return grid, moves, 2*(x+1), y+1

def gridMove(grid, coord, dir, toSwap):
    if coord + dir in toSwap:
        return True, toSwap
    else:
        match grid[nextCoord := coord + dir]:
            case ".":
                # Swap
                toSwap[nextCoord] = grid[coord]
                return True, toSwap
            case "O":
                # Check Next
                toSwap[nextCoord] = grid[coord]
                return gridMove(grid, nextCoord, dir, toSwap)
            case "[":
                # Check Next
                toSwap[nextCoord] = grid[coord]
                leftCheck, toSwap = gridMove(grid, nextCoord, dir, toSwap)
                rightCheck, toSwap = gridMove(grid, nextCoord+1, dir, toSwap)
                return leftCheck and rightCheck, toSwap
            case "]":
                # Check Next
                toSwap[nextCoord] = grid[coord]
                rightCheck, toSwap = gridMove(grid, nextCoord, dir, toSwap)
                leftCheck, toSwap = gridMove(grid, nextCoord-1, dir, toSwap)
                return leftCheck and rightCheck, toSwap
            case "#":
                # Can't swap
                return False, toSwap

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
        cls.inputStrCus = importlib.resources.read_text(__package__, "inputCustom.txt")
        cls.inputStrCus2 = importlib.resources.read_text(__package__, "inputCustom2.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 10092)
    def testExample2Part1(self):
        self.assertEqual(part1(self.inputStrEx2), 2028)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 9021)
    def testCustomPart2(self):
        self.assertEqual(part2(self.inputStrCus), 102)
    def testCustom2Part2(self):
        self.assertEqual(part2(self.inputStrCus2), 304)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1448589)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1472235)

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