# 413733
def part1(inputStr):
	brackets = {'(':')', '[':']', '{':'}', '<':'>'}
	points = {")": 3, "]": 57, "}": 1197, ">": 25137}

	score = 0
	for line in inputStr.split('\n'):
		syntaxStack = []
		for char in line: 
			if char in brackets.keys():
				syntaxStack.append(char)
			elif char in brackets.values():
				expected = brackets[syntaxStack[-1]]
				if char != expected:
					# print(f"Expected {expected}, but found {char} instead.")
					score += points[char]
					break
				else:
					syntaxStack.pop(-1)
	return score

# 3354640192
def part2(inputStr):
	brackets = {'(':')', '[':']', '{':'}', '<':'>'}
	points = {"(": 1, "[": 2, "{": 3, "<": 4}
	scores = []

	for line in inputStr.split('\n'):
		syntaxStack = []
		for char in line: 
			validLine = True
			if char in brackets.keys():
				syntaxStack.append(char)
			elif char in brackets.values():
				expected = brackets[syntaxStack[-1]]
				if char != expected:
					# print(f"Expected {expected}, but found {char} instead.")
					validLine = False
					break
				else:
					syntaxStack.pop(-1)
		if validLine:
			# Go backwards through the stack
			# syntaxStack.reverse()
			score = 0
			for char in syntaxStack[::-1]:
				score *= 5
				score += points[char]
			scores.append(score)

	scores.sort()
	return scores[len(scores)//2]

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
        self.assertEqual(part1(self.inputStrEx), 26397)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 288957)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 413733)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 3354640192)