# 247
def part1(inputStr):
    antennas, maxX, maxY = parseInput(inputStr)

    antinodes = set()
    from itertools import combinations
    for sameAntennas in antennas.values():
        pairs = combinations(sameAntennas, 2)
        for a, b in pairs:
            diff = a - b
            if 0 <= (aDiff := a + diff).real <= maxX and 0 >= aDiff.imag >= -maxY:
                antinodes.add(aDiff)
            if 0 <= (bDiff := b - diff).real <= maxX and 0 >= bDiff.imag >= -maxY:
                antinodes.add(bDiff)

    return len(antinodes)

# 861
def part2(inputStr):
    antennas, maxX, maxY = parseInput(inputStr)

    antinodes = set()
    from itertools import combinations
    for sameAntennas in antennas.values():
        pairs = combinations(sameAntennas, 2)
        for a, b in pairs:
            diff = a - b
            count = 0
            while 0 <= (aDiff := a + count*diff).real <= maxX and 0 >= aDiff.imag >= -maxY:
                antinodes.add(aDiff)
                count += 1
            
            count = 0
            while 0 <= (bDiff := b - count*diff).real <= maxX and 0 >= bDiff.imag >= -maxY:
                antinodes.add(bDiff)
                count += 1

    return len(antinodes)

def parseInput(inputStr):
    from collections import defaultdict
    antennas = defaultdict(lambda : [])
    for y, line in enumerate(inputStr.split("\n")):
        for x, char in enumerate(line):
            if char != ".":
                antennas[char].append(complex(x, -y))

    return antennas, x, y

    

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
        self.assertEqual(part1(self.inputStrEx), 14)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 34)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 247)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 861)