# 1172
def part1(inputStr):
    dirs = parseInput(inputStr)
    dialPos = 50
    count = 0

    for dir in dirs:
        dialPos = (dialPos + dir) % 100
        if dialPos == 0:
            count += 1

    return count

# 6932
def part2(inputStr):
    dirs = parseInput(inputStr)
    dialPos = 50
    count = 0

    # Counting clicks step by step
    # for dir in dirs:
    #     for _ in range(abs(dir)):
    #         dialPos += (1 if dir > 0 else -1)
    #         if (dialPos := dialPos % 100) == 0:
    #             count += 1

    for dir in dirs:
        if dir > 0:
            dialPos += dir
            count += dialPos // 100
            dialPos %= 100
        else:
            if dialPos == 0: # Avoid double count when starting at 0
                count -= 1
            dialPos += dir
            count += abs(dialPos // 100) 
            dialPos %= 100
            if dialPos == 0: # Add double count when ending at 0
                count += 1

    return count

def parseInput(inputStr):
    import re
    regex = re.compile(r"([R|L])(\d+)")
    results = regex.findall(inputStr)
    return [-int(num) if LR == "L" else int(num) for LR, num in results]

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
        self.assertEqual(part1(self.inputStrEx), 3)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 6)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1172)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 6932)

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