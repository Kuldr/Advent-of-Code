# 26796446
def part1(inputStr, preamble=25):
    import itertools

    data = list(map(int, inputStr.split('\n')))

    for i in range(preamble+1, len(data)):
        previousData = data[i-(preamble+1):i]
        combos = itertools.combinations(previousData, 2)
        comboFound = False
        for x, y in combos:
            if x + y == data[i]:
                comboFound = True
        if not comboFound:
            return data[i]

# 3353494
def part2(inputStr, preamble=25):   
    target = part1(inputStr, preamble)
    data = list(map(int, inputStr.split('\n')))

    # return {sum(x): min(x)+max(x) for x in [i for i in [data[m:n+1] for m in range(len(data)+1) for n in range(m,len(data)+1)] if len(i) >= 2]}[target] #Elegance doesn't always give speed

    for lowerIndex in range(len(data)):
        for upperIndex in range(lowerIndex, len(data)):
            temp = data[lowerIndex:upperIndex+1]
            if sum(temp) == target:
                return min(temp)+max(temp)
            elif sum(temp) > target:
                break

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
        self.assertEqual(part1(self.inputStrEx, preamble=5), 127)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx, preamble=5), 62)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 26796446)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 3353494)