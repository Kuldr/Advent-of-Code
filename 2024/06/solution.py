# 4711
def part1(inputStr):
    obstacles, gaurdPos, maxX, maxY = parseInput(inputStr)

    _, vistedPosAndDirs = checkForLoop(obstacles, gaurdPos, maxX, maxY)
    visitedPos = set(pos for pos, _ in vistedPosAndDirs)

    return len(visitedPos)

# 1562
def part2(inputStr):
    obstacles, gaurdPos, maxX, maxY = parseInput(inputStr)

    _, vistedPosAndDirs = checkForLoop(obstacles, gaurdPos, maxX, maxY)
    
    # Only consider new obstacles that the gaurd could walk into
    newObstacles = set(newPos for pos, dir in vistedPosAndDirs
                       if 0 <= (newPos := pos + dir).real <= maxX and 0 <= newPos.imag <= maxY)  
      
    newObstacles = newObstacles.difference(obstacles) # Remove all current obstacles to avoid dupes
    newObstacles = newObstacles.difference([gaurdPos]) # Remove gaurd position

    loops = [newObstacle for newObstacle in newObstacles 
             if checkForLoop(obstacles.union([newObstacle]), gaurdPos, maxX, maxY)[0]]
    
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

def checkForLoop(obstacles, gaurdPos, maxX, maxY) -> bool:
    gaurdDir = 0-1j
    visitedPosAndDir = set()
    
    while 0 <= gaurdPos.real <= maxX and 0 <= gaurdPos.imag <= maxY:
        visitedPosAndDir.add((gaurdPos, gaurdDir))
        if gaurdPos + gaurdDir in obstacles: # Turn Right
            gaurdDir *= 1j
        else:
            gaurdPos += gaurdDir
            if (gaurdPos, gaurdDir) in visitedPosAndDir:
                return True, visitedPosAndDir
    
    return False, visitedPosAndDir

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