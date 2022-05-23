# 6430
def part1(inputStr):
    return sum([len(set(c.replace('\n', ''))) for c in inputStr.split('\n\n')])

# 3125
def part2(inputStr):
    customForms = inputStr.split('\n\n')

    tally = 0
    for c in customForms:
        people = c.count('\n') + 1
        qCount = {q : c.count(q) for q in set(c)}
        qAll = 0
        for _, v in qCount.items():
            if v == people:
                qAll += 1
        tally += qAll

    return tally

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
        self.assertEqual(part1(self.inputStrEx), 11)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 6)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 6430)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 3125)