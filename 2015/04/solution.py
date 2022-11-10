# 282749
def part1(inputStr):
	return mineAdventCoin(inputStr, 5)

def mineAdventCoin(inputStr, goal):
	from hashlib import md5
	from itertools import count

	for num in count(1):
		hash = md5(f"{inputStr}{num}".encode('utf-8')).hexdigest()
		if hash[:goal] == "0"*goal:
			return num
			
# 9962624
def part2(inputStr):
    return mineAdventCoin(inputStr, 6)

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        # cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        # cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1("abcdef"), 609043)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1("yzbqklnj"), 282749)
    def testRealPart2(self):
        self.assertEqual(part2("yzbqklnj"), 9962624)