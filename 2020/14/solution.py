# 15018100062885
def part1(inputStr):
    input = parseInput(inputStr)

    mask = "X"*36
    memDict = {}
    for v in input:
        if v[0] == "mask":
            mask = v[1]
        if v[0] == "mem":
            s = ""
            for i, c in enumerate(mask):
                if c == 'X':
                    s = s + v[2][i]
                else:
                    s = s + c
            memDict[int(v[1], 2)] = int(s, 2)

    return sum(memDict.values())

# 5724245857696
def part2(inputStr):
    input = parseInput(inputStr)
    import itertools

    memDict = {}
    for v in input:
        if v[0] == "mask":
            mask = v[1]
            perms = [''.join(x) for x in itertools.product('01', repeat=v[1].count('X'))]
        if v[0] == "mem":
            s = ""
            for i, c in enumerate(mask):
                if c == '0':
                    s = s + v[1][i]
                elif c == '1':
                    s = s + '1'
                elif c == 'X':
                    s = s + 'X'
            for p in perms:
                sPrime = s[:]
                for c in p:
                    sPrime = sPrime.replace('X', c, 1)
                memDict[int(sPrime, 2)] = int(v[2], 2)

    return sum(memDict.values())

def parseInput(inputStr):
    import re 
    regexMask = re.compile("mask = ([X01]{36})")
    regexMem = re.compile("mem\[(\d*)\] = (\d*)")

    input = []
    for s in inputStr.split('\n'):
        matchMask = re.match(regexMask, s)
        matchMem  = re.match(regexMem, s)
        if matchMask:
            input.append(("mask", matchMask.group(1)))
        if matchMem:
            addr = str(bin(int(matchMem.group(1))))[2:].zfill(36)
            value = str(bin(int(matchMem.group(2))))[2:].zfill(36)
            input.append(("mem", addr, 
                        value
                        ))
    return input


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
        self.assertEqual(part1(self.inputStrEx), 165)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx2), 208)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 15018100062885)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 5724245857696)