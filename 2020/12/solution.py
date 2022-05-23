# 796
def part1(inputStr):
    directions = parseInput(inputStr)

    xPos = 0
    yPos = 0
    facing = 'E'

    for d, v in directions:
        if d in ['N', 'E', 'S', 'W']:
            xPos, yPos = addDirection(d, v, xPos, yPos)
        elif d == 'F':
            xPos, yPos = addDirection(facing, v, xPos, yPos)
        elif d == 'R':
            facing = rotateRight(v//90, facing)
        elif d == 'L':
            facing = rotateRight(-v//90, facing)

    return abs(xPos) + abs(yPos)

# 39446
def part2(inputStr):
    directions = parseInput(inputStr)

    xPosShip = 0
    yPosShip = 0
    xPosWayPoint = 10
    yPosWayPoint = 1

    for d, v in directions:
        if d in ['N', 'E', 'S', 'W']:
            xPosWayPoint, yPosWayPoint = addDirectionWayPoint(d, v, xPosWayPoint, yPosWayPoint)
        elif d == 'F':
            xPosShip += xPosWayPoint * v
            yPosShip += yPosWayPoint * v
        elif d == 'R':
            xPosWayPoint, yPosWayPoint = rotateRightWayPoint(v//90, xPosWayPoint, yPosWayPoint)
        elif d == 'L':
            xPosWayPoint, yPosWayPoint = rotateRightWayPoint(4-(v//90), xPosWayPoint, yPosWayPoint)

    return abs(xPosShip) + abs(yPosShip)

def parseInput(inputStr):
    return [(x[0], int(x[1:])) for x in inputStr.split('\n')]

def addDirection(d, v, xPos, yPos):
    if d == 'N':
        yPos += v
    elif d == 'S':
        yPos -= v
    elif d == 'E':
        xPos += v
    elif d == 'W':
        xPos -= v
    return xPos, yPos

def rotateRight(steps, facing):
    if facing == 'N':
        facing = ['N', 'E', 'S', 'W'][steps]
    elif facing == 'E':
        facing = ['E', 'S', 'W', 'N'][steps]
    elif facing == 'S':
        facing = ['S', 'W', 'N', 'E'][steps]
    elif facing == 'W':
        facing = ['W', 'N', 'E', 'S'][steps]
    return facing

def addDirectionWayPoint(d, v, xPosWayPoint, yPosWayPoint):
    if d == 'N':
        yPosWayPoint += v
    elif d == 'S':
        yPosWayPoint -= v
    elif d == 'E':
        xPosWayPoint += v
    elif d == 'W':
        xPosWayPoint -= v
    return  xPosWayPoint, yPosWayPoint

def rotateRightWayPoint(steps, xPosWayPoint, yPosWayPoint):
    for _ in range(steps):
        yPosWayPoint, xPosWayPoint = -xPosWayPoint, yPosWayPoint
    return  xPosWayPoint, yPosWayPoint

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
        self.assertEqual(part1(self.inputStrEx), 25)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 286)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 796)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 39446)