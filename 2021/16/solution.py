# ANSWER
def part1(inputStr):
	return sumVersions(parsePacket(hexToBin(inputStr)))

# ANSWER
def part2(inputStr):
    return "Part 2 Not Implemented"

def hexToBin(inputStr):
	return bin(int(inputStr, 16))[2:]

def parsePacket(binStr):
	packetVersion = int(binStr[:3], 2)
	packetTypeID = int(binStr[3:6], 2)
	remainingStr = binStr[6:]

	print(packetVersion, packetTypeID, remainingStr)

	if packetTypeID == 4:
		# Complete 
		subPackets = []
		value = readLiteralPacketValue(remainingStr)
	else: 
		lengthTypeID = int(remainingStr[0])
		if lengthTypeID == 0:
			totalLength = int(remainingStr[1:14], 2)
			packetsToDecode = remainingStr[14:14+totalLength]
			# Todo need to be able to decode the remaining sub packets
		else:
			print(" " + remainingStr[1:12])
			numPackets = int(remainingStr[1:12], 2)

	return (packetVersion, packetTypeID, subPackets, value)

def readLiteralPacketValue(remainingStr):
	valueStr = ""
	groups = [remainingStr[i:i+5] for i in range(0, len(remainingStr), 5)]
	for group in groups:
		if group[0] == "1":
			valueStr += group[1:]
		else:
			valueStr += group[1:]
			break
	return int(valueStr, 2)

def sumVersions(packet):
	# (Version, ID, [subpackets], Value)
	version, _, subPackets, _ = packet
	return version + sum([sumVersions(subPacket) for subPacket in subPackets])
		
# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		import importlib.resources
		cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
		cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests
	def testTHROWAWAY(self):
		self.assertEqual(part1("D2FE28"), 0)
	def testExample1Part1(self):
		self.assertEqual(part1(self.inputStrEx), 16)
	def testExample2Part1(self):
		self.assertEqual(part1("620080001611562C8802118E34"), 12)
	def testExample3Part1(self):
		self.assertEqual(part1("C0015000016115A2E0802F182340"), 23)
	def testExample4Part1(self):
		self.assertEqual(part1("A0016C880162017C3686B18A3D4780"), 23)
    # def testExamplePart2(self):
    #     self.assertEqual(part2(self.inputStrEx), 0)

    # # Real Input
    # def testRealPart1(self):
    #     self.assertEqual(part1(self.inputStrReal), 0)
    # def testRealPart2(self):
    #     self.assertEqual(part2(self.inputStrReal), 0)