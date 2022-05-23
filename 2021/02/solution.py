# 1936494
def part1(inputStr):
	horizontal = 0
	depth = 0

	commands = parseInput(inputStr)
	for command, val in commands:
		if command == "forward":
			horizontal += val
		elif command == "down":
			depth += val
		elif command == "up":
			depth -= val
	
	return depth * horizontal

# 1997106066
def part2(inputStr):
	horizontal = 0
	depth = 0
	aim = 0

	commands = parseInput(inputStr)
	for command, val in commands:
		if command == "forward":
			horizontal += val
			depth += aim * val
		elif command == "down":
			aim += val
		elif command == "up":
			aim -= val
	
	return depth * horizontal

def parseInput(inputStr):
	commands = []
	for line in inputStr.split('\n'):
		command, valStr = line.split(' ')
		commands.append((command, int(valStr)))
	return commands
	
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
        self.assertEqual(part1(self.inputStrEx), 150)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 900)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1936494)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1997106066)