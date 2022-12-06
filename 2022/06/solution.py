# Taken from itertools recipes
# https://docs.python.org/3/library/itertools.html#itertools-recipes
def sliding_window(iterable, n):
	import collections
	from itertools import islice
	# sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
	it = iter(iterable)
	window = collections.deque(islice(it, n), maxlen=n)
	if len(window) == n:
		yield tuple(window)
	for x in it:
		window.append(x)
		yield tuple(window)

# 1210
def part1(inputStr):
	MARKER_SIZE = 4
	for index, chunk in enumerate(sliding_window(inputStr, MARKER_SIZE)):
		if len(set(chunk)) == MARKER_SIZE:
			return index + MARKER_SIZE

# 3476
def part2(inputStr):
	MARKER_SIZE = 14
	for index, chunk in enumerate(sliding_window(inputStr, MARKER_SIZE)):
		if len(set(chunk)) == MARKER_SIZE:
			return index + MARKER_SIZE

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
		self.assertEqual(part1(self.inputStrEx), 7)
	def testExample2Part1(self):
		self.assertEqual(part1("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
	def testExample3Part1(self):
		self.assertEqual(part1("nppdvjthqldpwncqszvftbrmjlhg"), 6)
	def testExample4Part1(self):
		self.assertEqual(part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
	def testExample5Part1(self):
		self.assertEqual(part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx), 19)
	def testExample2Part2(self):
		self.assertEqual(part2("bvwbjplbgvbhsrlpgdmjqwftvncz"), 23)
	def testExample3Part2(self):
		self.assertEqual(part2("nppdvjthqldpwncqszvftbrmjlhg"), 23)
	def testExample4Part2(self):
		self.assertEqual(part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29)
	def testExample5Part2(self):
		self.assertEqual(part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 26)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 1210)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 3476)