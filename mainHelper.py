# Imports
import importlib
import importlib.resources
import time
import cProfile
import pstats

# Constants
PROFILING_LINES = 20

# Testing profiling decorator
def profileDecorator(fileName, profiling):
	def inner(func):
		def wrapper(*args, **kwargs):
			if not profiling: 
				return func()

			with cProfile.Profile() as profiler:
			    funcReturn = func()
			profiler.dump_stats("profilerStats/"+fileName) # Note use of name from outer scope
			profilerPrintStats(pstats.Stats(profiler))
				
			return funcReturn
		return wrapper
	return inner

def profilerPrintStats(profilerStats):
	# I only really want the first when profilling a day and the second when profiling a year
	# Some times I want to profile the tests

	# General Profiler
	# What is the difference between TIME and CUMULTATIVE on the next line
	profilerStats.sort_stats(pstats.SortKey.TIME).print_stats(PROFILING_LINES)
	
	# Which parts take the longest
	profilerStats.sort_stats(pstats.SortKey.CUMULATIVE).print_stats("\(part", PROFILING_LINES)


# Helper Functions
def daysRange(singleDay, day):
	if singleDay:
		return range(day, day+1)
	else:
		return range(1, 25+1)

def getInput(year, day):
    return importlib.resources.read_text(f"{year}.{str(day).zfill(2)}", "input.txt")

def getSolutionModule(year, day):
    return importlib.import_module(".solution", f"{year}.{str(day).zfill(2)}")

def runSolution(year, day):
	# Get module and input
	solution = getSolutionModule(year, day)
	inputStr = getInput(year, day)

	print(f"{year} Day {str(day).zfill(2)}")

	# Part 1
	start1 = time.perf_counter()
	print(f"  Part1: ")
	ans = solution.part1(inputStr)
	print(f"\tAns  | {ans}")
	print(f"\tTime | {round(time.perf_counter() - start1, 5)}s")

	# Part 2 
	start2 = time.perf_counter()
	print(f"  Part2: ")
	ans = solution.part2(inputStr)
	print(f"\tAns  | {ans}")
	print(f"\tTime | {round(time.perf_counter() - start2, 5)}s")