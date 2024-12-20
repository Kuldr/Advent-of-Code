# ANSWER
def part1(inputStr):
    parseInput(inputStr)
    raise NotImplementedError("Part 1")

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseInput(inputStr):
    raise NotImplementedError("Parse Input")

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
        self.assertEqual(part1(self.inputStrEx), 0)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 0)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)

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