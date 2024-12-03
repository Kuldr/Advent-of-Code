# 173419328
def part1(inputStr):
    import re
    regex =  re.compile(r"mul\(([\d]{1,3}),([\d]{1,3})\)")
    results = regex.findall(inputStr)

    results = [int(x)*int(y) for x, y in results]

    return sum(results)

# 90669332
def part2(inputStr):
    import re
    regex =  re.compile(r"(mul)\(([\d]{1,3}),([\d]{1,3})\)|(do)\(\)|(don\'t)\(\)")
    results = regex.findall(inputStr)

    answer = 0
    enabled = True
    for match in results:
        if match[0] and enabled: # Mul Instruction
            answer += int(match[1]) * int(match[2])
        elif match[3]: # Do Instruction
            enabled = True
        elif match[4]: # Don't Instruction
            enabled = False

    return answer


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