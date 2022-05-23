# 270768
def part1(inputStr):
	global numOrbits, directOrbits
	day6Input = inputStr.split('\n')

	# key is orbited by value
	directOrbits = {}
	for s in day6Input:
		k, v = s.split(')') 
		if k in directOrbits:
			directOrbits[k].append(v)
		else:
			directOrbits[k] = [v]

	numOrbits = {}
	key = "COM"
	numOrbits[key] = 0

	countOrbits(key)

	return sum(numOrbits.values())

# 451
def part2(inputStr):
	global numOrbits, directOrbits
	day6Input = inputStr.split('\n')

	# key orbits value
	directOrbits = {}
	for s in day6Input:
		v, k = s.split(')') 
		if k in directOrbits:
			directOrbits[k].append(v)
		else:
			directOrbits[k] = [v]

	distSAN = {}
	distYOU = {}

	distCalc("SAN", -1, distSAN)
	distCalc("YOU", -1, distYOU)

	distCombined = {}
	for key in set(distSAN).intersection(set(distYOU)):
		distCombined[key] = distSAN[key] + distYOU[key]
		

	return sorted(distCombined.values())[0]

def countOrbits(key):
	global numOrbits, directOrbits
	if key in directOrbits:
		for x in directOrbits.pop(key):
			numOrbits[x] = numOrbits[key] + 1
			countOrbits(x)

def distCalc(currentNode, currentDist, distDict):
	global numOrbits, directOrbits
	if currentNode in directOrbits:
		for x in directOrbits[currentNode]:
			distDict[x] = currentDist + 1
			distCalc(x, currentDist + 1, distDict)

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
		cls.inputStrEx2 = importlib.resources.read_text(__package__, "inputEx2.txt")
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests
	def testExamplePart1(self):
		self.assertEqual(part1(self.inputStrEx), 42)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx2), 4)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 270768)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 451)