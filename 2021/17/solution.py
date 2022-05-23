# 4095
def part1(inputStr):
	return max(tryAllShots(*parseTargetArea(inputStr)))

# 3773
def part2(inputStr):
	return len(tryAllShots(*parseTargetArea(inputStr)))

def parseTargetArea(inputStr):
	#           1 
	# 0123456789012
	# target area: x=244..303, y=-91..-54
	xs, ys = inputStr[13:].split(", ")
	xs = xs[2:].split("..")
	ys = ys[2:].split("..")
	xlow, xhigh = map(int, xs)
	ylow, yhigh = map(int, ys)
	return xlow, xhigh, ylow, yhigh

def simulateProbe(probeVelX, probeVelY, xlow, xhigh, ylow, yhigh):
	probePosX = 0
	probePosY = 0
	maxY = 0
	while True:
		# Update the positions
		probePosX += probeVelX
		probePosY += probeVelY
		if probePosY > maxY:
			maxY = probePosY

		# Change velocity
		probeVelY -= 1
		if probeVelX > 0:
			probeVelX -= 1

		# Check the position is out of bounds
		if probeVelY < 0 and probePosY < ylow:
			return False, maxY	
		if probeVelX == 0 and (probePosX < xlow or probePosX > xhigh):
			return False, maxY
				
		# Check in bounds
		if probePosX >= xlow and probePosX <= xhigh and probePosY >= ylow and probePosY <= yhigh:
			return True, maxY

def tryAllShots(xlow, xhigh, ylow, yhigh):
	allShots = []
	from itertools import product
	xbounds = range(0, xhigh+1)
	ybounds = range(ylow, -ylow+1)
	for x, y in product(xbounds, ybounds):
		hit, maxY = simulateProbe(x, y, xlow, xhigh, ylow, yhigh)
		if hit: allShots.append(maxY)

	return allShots

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
        self.assertEqual(part1(self.inputStrEx), 45)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 112)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 4095)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 3773)