# 5410 Too Low ??
# 3497 Too Low (For sure)
def part1(inputStr):
    pairs = parseInput(inputStr)

    inOrderIndexes = [i for i, lists in enumerate(pairs, 1) if listsInOrder(*lists)]
    notInOrderIndexes = [i for i, lists in enumerate(pairs, 1) if not listsInOrder(*lists)]

    print(notInOrderIndexes)

    return sum(inOrderIndexes)

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

def listsInOrder(leftList, rightList):
    pass
    # # Not yet finished 
    # types = type(leftList), type(rightList)
    # if types == (int, int):
    #     if leftList < rightList:
    #         return True
    #     elif leftList > rightList:
    #         return False
    # elif types == (list, int):
    #     rightList = [rightList]
    # elif types == (int, list):
    #     leftList = [leftList]

    # from itertools import zip_longest
    # for leftElm, rightElm in zip_longest(leftList, rightList):
    #     if leftElm is None:
    #         return True
    #     elif rightElm is None:
    #         return False
    
    # # This works with example and tests not real
    # from itertools import zip_longest
    # for leftElm, rightElm in zip_longest(leftList, rightList):
    #     if leftElm is None:
    #         return True
    #     elif rightElm is None:
    #         return False
    #     elif type(leftElm) == int and type(rightElm) == int:
    #         if leftElm > rightElm:
    #             return False
    #     elif type(leftElm) == list and type(rightElm) == list:
    #         return listsInOrder(leftElm, rightElm)
    #     elif type(leftElm) == list and type(rightElm) == int:
    #         if listsInOrder(leftElm, [rightElm]) == False:
    #             return False
    #     elif type(leftElm) == int and type(rightElm) == list:
    #         if listsInOrder([leftElm], rightElm) == False:
    #             return False
    #     else:
    #         raise NotImplementedError(f"\n{leftElm  = }\n{rightElm = }")
    # return True

def parseInput(inputStr):
    from ast import literal_eval
    result = []
    for pairs in inputStr.split("\n\n"):
        packetAStr, packetBStr = pairs.split("\n")
        packetA = literal_eval(packetAStr)
        packetB = literal_eval(packetBStr)
        result.append((packetA, packetB))

    return result

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # # Example tests   
    # def testExamplePart1(self):
    #     self.assertEqual(part1(self.inputStrEx), 13)
    # # def testExamplePart2(self):
    # #     self.assertEqual(part2(self.inputStrEx), 0)

    # # Real Input
    # def testRealPart1(self):
    #     self.assertEqual(part1(self.inputStrReal), 0)
    # # def testRealPart2(self):
    # #     self.assertEqual(part2(self.inputStrReal), 0)

    # Testing if lists are in order
    def testListOrderAllInts(self): # All Ints
        self.assertTrue(listsInOrder([1,1,3,1,1], [1,1,5,1,1])) # Ex Pair 1
    def testListOrderMixedTypes(self): # Mixed Types
        self.assertTrue(listsInOrder([[1],[2,3,4]], [[1],4])) # Ex Pair 2
        self.assertFalse(listsInOrder([9], [[8,7,6]])) # Ex Pair 3
    def testListOrderOneSideRunsOut(self):
        self.assertTrue(listsInOrder([[4,4],4,4], [[4,4],4,4,4])) # Ex Pair 4
        self.assertFalse(listsInOrder([7,7,7,7], [7,7,7])) # Ex Pair 5
        self.assertTrue(listsInOrder([], [3])) # Ex Pair 6
        self.assertFalse(listsInOrder([[[]]], [[]])) # Ex Pair 7
    def testListOrderListsOfInts(self):
        self.assertFalse(listsInOrder([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])) # Ex Pair 8