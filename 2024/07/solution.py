# 465126289353
def part1(inputStr):
    tests = parseInput(inputStr)

    # return sum([target for target, nums in tests if testOperators(target, nums, ["*", "+"])])
    # return sum([target for target, nums in tests if testOperatorsHeadRecursive(target, nums[1:], False, nums[0])])
    return sum([target for target, nums in tests if testOperatorsTailRecursive(target, nums, False)])

# 70597497486371
def part2(inputStr):
    tests = parseInput(inputStr)

    # return sum([target for target, nums in tests if testOperators(target, nums, ["*", "+", "||"])])
    # return sum([target for target, nums in tests if testOperatorsHeadRecursive(target, nums[1:], True, nums[0])])
    return sum([target for target, nums in tests if testOperatorsTailRecursive(target, nums, True)])

def parseInput(inputStr):
    lines = inputStr.split("\n")
    tests = []
    for line in lines:
        target, numsStr = line.split(": ")
        nums = numsStr.split(" ")
        nums = list(map(int, nums))
        tests.append((int(target), nums))

    return tests

def testOperators(target, nums, operators):
    from itertools import product

    for ops in product(operators, repeat=len(nums)-1):
        currentResult = nums[0]
        for i, op in enumerate(ops, 1):
            if op == "*":
                currentResult *= nums[i]
            elif op == "+":
                currentResult += nums[i]
            elif op == "||":
                currentResult = int( str(currentResult) + str(nums[i]) )
        if currentResult == target:
            return True
    
    return False

def testOperatorsHeadRecursive(target, numsRemaining, part2, currentResult):
    if len(numsRemaining) == 0:
        return target == currentResult
    elif currentResult > target:
        return False
    else:
        nextNum = numsRemaining[0]
        nextResults = [currentResult * nextNum, currentResult + nextNum]
        if part2:
            nextResults.append(int( str(currentResult) + str(nextNum) ))
        
        return any([testOperatorsHeadRecursive(target, numsRemaining[1:], part2, nextResult) for nextResult in nextResults])

def testOperatorsTailRecursive(target, numsRemaining, part2):
    if len(numsRemaining) == 1:
        return target == numsRemaining[0]
    else:
        nextTargets = []
        nextNum = numsRemaining[-1]
        if target % nextNum == 0: # Can only be multiply if gives whole number
            nextTargets.append(target // nextNum)
        if target - nextNum > 0: # Can only be add if above 0
            nextTargets.append(target - nextNum)
        if part2 and str(target).endswith(str(nextNum)): # Can only be concate if ends with nextNum
            try:
                nextTargets.append(int(str(target)[:-(len(str(nextNum)))]))
            except: # target can just be nextNum but not the last number remaining
                pass

        return any([testOperatorsTailRecursive(nextTarget, numsRemaining[:-1], part2) for nextTarget in nextTargets])

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
        self.assertEqual(part1(self.inputStrEx), 3749)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 11387)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 465126289353)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 70597497486371)