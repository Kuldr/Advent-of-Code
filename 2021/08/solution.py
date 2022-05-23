#239
def part1(inputStr):
	inputs = parseInput(inputStr)
	uniqueLens = [2, 3, 4, 7]
	count = 0
	for _, outputs in inputs:
		for output in outputs:
			if len(output) in uniqueLens:
				count += 1
	return count

# ANSWER
def part2(inputStr):
	inputs = parseInput(inputStr)
	return sum([decodeLine(signals, outputs) for signals, outputs in inputs])

def parseInput(inputStr):
	lines = inputStr.split('\n')
	signalsStr = [line.split(' | ')[0] for line in lines]
	signals = [s.split(' ') for s in signalsStr]
	outputsStr = [line.split(' | ')[1] for line in lines]
	outputs = [s.split(' ') for s in outputsStr]
	return zip(signals, outputs)

def decodeLine(signals, outputs):
	signalToValue = {}
	valueToSignal = {}

	# any advantage to moving this to the parse
	signals = list(map(frozenset, signals))

	# Sort out the trvival signals
	for signal in signals:
		if len(signal) == 2:
			signalToValue[signal] = 1
			valueToSignal[1] = signal
		elif len(signal) == 3:
			signalToValue[signal] = 7
			valueToSignal[7] = signal
		elif len(signal) == 4:
			signalToValue[signal] = 4
			valueToSignal[4] = signal
		elif len(signal) == 7:
			signalToValue[signal] = 8
			valueToSignal[8] = signal

	# # Remove signals already found (could delete this code ??)
	# for signal in valueToSignal.values():
	# 	signals.remove(signal)

	# find none trivial from trivial
	for signal in signals:
		if len(signal) == 5:
			if valueToSignal[1] < signal:
				signalToValue[signal] = 3
				valueToSignal[3] = signal
			elif (valueToSignal[4] - valueToSignal[1]) < signal:
				signalToValue[signal] = 5
				valueToSignal[5] = signal
			else:
				signalToValue[signal] = 2
				valueToSignal[2] = signal
		elif len(signal) == 6:
			if valueToSignal[4] < signal:
				signalToValue[signal] = 9
				valueToSignal[9] = signal
			elif (valueToSignal[4] - valueToSignal[1]) < signal:
				signalToValue[signal] = 6
				valueToSignal[6] = signal
			else:
				signalToValue[signal] = 0
				valueToSignal[0] = signal

	ans = 0
	for digitStr in outputs:
		digit = frozenset(digitStr)
		ans = (ans * 10) + signalToValue[digit]

	return ans

def tryLineDecode(signalToValue, outputs):
	pass

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
		self.assertEqual(part1(self.inputStrEx), 26)
	def testExamplePart2(self):
		self.assertEqual(part2(self.inputStrEx), 61229)

	# # Decode line test
	# def testDecodeLine1(self):
	# 	line1 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
	# 	self.assertEqual(decodeLine(line1), 5353)
	# # How do I either break this up into many tests or keep running tests after a fail
		# no 0 tests
	# def testDecodeLineExample(self):
	# 	tests = zip(self.inputStrEx.split("\n"), [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315])
	# 	for line, ans in tests:
	# 		self.assertEqual(decodeLine(line), ans)

    # Real Input
	def testRealPart1(self):
		self.assertEqual(part1(self.inputStrReal), 239)
	def testRealPart2(self):
		self.assertEqual(part2(self.inputStrReal), 946346)