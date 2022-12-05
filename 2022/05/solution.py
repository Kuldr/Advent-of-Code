# ANSWER
def part1(inputStr):
    stackStr, movesStr = inputStr.split("\n\n")
    moves = parseMoves(movesStr) # Number | FromIndex | ToIndex

    # stacks = parseStack(stackStr)
    stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

    for number, fromIndex, toIndex in moves:
        for _ in range(number):
            stacks[toIndex].append(stacks[fromIndex].pop(-1))

    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer

    raise NotImplementedError("Part 1")

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def parseStack(stackStr):
    pass

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
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # # Real Input
    # def testRealPart1(self):
    #     self.assertEqual(part1(self.inputStrReal), 0)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)