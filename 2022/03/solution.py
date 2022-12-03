# 7793
def part1(inputStr):
    from string import ascii_letters
    priorities = {letter:index+1 for index, letter in enumerate(ascii_letters)}

    total = 0
    for backpack in inputStr.split("\n"):
        compartment1 = set(backpack[:(size := len(backpack)//2)])
        compartment2 = set(backpack[size:])
        
        duplicate = compartment1.intersection(compartment2).pop()
        total += priorities[duplicate]        


    return total

# 2499
def part2(inputStr):
    from string import ascii_letters
    priorities = {letter:index+1 for index, letter in enumerate(ascii_letters)}

    elves = inputStr.split("\n")
    groups = [elves[index: index+3] for index in range(0, len(elves), 3)]
    total = 0
    for backpacks in groups:
        b1, b2, b3 = backpacks
        b1, b2, b3 = set(b1), set(b2), set(b3)
        
        duplicate = b1.intersection(b2).intersection(b3).pop()
        total += priorities[duplicate]        

    return total

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
        self.assertEqual(part1(self.inputStrEx), 157)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 70)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 7793)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 2499)