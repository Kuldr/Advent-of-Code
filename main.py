# Imports
import unittest
import time
import mainHelper as mh

# Constants
YEAR = 2023
DAY = 5
SINGLE_DAY = True
TESTING = True
TEST_PREFIX = "test" #"testExample" "testReal"
PROFILING = False
# PROFILING_LINES constant in mainHelper # TODO: fix this

@mh.profileDecorator("profile.prof", PROFILING)
def main():
	# Start the timer
	globalStart = time.perf_counter()
	
	if TESTING:
		loader = unittest.TestLoader()
		loader.testMethodPrefix = TEST_PREFIX
		tests = []
	
		for day in mh.daysRange(SINGLE_DAY, DAY):
			try:
				solution = mh.getSolutionModule(YEAR, day)
				tests.append(loader.loadTestsFromTestCase(solution.tests))
			except ModuleNotFoundError:
				print(f"Tests found up to Day {day-1}")
				break
		
		unittest.TextTestRunner().run(unittest.TestSuite(tests))
	else:
		for day in mh.daysRange(SINGLE_DAY, DAY):
			try:
				mh.runSolution(YEAR, day)
			except ModuleNotFoundError:
				print(f"\nSolutions found up to Day {day-1}")
				break
				
	globalTimeTaken = round(time.perf_counter() - globalStart, 5)
	print(f"\nGlobal Time Taken = {globalTimeTaken}s")

# Main script
main()