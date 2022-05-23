# 2498354
def part1(inputStr):
	digitsRow = parseRows(inputStr)

	from numpy import transpose
	digitsCol = transpose(digitsRow)

	gammaRate = ""
	epsilonRate = "" # Could use string translation for this but I'm already itterating through for gammaRate
	for col in digitsCol:
		if sum(col) > len(col)//2:
			gammaRate += '1'
			epsilonRate += '0'
		else:
			gammaRate += '0'
			epsilonRate += '1'

	return int(gammaRate, 2) * int(epsilonRate, 2)

# 3277956
def part2(inputStr):
	digitsRow = parseRows(inputStr)

	O2Rating = filterByCommonValue(digitsRow.copy(), 1)
	CO2Rating = filterByCommonValue(digitsRow.copy(), 0)

	return int(O2Rating, 2) * int(CO2Rating, 2)

def parseRows(inputStr):
	return [[int(i) for i in list(s)] for s in inputStr.split('\n')]

def filterByCommonValue(digitsRow, value):
	from numpy import transpose
	index = 0
	
	while len(digitsRow) > 1:
		currentCol = transpose(digitsRow)[index]
		if sum(currentCol) >= len(digitsRow)-sum(currentCol):
			commonValue = value
		else:
			commonValue = 1-value
		
		toRemove = []
		for num in digitsRow:
			if num[index] != commonValue:
				toRemove.append(num)
		for num in toRemove:
			digitsRow.remove(num)

		index += 1

	return ''.join(map(str, digitsRow[0]))

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
        self.assertEqual(part1(self.inputStrEx), 198)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 230)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2498354)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 3277956)