# 17193
def part1(inputStr):
    banks = parseInput(inputStr)
    sumBatteries = 0

    from itertools import combinations
    for bank in banks:
        # sumBatteries += max([int(l+r) for l, r in combinations(bank, 2)])
        sumBatteries += max([int("".join(combo)) for combo in combinations(bank, 2)])

    return sumBatteries

# ANSWER
def part2(inputStr):
    banks = parseInput(inputStr)
    sumBatteries = 0

    # # Combinations method intractable 1.05E15 combos per bank
    # from itertools import combinations
    # for bank in banks:
    #     maxBattery = 0
    #     for combo in combinations(bank, 12):
    #         if (newBattery := int("".join(combo))) > maxBattery:
    #             maxBattery = newBattery
    #     sumBatteries += maxBattery

    #     # As this builds the entire list first takes too much memory
    #     # sumBatteries += max([int("".join(combo)) for combo in combinations(bank, 12)])

    return sumBatteries

def parseInput(inputStr):
    return [line for line in inputStr.split("\n")]

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