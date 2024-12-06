# 4711
def part1(inputStr):
    obstacles, gaurdPos, maxX, maxY = parseInput(inputStr)
    
    gaurdDir = 0-1j
    visitedPos = set()
    while 0 <= gaurdPos.real <= maxX and 0 <= gaurdPos.imag <= maxY:
        visitedPos.add(gaurdPos)
        if gaurdPos + gaurdDir in obstacles: # Turn Right
            gaurdDir *= 1j
        else:
            gaurdPos += gaurdDir

    return len(visitedPos)


# 1562
def part2(inputStr):
    obstacles, gaurdPos, maxX, maxY = parseInput(inputStr)

    newObstacles = [x+y*1j for x in range(maxX+1) for y in range(maxY+1)]

    loops = [newObstacle for newObstacle in newObstacles 
             if checkForLoop(obstacles.copy(), gaurdPos, maxX, maxY, newObstacle)]
    
    return len(loops)

def parseInput(inputStr):
    obstacles = set()
    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            match char:
                case "#":
                    obstacles.add(x+y*1j)
                case "^":
                    gaurdPos = x+y*1j

    return obstacles, gaurdPos, x, y 

def checkForLoop(obstacles, gaurdPos, maxX, maxY, newObstacle) -> bool:
    gaurdDir = 0-1j
    visitedPosAndDir = set()
    obstacles.add(newObstacle)
    
    while 0 <= gaurdPos.real <= maxX and 0 <= gaurdPos.imag <= maxY:
        visitedPosAndDir.add((gaurdPos, gaurdDir))
        if gaurdPos + gaurdDir in obstacles: # Turn Right
            gaurdDir *= 1j
        else:
            gaurdPos += gaurdDir
            if (gaurdPos, gaurdDir) in visitedPosAndDir:
                return True
    
    return False

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
        self.assertEqual(part1(self.inputStrEx), 41)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 6)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 4711)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1562)