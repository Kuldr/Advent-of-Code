def parseIntCode(inputStr):
	return {index: int(val) for index, val in enumerate(inputStr.split(","))}

def intCodeParamMode(mode, value, memory):
	if mode == '0':
		return memory[value]
	elif mode == '1':
		return value

def intCodeCycle(pc, memory, inputs, outputs):
	halt = False
	
	MAX_INSTRUCTION_LENGTH = 5
	instruction = str(memory[pc]).rjust(MAX_INSTRUCTION_LENGTH, '0')
	op = int(instruction[-2:])

	if op == 1: # Add
		paramA = intCodeParamMode(instruction[-3], pc+1, memory)
		paramB = intCodeParamMode(instruction[-4], pc+2, memory)
		store = intCodeParamMode(instruction[-5], pc+3, memory)
		memory[store] = memory[paramA] + memory[paramB]
		pc += 4
	elif op == 2: # Multiply
		paramA = intCodeParamMode(instruction[-3], pc+1, memory)
		paramB = intCodeParamMode(instruction[-4], pc+2, memory)
		store = intCodeParamMode(instruction[-5], pc+3, memory)
		memory[store] = memory[paramA] * memory[paramB]
		pc += 4
	elif op == 3: # Input
		store = intCodeParamMode(instruction[-3], pc+1, memory)
		memory[store] = inputs.pop(0)
		pc += 2
	elif op == 4: # Output
		store = intCodeParamMode(instruction[-3], pc+1, memory)
		outputs.append(memory[store])
		pc += 2
	elif op == 5: # Jump if True (Non-Zero)
		paramA = intCodeParamMode(instruction[-3], pc+1, memory)
		paramB = intCodeParamMode(instruction[-4], pc+2, memory)
		if memory[paramA] != 0:
			pc = memory[paramB]
		else:
			pc += 3
	elif op == 6: # Jump if False (Zero)
		paramA = intCodeParamMode(instruction[-3], pc+1, memory)
		paramB = intCodeParamMode(instruction[-4], pc+2, memory)
		if memory[paramA] == 0:
			pc = memory[paramB]
		else:
			pc += 3
	elif op == 7: # Less Than
		paramA = intCodeParamMode(instruction[-3], pc+1, memory)
		paramB = intCodeParamMode(instruction[-4], pc+2, memory)
		store = intCodeParamMode(instruction[-5], pc+3, memory)

		if memory[paramA] < memory[paramB]:
			memory[store] = 1
		else:
			memory[store] = 0
		pc += 4
	elif op == 8: # Equals
		paramA = intCodeParamMode(instruction[-3], pc+1, memory)
		paramB = intCodeParamMode(instruction[-4], pc+2, memory)
		store = intCodeParamMode(instruction[-5], pc+3, memory)
		
		if memory[paramA] == memory[paramB]:
			memory[store] = 1
		else:
			memory[store] = 0
		pc += 4
	elif op == 99:
		halt = True
		pc += 1
	else:
		raise NotImplementedError(f"Operand {op} Unkown")
		
	return (halt, pc, memory, outputs)
		
