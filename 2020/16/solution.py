# TODO
# Fix part 2



# 28873
def part1(inputStr):
	rules, _, nearbyTickets = parseInput(inputStr)	
	invalidValues = findInvalidNumbers(rules, nearbyTickets)

	return sum(invalidValues)

# 2587271823407
def part2(inputStr):
	# Parse input and remove invalid tickets
	rules, yourTicket, nearbyTickets = parseInput(inputStr)
	invalidValues = findInvalidNumbers(rules, nearbyTickets)
	for ticket in nearbyTickets:
		if [i for i in ticket if i in invalidValues]:
			nearbyTickets.remove(ticket)

	# List of fields
	import numpy as np
	fields = np.array(nearbyTickets).T.tolist()
	# Dictionary of fields with potential columns
	potential = {ruleName:list(range(0, len(fields))) for ruleName in rules}

	print(fields[12])
	# Remove totally invalid columns
	for ruleName, cols in potential.items():
		currentValid = rules[ruleName]
		print(currentValid)
		for col in cols:
			for num in fields[col]:
				if num not in currentValid:
					# print("Removing", col, "from", ruleName)
					potential[ruleName].remove(col)
					break
	
	# Seems to be remove some cols entirely
	# TODO: Create a print function for potential with alignment
	print(potential)
	printColumnsAligned(potential)

	# while not oneColPerRule(potential):
	# 	print(potential)
	# 	colsToRemove = []
	# 	for v in potential.values():
	# 		if len(v) == 1:
	# 			colsToRemove.append(v[0])
        
	# 	for v in potential.values():
	# 		if len(v) > 1:
	# 			for c in colsToRemove:
	# 				if c in v:
	# 					v.remove(c)

	result = 1
	for k, v in potential.items():
		if 'departure' in k:
			result *= yourTicket[v[0]]
	return result

# for debugging potential columns code
def printColumnsAligned(potenialCols, numCols=20):

	# find max length key names
	maxKeyLen = 0
	for key in potenialCols.keys():
		if len(key) > maxKeyLen: maxKeyLen = len(key)
	print(maxKeyLen)

	header = " "*maxKeyLen + " | "
	for i in range(numCols):
		header += str(i)
		header += ' '
	print(header)
	print('-'*len(header))
	# Print each row with potential columns
	for name, cols in potenialCols.items():
		print(name.rjust(maxKeyLen, ' ') + " | ", end='')
		for i in range(numCols):
			if i in cols:
				print(i, end=' ')
			else:
				if i > 9:
					print("  ", end=' ')
				else:
					print(" ", end=' ')
		print()

def parseInput(inputStr):
	splitInput = inputStr.split('\n\n')

	# Rules
	rules = {}
	for r in splitInput[0].split('\n'):
		k, s = r.split(': ')
		l, r = s.split(' or ')
		ll, lu = [int(i) for i in l.split('-')]
		rl, ru = [int(i) for i in r.split('-')]
		validNumbers = set()
		[validNumbers.add(i) for i in range(ll, lu+1)]
		[validNumbers.add(i) for i in range(rl, ru+1)]
			
		rules[k] = validNumbers

	# Tickets	
	yourTicket = list(map(int, splitInput[1].split('\n')[1].split(',')))
	nearbyTickets = [list(map(int, s.split(','))) for s in splitInput[2].split('\n')[1:]]
	return rules, yourTicket, nearbyTickets

def findInvalidNumbers(rules, nearbyTickets):
	# Add all valid numbers to a set
    validNumbers = set()
    for valid in rules.values():
        validNumbers.update(valid)

	# list of all values that appear and aren't valid
    return [value for ticket in nearbyTickets for value in ticket if value not in validNumbers]

def oneColPerRule(rulesCol):
    for v in rulesCol.values():
        if len(v) > 1:
            return False
    return True

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
		self.assertEqual(part1(self.inputStrEx), 71)
	# def testExamplePart2(self):
	# 	self.assertEqual(part1(self.inputStrEx2), 1)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 28873)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 2587271823407)