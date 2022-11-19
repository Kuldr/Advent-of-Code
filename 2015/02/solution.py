# 1598415
def part1(inputStr):
	area = 0
	for dimensions in inputStr.split("\n"):
		area += dimensionsToArea(dimensions)

	return area


def dimensionsToArea(dimensions):
	l, w, h = sorted(map(int, dimensions.split("x")))
	area = 3 * l * w + 2 * w * h + 2 * h * l

	return area


# 3812909
def part2(inputStr):
	length = 0
	for dimensions in inputStr.split("\n"):
		length += dimensionsToBow(dimensions)

	return length


def dimensionsToBow(dimensions):
	l, w, h = sorted(map(int, dimensions.split("x")))
	length = 2 * l + 2 * w + l * w * h

	return length


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
		self.assertEqual(dimensionsToArea("2x3x4"), 58)

	def testExamplePart2(self):
		self.assertEqual(dimensionsToBow("2x3x4"), 34)

	# Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 1598415)

	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 3812909)
