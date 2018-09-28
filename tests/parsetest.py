#!/usr/bin/python3

from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.parser import Parser
from src.scanner import Scanner

# pass in arg for path to flair program
if len(argv) > 1:
    if "parsetest.py" in argv[0]:
        FILE_PATH = argv[1]
    elif "parsetest.py" in argv[1]:
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

result = parser.parse()
if result:
    print("Valid Program.")
