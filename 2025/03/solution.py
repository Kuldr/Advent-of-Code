# 17193
def part1(inputStr):
    banks = parseInput(inputStr)
    return largestBatteryCombinations(banks, 2)

# ANSWER
def part2(inputStr):
    banks = parseInput(inputStr)
    return largestBatteryCombinations(banks, 12)

    # sumBatteries = 0

    # import re
    
    # from time import time
    # startTime = time()

    # for i in range(111_111_111_111, 999_999_999_999):
    #     # regex => (.*[9].*[9].*[9].*[9].*[9].*[9].*[9].*[9].*[9].*[9].*[9].*[9].*)
    #     regex = "(.*[" + "].*[".join(str(i)) + "].*)"
    #     if found := re.findall(regex, inputStr):
    #         sumBatteries += i
    #         inputStr = inputStr.replace(found[0], "")

def parseInput(inputStr):
    return [line for line in inputStr.split("\n")]

# Intractable for part 2 real 1.05E15 combos per bank
def largestBatteryCombinations(banks, cells):
    sumBatteries = 0

    from itertools import combinations
    for bank in banks:
        # As this builds the entire list first takes too much memory
        # Can remove the list comprehension and use combinations as iterator
        sumBatteries += max([int("".join(combo)) for combo in combinations(bank, cells)])

    return sumBatteries

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
        self.assertEqual(part1(self.inputStrEx), 357)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 3121910778619)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 17193)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 0)

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