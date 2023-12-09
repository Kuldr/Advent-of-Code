# 316800
def part1(inputStr):
    import re
    numbersRegex = re.compile(r"(\d+)")
    nums = list(map(int, numbersRegex.findall(inputStr)))
    races = zip(nums[:len(nums)//2], nums[len(nums)//2:])

    from math import prod
    return prod([waysToBeat(*race) for race in races])

# 45647654
def part2(inputStr):
    import re
    numbersRegex = re.compile(r"(\d+)")
    nums = numbersRegex.findall(inputStr)

    time = int("".join(nums[:len(nums)//2]))
    record = int("".join(nums[len(nums)//2:]))

    return waysToBeat(time, record)
    

def waysToBeat(time, record):
    count = 0
    for timeHeld in range((time+1)):
        dist = timeHeld * (time-timeHeld)
        if dist > record:
            count += 1
    return count

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
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 71503)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 316800)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 45647654)