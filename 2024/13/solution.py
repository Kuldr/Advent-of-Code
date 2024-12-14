# 36954
def part1(inputStr):
    machines = parseInput(inputStr)

    # return bruteForceSolve(machines, 100)
    return sum([bruteForceSolve(machine, 100) for machine in machines])

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseInput(inputStr):
    import re
    findMachines = re.compile(r"Button A: X\+([\d]+), Y\+([\d]+)\nButton B: X\+([\d]+), Y\+([\d]+)\nPrize: X=([\d]+), Y=([\d]+)")

    # (aX, aY, bX, bY, targetX, targetY)
    machines = findMachines.findall(inputStr)
    machines = [(int(aX), int(aY), int(bX), int(bY), int(targetX), int(targetY)) for (aX, aY, bX, bY, targetX, targetY) in machines]

    return machines

def bruteForceSolve(machine, steps):
    (aX, aY, bX, bY, targetX, targetY) = machine
    steps += 1
    from itertools import product
    for a, b in product(range(steps), repeat = 2):
        if targetX == aX * a + bX * b and targetY == aY * a + bY * b:
            return 3 * a + b
    
    return 0
                break

    return totalCost

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
        self.assertEqual(part1(self.inputStrEx), 480)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 36954)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)

if __name__ == "__main__":
    import runpy
    import os
    import sys

    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.getcwd())
    sys.path.insert(0, os.path.join(parent_dir, 'Advent-of-Code'))

    # Run the script
    runpy.run_path("main.py")