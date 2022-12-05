# BWNCQRMDB
def part1(inputStr):
    stackStr, movesStr = inputStr.split("\n\n")
    moves = parseMoves(movesStr) # Number | FromIndex | ToIndex

    stacks = parseStack(stackStr)

    for number, fromIndex, toIndex in moves:
        for _ in range(number):
            stacks[toIndex].append(stacks[fromIndex].pop(-1))

    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer

# NHWZCBNBF
def part2(inputStr):
    stackStr, movesStr = inputStr.split("\n\n")
    moves = parseMoves(movesStr) # Number | FromIndex | ToIndex

    stacks = parseStack(stackStr)

    for number, fromIndex, toIndex in moves:
        tempStack = stacks[fromIndex][-number:]
        stacks[fromIndex] = stacks[fromIndex][:-number]
        stacks[toIndex] += tempStack

    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer

def parseStack(stackStr):
    lines = stackStr.split("\n")
    nStacks = (len(lines[-1]) + 1) // 4
    
    stacks = [[] for _ in range(nStacks)]
    for line in reversed(lines[:-1]):
        for s in range(nStacks):
            if (char := line[1+s*4]) != " ":
                stacks[s].append(char)
    
    return stacks

def parseMoves(movesStr):
    moves = []
    for move in movesStr.split("\n"):
        move = move.split(" ")
        moveTuple = (int(move[1]), int(move[3])-1, int(move[5])-1)
        moves.append(moveTuple)

    return moves

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
        self.assertEqual(part1(self.inputStrEx), "CMZ")
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), "MCD")

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), "BWNCQRMDB")
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), "NHWZCBNBF")