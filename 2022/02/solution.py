# 12586
def part1(inputStr):
    scoresShapes = {"X":1, "Y":2, "Z":3}
    scoresOutcomes = {-1:0, 0:3, 1:6}
    score = 0

    foeIndexes = {"A":0, "B":1, "C":2}
    youIndexes = {"X":0, "Y":1, "Z":2}
    rps = ["R", "P", "S"]

    for round in inputStr.split("\n"):
        foe, you = round.split(" ")
        foeIndex = foeIndexes[foe]
        youIndex = youIndexes[you]
        # Outcomes
        if rps[youIndex] == rps[foeIndex]:
            outcome = 0
        elif rps[youIndex-1] == rps[foeIndex]:
            outcome = 1
        else: # Could use youIndex + 1 % 3
            outcome = -1
        
        score += scoresShapes[you] + scoresOutcomes[outcome]

    return score

# 13193
def part2(inputStr):
    objectives = {"X":-1, "Y":0, "Z":1}

    scoresOutcomes = {-1:0, 0:3, 1:6}
    score = 0

    foeIndexes = {"A":0, "B":1, "C":2}
    rps = ["R", "P", "S"]
    scoresShapes = {"R":1, "P":2, "S":3}

    for round in inputStr.split("\n"):
        foe, objective = round.split(" ")
        foeIndex = foeIndexes[foe]
        objective = objectives[objective]

        foeShape = foeIndexes[foe]
        youShape = rps[(foeIndex+objective)%3]
        
        score += scoresShapes[youShape] + scoresOutcomes[objective]

    return score

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
        self.assertEqual(part1(self.inputStrEx), 15)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 12)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 12586)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 13193)