# 111627841
def part1(inputStr):
    seeds, maps = parseInput(inputStr)
    answers = [seedToLocation(seed, maps) for seed in seeds]
    return min(answers)

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseInput(inputStr):
    mapStrs = inputStr.split("\n\n")

    seeds = numbersFromString(mapStrs[0])
    maps = []
    for mapStr in mapStrs[1:]: 
        nextMap = {}
        for line in mapStr.split("\n")[1:]:
            destStart, srcStart, rangeLength = numbersFromString(line)
            nextMap[range(srcStart, srcStart+rangeLength)] = destStart - srcStart
            # for x in range(rangeLength):
            #     nextMap[srcStart + x] = destStart + x
        maps.append(nextMap)
    
    return seeds, maps

def seedToLocation(seed, maps):
    current = seed
    for mapping in maps:
        for key, diff in mapping.items():
            if current in key:
                current += diff
                break
    
    return current
    
def numbersFromString(str):
    import re
    numbersRegex = re.compile(r"(\d+)")

    return map(int, numbersRegex.findall(str))

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
        self.assertEqual(part1(self.inputStrEx), 35)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 111627841)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)