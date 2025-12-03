# 31210613313
def part1(inputStr):
    ranges = parseInput(inputStr)
    sumInvalid = 0
    
    for start, end in ranges:
        for ID in range(start, end + 1):
            strID = str(ID)
            lenID = len(strID)
            if lenID % 2 == 0 and strID[:lenID//2] == strID[lenID//2:]:
                sumInvalid += ID
    
    return sumInvalid

# 41823587546
def part2(inputStr):
    ranges = parseInput(inputStr)
    sumInvalid = 0
    
    for start, end in ranges:
        for ID in range(start, end + 1):
            strID = str(ID)
            lenID = len(strID)
            for x in range(2,lenID+1):
                if lenID % x == 0 and strID[:lenID//x]*x == strID:
                    sumInvalid += ID
                    # Only count each invalid ID once
                    # 222222 is 2*6 and 22*3 and 222*2
                    break
    
    return sumInvalid

def parseInput(inputStr):
    import re
    regex = re.compile(r"(\d+)-(\d+)")
    results = regex.findall(inputStr)

    results = [(int(s), int(e)) for s, e in results]

    return results

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
        self.assertEqual(part1(self.inputStrEx), 1227775554)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 4174379265)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 31210613313)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 41823587546)

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