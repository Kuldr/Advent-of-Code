# 226
def part1(inputStr):
    parsedInput = parseInput(inputStr)

    queue = ["shiny gold"]
    seen = set()
    while queue:
        current = queue.pop(0)
        seen.add(current)
        for k, v in parsedInput.items():
            if current in v:
                queue.append(k)

    return len(seen)-1 # -1 as shiny gold is in seen too

# 9569
def part2(inputStr):
    return numBagsInside(parseInput(inputStr), "shiny gold")

def parseInput(inputStr):
    # Parse the input | parsedInput :: {colour: {colour: number}}
    parsedInput = {}
    for s in inputStr.split("\n"):
        s = s.replace(".", "").replace(" bags", "").replace(" bag", "")
        s = s.split(" contain ")

        r = s[1].split(", ")
        rDict = {}
        for i in r:
            if i == "no other":
                pass
            else:
                rDict[i[2:]] = int(i[0])
        parsedInput[s[0]] = rDict
    
    return parsedInput

def numBagsInside(parsedInput, bag):
        if parsedInput[bag]:
            return sum([v + numBagsInside(parsedInput, k) * v for k, v in parsedInput[bag].items()]) 
        else:
            return 0  

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
        self.assertEqual(part1(self.inputStrEx), 4)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 32)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 226)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 9569)