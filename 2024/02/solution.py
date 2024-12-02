# 510
def part1(inputStr):
    reports = parseInput(inputStr)

    valid = 0
    for report in reports:
        asc = 1 if report[1] - report[0] > 0 else -1
        
        validReport = True
        for levelCurr, levelNext in zip(report, report[1:]):
            if not ((diff := (levelNext - levelCurr)*asc) >= 1 and diff <= 3):
                validReport = False
                break
        if validReport:
            valid += 1

    return valid

# 553
def part2(inputStr):
    reports = parseInput(inputStr)

    valid = 0
    for reportPreVar in reports:
        reportVars = generateReportVariations(reportPreVar)
        for report in reportVars:
            asc = 1 if report[1] - report[0] > 0 else -1
            
            validReport = True
            for levelCurr, levelNext in zip(report, report[1:]):
                if not ((diff := (levelNext - levelCurr)*asc) >= 1 and diff <= 3):
                    validReport = False
                    break
            if validReport:
                valid += 1
                break

    return valid

def parseInput(inputStr):
    reports = inputStr.split("\n")
    reports = [list(map(int, report.split(" "))) for report in reports]
    return reports

def generateReportVariations(report):
    reportVars = [report]
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]
        reportVars.append(temp)

    return reportVars

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
        self.assertEqual(part1(self.inputStrEx), 2)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 4)

    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 510)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 553)