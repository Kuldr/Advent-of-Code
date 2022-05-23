# 2298
def part1(inputStr):
    input = inputStr.split('\n')
    timestamp = int(input[0])
    busIDs = [int(i) for i in input[1].split(',') if i != 'x']

    import math
    results = sorted([(i, i*math.ceil(timestamp/i)-timestamp) for i in busIDs], key = lambda x: x[1])
    return results[0][0] * results[0][1]

# ANSWER
def part2(inputStr):
    busIDs = [(i,int(v)) for i, v in enumerate(inputStr.split('\n')[1].split(',')) if v != 'x']

    t = 0
    inc = busIDs[0][1]

    for goalOffset, goalID in busIDs[1:]:
        solved = False
        while not solved:
            t += inc
            if (t + goalOffset) % goalID == 0:
                solved = True
        inc *= goalID

    return t

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
        self.assertEqual(part1(self.inputStrEx), 295)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 1068781)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 2298)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 783685719679632)