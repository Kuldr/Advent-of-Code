# 21558
def part1(inputStr):
    return sum([scratchCardPoints(cardStr) for cardStr in inputStr.split("\n")])

# 10425665
def part2(inputStr):
    from collections import defaultdict
    copiesOfCard = defaultdict(lambda: 1)
    for cardNum, cardStr in enumerate(inputStr.split("\n"), start = 1):
        matches = scratchCardMatches(cardStr)
        copiesOfCard[cardNum] # Hit the defaultdict at least once to set it to 1 copy
        for x in range(1,matches+1):
            copiesOfCard[cardNum+x] += copiesOfCard[cardNum]

    return sum(copiesOfCard.values())

def scratchCardPoints(cardStr):
    matches = scratchCardMatches(cardStr)
    if matches == 0:
        return 0
    else:
        return 2**(matches-1)

def scratchCardMatches(cardStr):
    # Extract the 2 strings with numbers in
    numbersYouHaveStr, winningNumbersStr = cardStr.split(": ")[1].split("|")

    # Find all the numbers in each part
    import re
    numbersRegex = re.compile(r"(\d+)")
    numbersYouHave = set(numbersRegex.findall(numbersYouHaveStr))
    winningNumbers = set(numbersRegex.findall(winningNumbersStr))

    return len(numbersYouHave & winningNumbers)

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
        self.assertEqual(part1(self.inputStrEx), 13)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 30)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 21558)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 10425665)