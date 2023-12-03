# 517021
def part1(inputStr):
    numberCoords = parseNumbers(inputStr)
    symbolCoords = parseSymbols(inputStr)

    partTotal = 0
    for symbolCoord in symbolCoords.keys():
        currentParts = set()
        for offset in [-1-1j,-1,-1+1j,-1j,+1j,+1-1j,+1,+1+1j]:
            currentParts.add(numberCoords[symbolCoord + offset])
        partTotal += sum(currentParts)

    return partTotal

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseSymbols(inputStr):
    import re
    symbolRegex = re.compile(r"([^\d|.|\n])")
    symbolCoords = {}

    for y, lineStr in enumerate(inputStr.split("\n")):
        symbolMatches = symbolRegex.finditer(lineStr)
        for symbol in symbolMatches:
            symbolCoords[complex(symbol.start(),y)] = symbol[0]
            # print(f"{symbol[0]} @ {symbol.start()}+{y}j")

    return symbolCoords

def parseNumbers(inputStr):
    import re
    numberRegex = re.compile(r"(\d+)")
    from collections import defaultdict
    numberCoords = defaultdict(lambda: 0) # 0 so none parts won't effect total

    for y, lineStr in enumerate(inputStr.split("\n")):
        numberMatches = numberRegex.finditer(lineStr)
        for number in numberMatches:
            for x in range(*number.span()): # Tuple unpacking to create range args
                numberCoords[complex(x, y)] = int(number[0])
                # print(f"{number[0]} @ {x}+{y}j")
    
    return numberCoords

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
        self.assertEqual(part1(self.inputStrEx), 4361)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 467835)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 517021)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)