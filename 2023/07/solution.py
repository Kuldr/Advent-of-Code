# 248105065
def part1(inputStr):
    return genericPart(inputStr, False)

# 249515436
def part2(inputStr):
    return genericPart(inputStr, True)

def genericPart(inputStr, isPart2):
    if not isPart2:
        CARD_ORDER = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))
    else:
        CARD_ORDER = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))
    hands = parseInput(inputStr)
    from functools import cmp_to_key, partial
    compareHandsPartial = partial(compareHands, isPart2 = isPart2, cardOrder = CARD_ORDER)
    hands = sorted(hands, key=cmp_to_key(compareHandsPartial))
    return sum([i*hand[1] for i, hand in enumerate(hands, start = 1)])

def parseInput(inputStr):
    import re
    hands = re.compile(r"([A|K|Q|J|T|9|8|7|6|5|4|3|2|1]{5}) (\d+)").findall(inputStr)
    hands = list(map(lambda x: (x[0], int(x[1])), hands))    
    return hands

def compareHands(hand1, hand2, cardOrder, isPart2):
    # -1 if hand1 <  hand2
    #  0 if hand1 == hand2
    #  1 if hand1 >  hand2
    hand1Str, hand2Str = hand1[0], hand2[0]

    hand1Type = getHandType(hand1Str, isPart2)
    hand2Type = getHandType(hand2Str, isPart2)
    # Check type of hand first
    if hand1Type > hand2Type:
        return 1
    elif hand1Type < hand2Type:
        return -1
    else:
        # Hands are equal type
        for c1, c2 in zip(hand1Str, hand2Str):
            if cardOrder.index(c1) > cardOrder.index(c2):
                return 1
            elif cardOrder.index(c1) < cardOrder.index(c2):
                return -1

def getHandType(handStr, isPart2):
    from collections import Counter
    handCounter = Counter(handStr)
    handCounts = handCounter.most_common()
    if isPart2:
        if (jokers := handCounter["J"]) != 0:
            handCounts.remove(("J", jokers))
    else:
        jokers = 0

    if jokers == 5 or handCounts[0][1] + jokers == 5:
        return 7 # Five of a Kind
    elif handCounts[0][1] + jokers == 4:
        return 6 # Four of a Kind
    elif handCounts[0][1] + jokers == 3 and handCounts[1][1] == 2 \
            or handCounts[0][1] == 3 and handCounts[1][1] + jokers == 2:
        return 5 # Full House
    elif handCounts[0][1] + jokers == 3:
        return 4 # Three of a Kind
    elif handCounts[0][1] + jokers == 2 and handCounts[1][1] == 2 \
            or handCounts[0][1] == 2 and handCounts[1][1] + jokers == 2:
        return 3 # Two Pairs
    elif handCounts[0][1] + jokers == 2:
        return 2 # One Pair
    else:
        return 1

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
        self.assertEqual(part1(self.inputStrEx), 6440)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 5905)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 248105065)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 249515436)