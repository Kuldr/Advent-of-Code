# 1644735
def part1(inputStr):
	import re
	regex = re.compile("(?:\$ cd )(.*)(?:\n\$ ls)([^$]*)|(\$ cd ..)")
	matches = re.findall(regex, inputStr)

	# Parse the folder structure
	directoryPath = []
	directories = {}
	for dirName, lsOutput, cdDotDot in matches:
		if dirName != "":
			directoryPath.append(dirName)
			lsStructure = {}
			for line in lsOutput.split("\n"):
				if line != "":
					size, name = line.split(" ")
					if size == "dir":
						lsStructure["-".join(directoryPath)+"-"+name] = 0
					else:
						lsStructure["-".join(directoryPath)+"-"+name] = int(size)
	
			directories["-".join(directoryPath)] = lsStructure
		else:
			directoryPath.pop(-1)

	# Calculate the size of each folder
	directorySizes = {}
	for dirName in directories.keys():
		directorySizes[dirName] = directorySize(dirName, directories)
		
	return sum([size for size in directorySizes.values() if size <= 100000])

def directorySize(dirName, directories):
	totalSize = 0
	for name, size in directories[dirName].items():
		if size > 0:
			totalSize += size
		else:
			totalSize += directorySize(name, directories)

	return totalSize

# 1300850
def part2(inputStr):
	import re
	regex = re.compile("(?:\$ cd )(.*)(?:\n\$ ls)([^$]*)|(\$ cd ..)")
	matches = re.findall(regex, inputStr)

	# Parse the folder structure
	directoryPath = []
	directories = {}
	for dirName, lsOutput, cdDotDot in matches:
		if dirName != "":
			directoryPath.append(dirName)
			lsStructure = {}
			for line in lsOutput.split("\n"):
				if line != "":
					size, name = line.split(" ")
					if size == "dir":
						lsStructure["-".join(directoryPath)+"-"+name] = 0
					else:
						lsStructure["-".join(directoryPath)+"-"+name] = int(size)
	
			directories["-".join(directoryPath)] = lsStructure
		else:
			directoryPath.pop(-1)

	# Calculate the size of each folder
	directorySizes = {}
	for dirName in directories.keys():
		directorySizes[dirName] = directorySize(dirName, directories)

	MAX_SPACE  = 70_000_000
	NEED_SPACE = 30_000_000
	minNeeded = NEED_SPACE - (MAX_SPACE - directorySizes["/"])

	return sorted([size for size in directorySizes.values() if size >= minNeeded])[0]

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
	def testExample1Part1(self):
		self.assertEqual(part1(self.inputStrEx), 95437)
	def testExample2Part1(self):
		self.assertEqual(part1(self.inputStrEx2), 95437)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx), 24933642)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 1644735)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 1300850)