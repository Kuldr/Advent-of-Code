# 1046015 Too Low
def part1(inputStr):
	import re
	regex = re.compile("(?:\$ cd )(.*)(?:\n\$ ls)([^$]*)")
	matches = re.findall(regex, inputStr)

	# Parse the folder structure
	directories = {}
	for dirName, lsOutput in matches:
		# Found this out through a reddit meme before checking
		# if dirName in directories:
		# 	print("ARRRRGH", dirName)
		lsStructure = {}
		for line in lsOutput.split("\n"):
			if line != "":
				size, name = line.split(" ")
				if size == "dir":
					lsStructure[dirName+"-"+name] = 0
				else:
					lsStructure[name] = int(size)

		directories[dirName] = lsStructure

	print(directories)

	# Calculate the size of each folder
	directorySizes = {}
	for dirName in directories.keys():
		directorySizes[dirName] = directorySize(dirName, directories)
		# if (size := directorySize(dirName, directories)) <= 100000:
		# 	ansTotal += size
		
	return sum([size for size in directorySizes.values() if size <= 100000])

# from functools import lru_cache
# @lru_cache(maxsize=None)
def directorySize(dirName, directories):
	totalSize = 0
	for name, size in directories[dirName].items():
		if size > 0:
			totalSize += size
		else:
			totalSize += directorySize(name, directories)

	return totalSize

# ANSWER
def part2(inputStr):
    raise NotImplementedError("Part 2")

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
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # Real Input
    # def testRealPart1(self):
    #     self.assertEqual(part1(self.inputStrReal), 0)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)