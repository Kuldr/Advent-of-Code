# 335330
def part1(inputStr):
	return findMinFuel(inputStr, fuelToAlignToConst)

# 92439766
def part2(inputStr):
	return findMinFuel(inputStr, fuelToAlignToSum)

# Could make use of numpy??
# Could make use of memoization??
# Multiple repeat positions - could exploit this?
def findMinFuel(inputStr, fuelCalc):
	positions = list(map(int, inputStr.split(',')))
	return min([fuelCalc(final, positions) for final in range(min(positions), max(positions)+1)])

def fuelToAlignToConst(final, positions):
	return sum([abs(pos-final) for pos in positions])

def fuelToAlignToSum(final, positions):
	return sum([sum1toN(abs(pos-final)) for pos in positions])

def sum1toN(n):
	return n*(n+1)//2


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
        self.assertEqual(part2(self.inputStrEx), 168)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 335330)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 92439766)