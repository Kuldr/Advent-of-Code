import operator

# 3647606140187
def part1(inputStr):
	return sum(map(flattenNewMath, parseInput(inputStr)))

# 323802071857594
def part2(inputStr):
	return sum(map(flattenAdvancedMath, parseInput(inputStr)))

def parseInput(inputStr):
	parsedInput = inputStr.split("\n")
	parsedInput = map(lambda s:s.replace("(", "( "), parsedInput)
	parsedInput = map(lambda s:s.replace(")", " )"), parsedInput)
	parsedInput = map(lambda s:s.split(" "), parsedInput)

	return parsedInput
	
def evaluateNewMath(expression)	:
    result = 0
    currentOp = operator.add
    for i in expression:
        if i == "+":
            currentOp = operator.add
        elif i == "*":
            currentOp = operator.mul
        else:
            result = currentOp(result, int(i))
    return result

def flattenNewMath(expression):
    if "(" not in expression:
        return evaluateNewMath(expression)
    index = 0
    while index < len(expression):
        if expression[index] == "(":
            openCount = 1
            for i, x in enumerate(expression[index+1:]):
                if x == "(":
                    openCount += 1
                elif x == ")":
                    openCount -= 1
                if openCount == 0:
                    return flattenNewMath(expression[:index] +\
	                        [flattenNewMath(expression[index+1:index+1+i])] +\
                            expression[index+2+i:])
        index += 1
		
def evaluateAdvancedMath(expression):
    if "+" in expression:
        plusIndex = expression.index("+")
        return evaluateAdvancedMath(expression[:plusIndex-1] + 
               [int(expression[plusIndex-1]) + int(expression[plusIndex+1])] +
               expression[plusIndex+2:])
    elif "*" in expression:
        mulIndex = expression.index("*")
        return evaluateAdvancedMath(expression[:mulIndex-1] + 
               [int(expression[mulIndex-1]) * int(expression[mulIndex+1])] +
               expression[mulIndex+2:])
    else:
        return int(expression[0])

def flattenAdvancedMath(expression):
    if "(" not in expression:
        return evaluateAdvancedMath(expression)
    index = 0
    while index < len(expression):
        if expression[index] == "(":
            openCount = 1
            for i, x in enumerate(expression[index+1:]):
                if x == "(":
                    openCount += 1
                elif x == ")":
                    openCount -= 1
                if openCount == 0:
                    return flattenAdvancedMath(expression[:index] +\
                            [flattenAdvancedMath(expression[index+1:index+1+i])] +\
	                        expression[index+2+i:])
        index += 1
		
# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
		cls.inputStrEx2 = "1 + (2 * 3) + (4 * (5 + 6))"
		cls.inputStrEx3 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
		cls.inputStrEx4 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
		cls.inputStrEx5 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
	def testExamplePart1(self):
		self.assertEqual(part1(self.inputStrEx), 71)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx), 231)
	def testExample2Part1(self):
		self.assertEqual(part1(self.inputStrEx2), 51)
	def testExample2Part2(self):
		self.assertEqual(part2(self.inputStrEx2), 51)
	def testExample3Part1(self):
		self.assertEqual(part1(self.inputStrEx3), 437)
	def testExample3Part2(self):
		self.assertEqual(part2(self.inputStrEx3), 1445)
	def testExample4Part1(self):
		self.assertEqual(part1(self.inputStrEx4), 12240)
	def testExample4Part2(self):
		self.assertEqual(part2(self.inputStrEx4), 669060)
	def testExample5Part1(self):
		self.assertEqual(part1(self.inputStrEx5), 13632)
	def testExample5Part2(self):
		self.assertEqual(part2(self.inputStrEx5), 23340)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 3647606140187)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 323802071857594)