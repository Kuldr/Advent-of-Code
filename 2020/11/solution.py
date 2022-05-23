# 2386
def part1(inputStr):
	result = (parseSeats(inputStr), True)
	
	while (result := itterateSeats(result[0]))[1] == True: continue

	return list(result[0].values()).count('#')

# 2091
def part2(inputStr):
	result = (parseSeats(inputStr), True)
	
	while (result := itterateSeats2(result[0]))[1] == True: continue
		
	return list(result[0].values()).count('#')

def parseSeats(inputStr):
	from itertools import product
	global comboList
	comboList = list(product([-1, 0, 1], [-1, 0, 1]))
	comboList.remove((0, 0))

	currentSeats = {}
	for rowNum, row in enumerate(inputStr.split('\n')):
		for colNum, char in enumerate(row):
			currentSeats[(rowNum, colNum)] = char
	return currentSeats

def itterateSeats(current):
	nextSeats = {}
	changed = False
	for y, x in current:
		testSeat = current[(y, x)]
		if testSeat == 'L' and not lazyNeighboursCheck(current, x, y, lambda x: x >= 1, occupiedNeighbour):
			nextSeats[(y, x)] = '#'
			changed = True
		elif testSeat == '#' and lazyNeighboursCheck(current, x, y, lambda x: x >= 4, occupiedNeighbour):
			nextSeats[(y, x)] = 'L'
			changed = True
		else:
			nextSeats[(y, x)] = testSeat

	return nextSeats, changed
			
def lazyNeighboursCheck(current, x, y, target, occupiedFunc):
	neighbours = 0
	for dx, dy in comboList:
		if occupiedFunc(current, x, y, dx, dy) == True:
			neighbours += 1
			if target(neighbours):
				return True
	return False		

def occupiedNeighbour(current, x, y, dx, dy):
    try:
        return current[(y+dy, x+dx)] == '#'
    except KeyError:
        return False

def occupiedInDirection(current, x, y, dx, dy):
	try:
		count = 0
		while True:
			count += 1
			seatTest = current[(y+(count*dy), x+(count*dx))]
			
			if seatTest == '#':
				return True
			elif seatTest == 'L':
				return False
	except KeyError:
		return False

def itterateSeats2(current):
	nextSeats = {}
	changed = False
	for y, x in current:
		testSeat = current[(y, x)]
		if testSeat == 'L' and not lazyNeighboursCheck(current, x, y, lambda x: x >= 1, occupiedInDirection):
			nextSeats[(y, x)] = '#'
			changed = True
		elif testSeat == '#' and lazyNeighboursCheck(current, x, y, lambda x: x >= 5, occupiedInDirection):
			nextSeats[(y, x)] = 'L'
			changed = True
		else:
			nextSeats[(y, x)] = testSeat

	return nextSeats, changed
    
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
		self.assertEqual(part1(self.inputStrEx), 37)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx), 26)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 2386)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 2091)