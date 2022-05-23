# TODO
# Refactor part 1 to have valid numbers generated at print
# Fix part 2



# 28873
def part1(inputStr):
	rules, _, nearbyTickets = parseInput(inputStr)	
	invalidValues = findInvalid(rules, nearbyTickets)

	return sum(invalidValues)

# 2587271823407
def part2(inputStr):
	rules, yourTicket, nearbyTickets = parseInput(inputStr)
	invalidValues = findInvalid(rules, nearbyTickets)
	
	for ticket in nearbyTickets:
		if [i for i in ticket if i in invalidValues]:
			nearbyTickets.remove(ticket)

	import numpy as np
	columns = np.array(nearbyTickets).T.tolist()

	rulesCol = {ruleName:[] for ruleName in rules}
	for colIndex, column in enumerate(columns):
		for ruleName, ruleVal in rules.items():
			validInRule = set()
			[validInRule.add(x) for x in range(ruleVal[0][0], ruleVal[0][1]+1)]
			[validInRule.add(x) for x in range(ruleVal[1][0], ruleVal[1][1]+1)]

			validRule = True
			for v in column:
				if v not in validInRule:
					validRule = False
			if validRule:
				rulesCol[ruleName].append(colIndex)

	while not oneColPerRule(rulesCol):
		colsToRemove = []
		for v in rulesCol.values():
			if len(v) == 1:
				colsToRemove.append(v[0])
        
		for v in rulesCol.values():
			if len(v) > 1:
				for c in colsToRemove:
					if c in v:
						v.remove(c)

	result = 1
	for k, v in rulesCol.items():
		if 'departure' in k:
			result *= yourTicket[v[0]]
	return result

def parseInput(inputStr):
    splitInput = inputStr.split('\n\n')

    rules = {}
    for r in splitInput[0].split('\n'):
        k, s = r.split(': ')
        l, r = s.split(' or ')
        ll, lu = [int(i) for i in l.split('-')]
        rl, ru = [int(i) for i in r.split('-')]
        rules[k] = ((ll, lu), (rl, ru))
    yourTicket = list(map(int, splitInput[1].split('\n')[1].split(',')))
    nearbyTickets = [list(map(int, s.split(','))) for s in splitInput[2].split('\n')[1:]]
    return rules, yourTicket, nearbyTickets

def findInvalid(rules, nearbyTickets):
    validNumbers = set()
    for l, r in rules.values():
        [validNumbers.add(i) for i in range(l[0], l[1]+1)]
        [validNumbers.add(i) for i in range(r[0], r[1]+1)]

    return [i for sub in nearbyTickets for i in sub if i not in validNumbers]

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