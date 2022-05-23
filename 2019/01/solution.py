# ANSWER
def part1(inputStr):
	return sum([m//3-2 for m in map(int, inputStr.split('\n'))])

# ANSWER
def part2(inputStr):
	calcFuelRec = lambda m: (f := m//3-2, f + calcFuelRec(f) if f > 0 else 0)[1] 

	return sum([calcFuelRec(m) for m in map(int, inputStr.split('\n'))])

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
        self.assertEqual(part1(self.inputStrEx), 33585)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 50348)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 3331849)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 4994898)