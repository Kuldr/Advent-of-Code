# 111627841
def part1(inputStr):
    seeds, maps = parseInput(inputStr)
    answers = [seedToLocation(seed, maps) for seed in seeds]
    return min(answers)

# ANSWER
def part2(inputStr):
    # Should work but will need to check 1945168946 seeds :(
    seeds, maps = parseInput(inputStr)
    seedRanges = parseSeedRanges(seeds)
    answers = [seedRangeToMinLocation(seedRange, maps) for seedRange in seedRanges]
    return min(answers)

def parseInput(inputStr):
    mapStrs = inputStr.split("\n\n")

    seeds = numbersFromString(mapStrs[0])
    maps = []
    for mapStr in mapStrs[1:]: 
        nextMap = {}
        for line in mapStr.split("\n")[1:]:
            destStart, srcStart, rangeLength = numbersFromString(line)
            nextMap[range(srcStart, srcStart+rangeLength)] = destStart - srcStart
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

def seedRangeToMinLocation(seedRange, maps):
    # Will need to consider the extreme values of the ranges and how they overlap with ranges in the map
    
    pass
    
def numbersFromString(str):
    import re
    numbersRegex = re.compile(r"(\d+)")

    return map(int, numbersRegex.findall(str))

def parseSeedRanges(seeds):
    seeds = list(seeds)
    pairs = zip(seeds[::2], seeds[1::2])
    seedRanges = []
    for start, length in pairs:
        seedRanges.append(range(start, start+length))
    return seedRanges

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
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 46)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 111627841)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 0)