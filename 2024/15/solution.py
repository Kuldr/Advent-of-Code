# 1448589
def part1(inputStr):
    grid, moves, maxX, maxY = parseInput(inputStr)

    robotCoord = [coord for coord, char in grid.items() if char == "@"][0]

    dirs = {"^": -1j, "v": +1j, "<": -1, ">": +1}
    for move in moves:
        canSwap, toSwap = gridMove(grid, robotCoord, dirs[move], {})
        if canSwap:
            robotCoord += dirs[move]
            for coord in toSwap.keys():
                grid[coord-dirs[move]] = "."
            for coord, char in toSwap.items():
                grid[coord] = char

    # printGrid(grid, maxX, maxY)

    gpsCoords = [100 * coord.imag + coord.real for coord, char in grid.items() if char == "O"]
    
    return sum(gpsCoords)
    
# 1472235
def part2(inputStr):            
    grid, moves, maxX, maxY = parseInput2(inputStr)

    robotCoord = [coord for coord, char in grid.items() if char == "@"][0]

    dirs = {"^": -1j, "v": +1j, "<": -1, ">": +1}
    for i, move in enumerate(moves):
        canSwap, toSwap = gridMove2(grid, robotCoord, dirs[move], {})
        if canSwap:
            robotCoord += dirs[move]
            for coord in toSwap.keys():
                grid[coord-dirs[move]] = "."
            for coord, char in toSwap.items():
                grid[coord] = char

    # printGrid(grid, maxX, maxY)

    gpsCoords = [100 * coord.imag + coord.real for coord, char in grid.items() if char == "["]
    
    return sum(gpsCoords)

def printGrid(grid, maxX, maxY):
    print()
    for y in range(maxY):
        for x in range(maxX):
            print(grid[complex(x, y)], end="")
        print()

def parseInput(inputStr):
    gridStr, movesStr = inputStr.split("\n\n")

    moves = movesStr.replace("\n", "")
    
    grid = {}
    for y, line in enumerate(gridStr.split("\n")):
        for x, char in enumerate(line):
            grid[complex(x, y)] = char
    
    return grid, moves, x+1, y+1

def parseInput2(inputStr):
    gridStr, movesStr = inputStr.split("\n\n")

    moves = movesStr.replace("\n", "")
    
    grid = {}
    for y, line in enumerate(gridStr.split("\n")):
        for x, char in enumerate(line):
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
    match grid[nextCoord := coord + dir]:
        case ".":
            # Swap
            toSwap[nextCoord] = grid[coord]
            return True, toSwap
        case "O":
            # Check Next
            toSwap[nextCoord] = grid[coord]
            return gridMove(grid, nextCoord, dir, toSwap)
        case "#":
            # Can't swap
            return False, toSwap

def gridMove2(grid, coord, dir, toSwap):
    # Might be able to clear up the if with recursion loop checking
    if dir == -1 or dir == +1: # Horizontal Movement
        match grid[nextCoord := coord + dir]:
            case ".":
                # Swap
                toSwap[nextCoord] = grid[coord]
                return True, toSwap
            case "[" | "]":
                # Check Next
                toSwap[nextCoord] = grid[coord]
                return gridMove2(grid, nextCoord, dir, toSwap)
            case "#":
                # Can't swap
                return False, toSwap
    else: # Vertical Movement
        match grid[nextCoord := coord + dir]:
            case ".":
                # Swap
                toSwap[nextCoord] = grid[coord]
                return True, toSwap
            case "[":
                # Check Next
                toSwap[nextCoord] = grid[coord]
                leftCheck, toSwap = gridMove2(grid, nextCoord, dir, toSwap)
                rightCheck, toSwap = gridMove2(grid, nextCoord+1, dir, toSwap)
                return leftCheck and rightCheck, toSwap
            case "]":
                # Check Next
                toSwap[nextCoord] = grid[coord]
                rightCheck, toSwap = gridMove2(grid, nextCoord, dir, toSwap)
                leftCheck, toSwap = gridMove2(grid, nextCoord-1, dir, toSwap)
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