# 316800
def part1(inputStr):
    races = parseInput(inputStr)
    waysToBeatList = []
    for time, record in races:
        waysToBeat = 0
        for timeHeld in range(time+1):
            dist = timeHeld * (time-timeHeld)
            if dist > record:
                waysToBeat += 1
        waysToBeatList.append(waysToBeat)

    from math import prod
    return prod(waysToBeatList)

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseInput(inputStr):
    import re
    numbersRegex = re.compile(r"(\d+)")
    nums = list(map(int, numbersRegex.findall(inputStr)))
    return zip(nums[:len(nums)//2], nums[len(nums)//2:])

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
        self.assertEqual(part1(self.inputStrEx), 288)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 316800)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)