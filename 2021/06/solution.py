# 380243
def part1(inputStr):
	return itterateSchool(inputStr, 80)

# 1708791884591
def part2(inputStr):
	return itterateSchool(inputStr, 256)

def itterateSchool(inputStr, days):
	school = [int(i) for i in inputStr.split(',')]
	timers = [school.count(0),
				school.count(1),
				school.count(2),
				school.count(3),
				school.count(4),
				school.count(5),
				school.count(6),
				school.count(7),
				school.count(8)]

	for day in range(days):
		newTimers = [0] * 9
		for index, count in enumerate(timers):
			if index == 0:
				newTimers[6] += count
				newTimers[8] += count
			else:
				newTimers[index - 1] += count
		timers = newTimers

	return sum(timers)

def itterateSchoolNAIVE(inputStr, days):
	school = [int(i) for i in inputStr.split(',')]

	for day in range(days):
		newSchool = []
		for timer in school:
			if timer == 0:
				newSchool.append(6)
				newSchool.append(8)
			else:
				newSchool.append(timer - 1)
		school = newSchool

	return len(school)

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
        self.assertEqual(part1(self.inputStrEx), 5934)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 26984457539)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 380243)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 1708791884591)