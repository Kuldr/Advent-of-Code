# 5452
def part1(inputStr):
    rules, manuals = parseInput(inputStr)

    correctManauls = [manual[len(manual)//2] for manual in manuals if checkManual(manual, rules)]

    return sum(correctManauls)

# 4598
def part2(inputStr):
    rules, manuals = parseInput(inputStr)

    incorrectManauls = [manual for manual in manuals if not checkManual(manual, rules)]

    fixedManuals = [correctManual(manual, rules) for manual in incorrectManauls]

    return sum([manual[len(manual)//2] for manual in fixedManuals])


def parseInput(inputStr):
    rulesStr, manuals = inputStr.split("\n\n")

    from collections import defaultdict
    rules = defaultdict(lambda : [])

    import re
    regex = re.compile(r"(\d{2})\|(\d{2})")
    rulesPairs = [(int(lStr), int(rStr)) for lStr, rStr in regex.findall(rulesStr)]
    for left, right in rulesPairs:
        rules[left].append(right)

    manuals = manuals.split("\n")
    manuals = [ [int(val) for val in manual.split(",")] for manual in manuals ]

    return rules, manuals

def checkManual(manual, rules) -> bool:
    for i, curr in enumerate(manual):
        for comp in manual[i+1:]:
            if comp not in rules[curr]:
                return False
    return True

def correctManual(manual, rules):
    while not checkManual(manual, rules):
        exit = False
        for i, curr in enumerate(manual):
            for j, comp in enumerate(manual[i+1:]):
                if comp not in rules[curr]:
                    exit = True
                    temp = manual[i]
                    manual[i] = manual[i+j+1]
                    manual[i+j+1] = temp
                    break
            if exit:
                break

    return manual       


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
        self.assertEqual(part1(self.inputStrEx), 143)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 123)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 5452)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 4598)