# 102399
def part1(inputStr):
    monkeys, _ = parseMonkeys(inputStr)

    for _ in range(20):
        for monkey in monkeys:
            while monkey.hasItems():
                monkeyIndex, item = monkey.turn1()
                monkeys[monkeyIndex].append(item)

    inspections = sorted([m.inspections for m in monkeys], reverse=True)
    return inspections[0] * inspections[1]

# 23641658401
def part2(inputStr):
    monkeys, mod = parseMonkeys(inputStr)

    for _ in range(10_000):
        for monkey in monkeys:
            while monkey.hasItems():
                monkeyIndex, item = monkey.turn2(mod)
                monkeys[monkeyIndex].append(item)

    inspections = sorted([m.inspections for m in monkeys], reverse=True)
    return inspections[0] * inspections[1]

def parseMonkeys(inputStr):
    monkeys = []
    mod = 1
    for monkeyStr in inputStr.split("\n\n"):
        lines = monkeyStr.split("\n")

        items = list(map(int, lines[1].split(": ")[1].split(",")))

        op = lines[2].split(" = ")[1]

        test = int(lines[3].split(" ")[-1])
        monkeyT = int(lines[4].split(" ")[-1])
        monkeyF = int(lines[5].split(" ")[-1])

        monkeys.append(monkeyClass(items, op, test, monkeyT, monkeyF))
        mod *= test
    
    return monkeys, mod

class monkeyClass:
    def __init__(self, items, op, test, monkeyT, monkeyF):
        self.items = items
        # Very Very Very fucky do not like but works for this
        self.op = lambda old: eval(op)
        self.test = lambda item: item % test == 0
        self.monkeyT = monkeyT
        self.monkeyF = monkeyF
        self.inspections = 0

    def __str__(self):
        return str(self.items)

    def append(self, item):
        self.items.append(item)

    def turn1(self):
        item = self.items.pop(0)
        item = self.op(item)
        item //= 3
        self.inspections += 1
        if self.test(item):
            return (self.monkeyT, item)
        else:
            return (self.monkeyF, item)
    
    def turn2(self, mod):
        item = self.items.pop(0)
        item = self.op(item)
        item %= mod
        self.inspections += 1
        if self.test(item):
            return (self.monkeyT, item)
        else:
            return (self.monkeyF, item)
    
    def hasItems(self):
        return True if len(self.items) > 0 else False
    
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
        self.assertEqual(part1(self.inputStrEx), 10605)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 2713310158)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 102399)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 23641658401)