def intCodeRun(memory, inputs = [0]):
	pc = 0
	halt = False
	outputs = []
	
	while not halt:
		(halt, pc, memory, outputs) = intCodeCycle(pc, memory, inputs, outputs)
	
	return memory, outputs

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
	# clear; python -m unittest 2019/intcode.py 
	
    # Day 02 Tests
	def testDay02ExMain(self):
		memory = parseIntCode("1,9,10,3,2,3,11,0,99,30,40,50")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(memory[0], 3500)
		self.assertEqual(list(memory.values()),
						 [3500,9,10,70,2,3,11,0,99,30,40,50])

	def testDay02Ex1(self):
		memory = parseIntCode("1,0,0,0,99")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(list(memory.values()), [2,0,0,0,99])

	def testDay02Ex2(self):
		memory = parseIntCode("2,3,0,3,99")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(list(memory.values()), [2,3,0,6,99])

	def testDay02Ex3(self):
		memory = parseIntCode("2,4,4,5,99,0")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(list(memory.values()), [2,4,4,5,99,9801])

	def testDay02Ex4(self):
		memory = parseIntCode("1,1,1,4,99,5,6,0,99")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(list(memory.values()), [30,1,1,4,2,5,6,0,99])

 	# Day 05 Part 01 Tests 
	def testDay05ExMulParamModes(self):
		memory = parseIntCode("1002,4,3,4,33")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(memory[4], 99)

	def testDay05ExNegativeNumbers(self):
		memory = parseIntCode("1101,100,-1,4,0")
		memory, outputs = intCodeRun(memory)
		self.assertEqual(memory[4], 99)

	def testDay05ExIO(self):
		memory = parseIntCode("3,0,4,0,99")
		memory, outputs = intCodeRun(memory, inputs = [42])
		self.assertEqual(outputs[-1], 42)

	# Day 05 Part 02 Tests 
	def testDay05ExPositionEq8True(self):
		memory = parseIntCode("3,9,8,9,10,9,4,9,99,-1,8")
		memory, outputs = intCodeRun(memory, inputs = [8])
		self.assertEqual(outputs[-1], 1)

	def testDay05ExPositionEq8False(self):
		memory = parseIntCode("3,9,8,9,10,9,4,9,99,-1,8")
		memory, outputs = intCodeRun(memory, inputs = [42])
		self.assertEqual(outputs[-1], 0)

	def testDay05ExPositionLT8True(self):
		memory = parseIntCode("3,9,7,9,10,9,4,9,99,-1,8")
		memory, outputs = intCodeRun(memory, inputs = [7])
		self.assertEqual(outputs[-1], 1)

	def testDay05ExPositionLT8FalseEq(self):
		memory = parseIntCode("3,9,7,9,10,9,4,9,99,-1,8")
		memory, outputs = intCodeRun(memory, inputs = [8])
		self.assertEqual(outputs[-1], 0)
		
	def testDay05ExPositionLT8False(self):
		memory = parseIntCode("3,9,7,9,10,9,4,9,99,-1,8")
		memory, outputs = intCodeRun(memory, inputs = [42])
		self.assertEqual(outputs[-1], 0)

	def testDay05ExImmediateEq8True(self):
		memory = parseIntCode("3,3,1108,-1,8,3,4,3,99")
		memory, outputs = intCodeRun(memory, inputs = [8])
		self.assertEqual(outputs[-1], 1)

	def testDay05ExImmediateEq8False(self):
		memory = parseIntCode("3,3,1108,-1,8,3,4,3,99")
		memory, outputs = intCodeRun(memory, inputs = [42])
		self.assertEqual(outputs[-1], 0)

	def testDay05ExImmediateLT8True(self):
		memory = parseIntCode("3,3,1107,-1,8,3,4,3,99")
		memory, outputs = intCodeRun(memory, inputs = [7])
		self.assertEqual(outputs[-1], 1)

	def testDay05ExImmediateLT8FalseEq(self):
		memory = parseIntCode("3,3,1107,-1,8,3,4,3,99")
		memory, outputs = intCodeRun(memory, inputs = [8])
		self.assertEqual(outputs[-1], 0)
		
	def testDay05ExImmediateLT8False(self):
		memory = parseIntCode("3,3,1107,-1,8,3,4,3,99")
		memory, outputs = intCodeRun(memory, inputs = [42])
		self.assertEqual(outputs[-1], 0)

	def testDay05ExPositionJmp0(self):
		memory = parseIntCode("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
		memory, outputs = intCodeRun(memory, inputs = [0])
		self.assertEqual(outputs[-1], 0)

	def testDay05ExPositionJmp1(self):
		memory = parseIntCode("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
		memory, outputs = intCodeRun(memory, inputs = [1])
		self.assertEqual(outputs[-1], 1)

	def testDay05ExImmediateJmp0(self):
		memory = parseIntCode("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
		memory, outputs = intCodeRun(memory, inputs = [0])
		self.assertEqual(outputs[-1], 0)

	def testDay05ExImmediateJmp1(self):
		memory = parseIntCode("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
		memory, outputs = intCodeRun(memory, inputs = [1])
		self.assertEqual(outputs[-1], 1)

	def testDay05ExLargeLT8(self):
		memory = parseIntCode(	"3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
		memory, outputs = intCodeRun(memory, inputs = [1])
		self.assertEqual(outputs[-1], 999)

	def testDay05ExLargeEQ8(self):
		memory = parseIntCode(	"3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
		memory, outputs = intCodeRun(memory, inputs = [8])
		self.assertEqual(outputs[-1], 1000)

	def testDay05ExLargeGT8(self):
		memory = parseIntCode(	"3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
		memory, outputs = intCodeRun(memory, inputs = [9])
		self.assertEqual(outputs[-1], 1001)