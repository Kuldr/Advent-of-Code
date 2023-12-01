# 54708
def part1(inputStr):
    import string
    table = str.maketrans('', '', string.ascii_lowercase)
    words = inputStr.translate(table).split("\n")

    return sum([int(word[0]) * 10 + int(word[-1]) for word in words])

# 53432 too low
def part2(inputStr):
    import re
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, word in enumerate(nums):
        inputStr = re.sub(word, str(digit+1), inputStr)

    print(inputStr)

    import string
    table = str.maketrans('', '', string.ascii_lowercase)
    words = inputStr.translate(table).split("\n")

    return sum([int(word[0]) * 10 + int(word[-1]) for word in words])

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 142)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 142)
    def testExample2Part2(self):
        self.assertEqual(part2(self.inputStrEx2), 281)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 54708)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)