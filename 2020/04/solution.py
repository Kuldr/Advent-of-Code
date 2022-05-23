# 260
def part1(inputStr):
    parsedPassports = parsePassports(inputStr)

    validTally = 0
    for p in parsedPassports:
        if p.keys() >= {'byr', 'iyr', 'hgt', 'ecl', 'pid', 'hcl', 'eyr'}:
            validTally += 1

    return validTally

# 153
def part2(inputStr):
    parsedPassports = parsePassports(inputStr)

    import re
    hclr = re.compile("#[0-9a-f]{6}")
    pidr = re.compile("[0-9]{9}")

    validTally = 0
    for p in parsedPassports:
        if p.keys() >= {'byr', 'iyr', 'hgt', 'ecl', 'pid', 'hcl', 'eyr'}:
            byrTest = int(p["byr"]) >= 1920 and int(p["byr"]) <= 2002
            iyrTest = int(p["iyr"]) >= 2010 and int(p["iyr"]) <= 2020
            eyrTest = int(p["eyr"]) >= 2020 and int(p["eyr"]) <= 2030
            pidTest = pidr.fullmatch(p["pid"])
            eclTest = p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            hclTest = hclr.fullmatch(p["hcl"])

            hgtTest = False
            if "cm" in p["hgt"]:
                hgtTest = int(p["hgt"][:-2]) >= 150 and int(p["hgt"][:-2]) <= 193 
            elif "in" in p["hgt"]:
                hgtTest = int(p["hgt"][:-2]) >= 59 and int(p["hgt"][:-2]) <= 76
            
            if byrTest and iyrTest and eyrTest and pidTest and hgtTest and eclTest and hclTest:
                validTally += 1

    return validTally

def parsePassports(inputStr):
    return [{d.split(":")[0]:d.split(":")[1]
            for d in p.replace("\n", " ").split(" ")}
            for p in inputStr.split("\n\n")]

# Tests ------------------------------------------
import unittest
class tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.resources
        cls.inputStrEx = importlib.resources.read_text(__package__, "inputEx.txt")
        cls.inputStrExP2Valid = importlib.resources.read_text(__package__, "inputExP2Valid.txt")
        cls.inputStrExP2Invalid = importlib.resources.read_text(__package__, "inputExP2Invalid.txt")
        cls.inputStrReal = importlib.resources.read_text(__package__, "input.txt")
    
    # Example tests   
    def testExamplePart1(self):
        self.assertEqual(part1(self.inputStrEx), 2)
    def testExamplePart2(self):
        self.assertEqual(part2(self.inputStrEx), 2)

    # Example tests: Part 2
    def testExamplePart2Valid(self):
        self.assertEqual(part2(self.inputStrExP2Valid), 4)
    def testExamplePart2Invalid(self):
        self.assertEqual(part2(self.inputStrExP2Invalid), 0)


    # Real Input
    def testRealPart1(self):
        self.assertEqual(part1(self.inputStrReal), 260)
    def testRealPart2(self):
        self.assertEqual(part2(self.inputStrReal), 153)