# 185894
def part1(inputStr):
    stones = parseInput(inputStr)
    
    # # Old Version
    # for _ in range(25):
    #     stones = blink(stones)
    # return len(stones)

    return sum([blinkSingeStone(stone, 25) for stone in stones])

# 221632504974231
def part2(inputStr):
    stones = parseInput(inputStr)

    return sum([blinkSingeStone(stone, 75) for stone in stones])

def parseInput(inputStr):
    return [int(num) for num in inputStr.split(" ")]

def blink(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif (lenStrStone := len(strStone := str(stone))) % 2 == 0:
            newStones.append(int(strStone[:lenStrStone//2]))
            newStones.append(int(strStone[lenStrStone//2:]))
        else:
            newStones.append(stone*2024)

    return newStones

from functools import cache
@cache
def blinkSingeStone(stone, repeat):
    if repeat == 0:
        return 1
    if stone == 0:
        return blinkSingeStone(1, repeat-1)
    elif (lenStrStone := len(strStone := str(stone))) % 2 == 0:
        lStone, rStone = int(strStone[:lenStrStone//2]), int(strStone[lenStrStone//2:])
        return blinkSingeStone(lStone, repeat-1) + blinkSingeStone(rStone, repeat-1)
    else:
        return blinkSingeStone(stone*2024, repeat-1)

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
        self.assertEqual(part1(self.inputStrEx), 55312)
    def testExampleBlink(self):
        self.assertEqual(blink([0,1,10,99,999]), [1,2024,1,0,9,9,2021976])

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 185894)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 221632504974231)