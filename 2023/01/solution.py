# 54708
def part1(inputStr):
    import string
    table = str.maketrans('', '', string.ascii_lowercase)
    words = inputStr.translate(table).split("\n")

    return sum([int(word[0]) * 10 + int(word[-1]) for word in words])

# 54087
def part2(inputStr):
    # Hacky solution for overlapping values
    import re
    nums = {"one":"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"n9e"}
    for word, digit in nums.items():
        inputStr = re.sub(word, str(digit), inputStr)

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
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 54087)