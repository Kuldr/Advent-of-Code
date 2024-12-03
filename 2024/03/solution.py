# 173419328
def part1(inputStr):
    results = parseInput(inputStr)

    results = [x*y for _, x, y in results]

    return sum(results)

# 90669332
def part2(inputStr):
    results = parseInput(inputStr)

    answer = 0
    enabled = True
    for match in results:
        if match[0] == "mul" and enabled:
            answer += match[1] * match[2]
        elif match[0] == "do":
            enabled = True
        elif match[0] == "don't":
            enabled = False

    return answer

def parseInput(inputStr):
    import re
    regex =  re.compile(r"(mul|do|don\'t)\(([\d]{0,3}),?([\d]{0,3})\)")
    results = regex.findall(inputStr)

    results = [(op, int(x), int(y)) if op == "mul" else (op,0,0) for op, x, y in results ]

    return results


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
        self.assertEqual(part1(self.inputStrEx), 161)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx2), 48)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 173419328)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 90669332)