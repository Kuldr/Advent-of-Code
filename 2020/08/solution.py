# 1671
def part1(inputStr):
    instructions = parseInput(inputStr)

    return runInstructions(instructions)[0]

# 892
def part2(inputStr):
    instructions = parseInput(inputStr)

    for i in range(len(instructions)):
        op, v = instructions[i]
        if op == "acc":
            pass
        else:    
            newInstructions = instructions.copy()
            if op == "jmp":
                newInstructions[i] = ("nop", v)
            elif op == "nop":
                newInstructions[i] = ("jmp", v)
            ans = runInstructions(newInstructions)
            if ans[1]:
                return ans[0]

def parseInput(inputStr):
    return [(s.split(" ")[0], int(s.split(" ")[1])) for s in inputStr.split("\n")]

def runInstructions(instructions):
        accumulator = 0
        visited = set()
        currentIndex = 0

        while (currentIndex not in visited) and (0 <= currentIndex < len(instructions)):
            op, v = instructions[currentIndex]
            
            if op == "jmp":
                visited.add(currentIndex)
                currentIndex += v
            elif op == "acc":    
                accumulator += v
                visited.add(currentIndex)
                currentIndex += 1
            elif op == "nop":
                visited.add(currentIndex)
                currentIndex += 1
        
        return accumulator, currentIndex >= len(instructions)

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
        self.assertEqual(part1(self.inputStrEx), 5)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 8)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 1671)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 892)