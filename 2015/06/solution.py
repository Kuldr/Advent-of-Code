# 400410
def part1(inputStr):
	from collections import defaultdict
	from operator import countOf
	grid = defaultdict(lambda: False)

	for command in inputStr.split("\n"):
		type, firstX, firstY, lastX, lastY = parseCommand(command)

		if type == "on":
			state = lambda x: True
		elif type == "off":
			state = lambda x: False
		elif type == "toggle":
			state = lambda x: not x

		for x in range(firstX, lastX+1):
			for y in range(firstY, lastY+1):
				grid[(x,y)] = state(grid[(x,y)])

	return countOf(grid.values(), True)
	
# 15343601
def part2(inputStr):
	from collections import defaultdict
	grid = defaultdict(lambda: 0)

	for command in inputStr.split("\n"):
		type, firstX, firstY, lastX, lastY = parseCommand(command)

		if type == "on":
			state = lambda x: x + 1
		elif type == "off":
			state = lambda x: a if (a := x - 1) > 0 else 0
		elif type == "toggle":
			state = lambda x: x + 2

		for x in range(firstX, lastX+1):
			for y in range(firstY, lastY+1):
				grid[(x,y)] = state(grid[(x,y)])

	return sum(grid.values())

def parseCommand(command):
	commands = command.split(" ")
	first = commands[-3].split(",")
	firstX = int(first[0])
	firstY = int(first[1])
	last = commands[-1].split(",")
	lastX = int(last[0])
	lastY = int(last[1])

	if "on" in commands:
		type = "on"
	elif "off" in commands:
		type = "off"
	elif "toggle" in commands:
		type = "toggle"

	return type, firstX, firstY, lastX, lastY

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1("turn on 0,0 through 999,999"), 1000000)
    def testExamplePart2(self):
        self.assertEqual(part2("toggle 0,0 through 999,999"), 2000000)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 400410)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 15343601)