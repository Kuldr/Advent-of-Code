# 945
def part1(inputStr):		
	potentialPasswords = [ [a,b,c,d,e,f] for a in range(10) for b in range(10) for c in range(10) for d in range(10) for e in range(10) for f in range(10) 
							if a <= b and b <= c and c <= d and d <= e and e <= f ]
	
	day4Input = list(map(int, inputStr.split('-')))
	
	counter = 0
	for p in potentialPasswords:
	    if validPassword(p, day4Input[0], day4Input[1]):
	        counter += 1
	
	return counter

# 617
def part2(inputStr):
	potentialPasswords = [ [a,b,c,d,e,f] for a in range(10) for b in range(10) for c in range(10) for d in range(10) for e in range(10) for f in range(10) 
							if a <= b and b <= c and c <= d and d <= e and e <= f ]

	day4Input = list(map(int, inputStr.split('-')))
	
	counter = 0
	for p in potentialPasswords:
	    if validPassword2(p, day4Input[0], day4Input[1]):
	        counter += 1
	
	return counter

def validPassword(password, rangeMin, rangeMax):
	# The value is within the range given in your puzzle input.
	passwordInt = int("".join(map(str, password))) 
	if not (passwordInt >= rangeMin and passwordInt < rangeMax):
		return False

	# Two adjacent digits are the same.
	lastc = password[0]
	double = False
	for c in password[1:]:
		if lastc == c:
			double = True
		lastc = c 
	if double == False:
		return False

	# Going from left to right, the digits never decrease 
	lastc = password[0]
	for c in password[1:]:
		if lastc > c:
			return False
		lastc = c 
	
	# Passed all tests
	return True

def validPassword2(password, rangeMin, rangeMax):
    # The value is within the range given in your puzzle input.
	passwordInt = int("".join(map(str, password))) 
	if not (passwordInt >= rangeMin and passwordInt < rangeMax):
		return False

    # Two adjacent digits are the same.
    #   But are not part of a larger group of matching digits.
	from itertools import groupby
	groups = [list(v) for k,v in groupby(password)]
	double = False
	for g in groups:
		if len(g) == 2:
			double = True
	if double == False:
		return False

    # Going from left to right, the digits never decrease.
	lastc = password[0]
	for c in password[1:]:
		if lastc > c:
			return False
		lastc = c 

    # Passed all tests
	return True


# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests
	def testExample1validPassword(self):
		self.assertEqual(validPassword("111111", 000000, 999999), True)
	def testExample2validPassword(self):
		self.assertEqual(validPassword("223450", 000000, 999999), False)
	def testExample3validPassword(self):
		self.assertEqual(validPassword("123789", 000000, 999999), False)
	def testExample1validPassword2(self):
		self.assertEqual(validPassword2("112233", 000000, 999999), True)
	def testExample2validPassword2(self):
		self.assertEqual(validPassword2("123444", 000000, 999999), False)
	def testExample3validPassword2(self):
		self.assertEqual(validPassword2("111122", 000000, 999999), True)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 945)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 617)