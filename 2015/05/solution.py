import re

vowels3 = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
doubleLetter = re.compile(r"(.)\1")
disallowed = re.compile(r"^((?!(ab|cd|pq|xy)).)*$")
doublePair = re.compile(r"")
doubleLetterWGap = re.compile(r"")

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# 255
def part1(inputStr):
	counter = 0
	for line in inputStr.split("\n"):
		if naughtyOrNice(line, [vowels3, doubleLetter, disallowed]):
			counter += 1

	return counter

def naughtyOrNice(inputLine, tests):
	results = []
	for test in tests:
		results.append(test.search(inputLine))
	
	return all(results)

# ANSWER
def part2(inputStr):
	counter = 0
	for line in inputStr.split("\n"):
		if naughtyOrNice(line, [doublePair, doubleLetterWGap]):
			counter += 1

	return counter

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
        self.assertEqual(part1(self.inputStrEx), 2)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 255)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 0)