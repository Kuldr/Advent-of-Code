# ANSWER
def part1(inputStr):
    diskBlocks = parseInput(inputStr)

    diskBlocks = diskFragmenter(diskBlocks)

    results = [i * id for i, id in enumerate(diskBlocks) if id != "."]

    return sum(results)

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseInput(inputStr):
    diskBlocks = []
    for i, blocks in enumerate(inputStr):
        id = "." if i % 2 == 1 else i // 2
        for _ in range(int(blocks)):
            diskBlocks.append(id)
    
    return diskBlocks

def diskFragmenter(diskBlocks):
    frontPtr = 0
    backPtr = len(diskBlocks) - 1

    while diskBlocks[frontPtr] != ".":
            frontPtr += 1
    while diskBlocks[backPtr] == ".":
        backPtr -= 1

    while frontPtr < backPtr:
        diskBlocks[frontPtr], diskBlocks[backPtr] = diskBlocks[backPtr], diskBlocks[frontPtr]

        while diskBlocks[frontPtr] != ".":
            frontPtr += 1
        while diskBlocks[backPtr] == ".":
            backPtr -= 1
          
    return diskBlocks

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")

    # Example tests   
    def testExampleParse(self):
        self.assertEqual("".join(map(str, parseInput(self.inputStrEx))), "00...111...2...333.44.5555.6666.777.888899")
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 1928)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 2858)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 6341711060162)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)