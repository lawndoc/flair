#!/usr/bin/python3

from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.parser import Parser
from src.scanner import Scanner
from src.analyzer import Analyzer
from src.generator import Generator

# pass in arg for path to flair program
if len(argv) > 1:
    if "generatortest.py" in argv[0]:
        FILE_PATH = argv[1]
    elif "generatortest.py" in argv[1]:
        FILE_PATH = argv[2]
    else:
        error_msg = ("Unexpected call from the command line: {}")
        raise SyntaxError(error_msg.format(" ".join(argv)))
else:
    error_msg = ("Please pass an arg for the path to a flair program.")
    raise SyntaxError(error_msg)

# store program into string variable
with open(FILE_PATH, "r") as flr:
    flairProgram = flr.read()

scanner = Scanner(flairProgram)
parser = Parser(scanner)
ast = parser.parse()
analyzer = Analyzer(ast)
symbolTable = analyzer.getSymbolTable()
generator = Generator(ast, symbolTable)
code = generator.generateCode()
if "/" in FILE_PATH:
    fileName = FILE_PATH[FILE_PATH.rindex("/")+1:]
else:
    fileName = FILE_PATH
if "." in fileName:
    fileName = fileName[:fileName.rindex(".")]
fileName += ".tm"
with open(fileName, 'w+') as f:
    f.write(code)
print("TM code saved to file {}".format(fileName))
