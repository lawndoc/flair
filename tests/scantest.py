#!/usr/bin/python3

from sys import argv, path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.scanner import Scanner

# pass in arg for path to flair program
if len(argv) > 1:
    if "scantest.py" in argv[0]:
        FILE_PATH = argv[1]
    elif "scantest.py" in argv[1]:
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

# pass program into scanner and get tokens
scanner = Scanner(flairProgram)
tokens = scanner.scan()

# print tokens
while True:
    call = input("Enter 'n' for next or 'p' for peek, 'a' for all tokens, or 'x' to exit. $> ")
    if call == "n":
        print(scanner.next())
    elif call == "p":
        print(scanner.peek())
    elif call == "a":
        for t in tokens:
            print(t.getType(), (str(t.getValue()) if str(t.getValue()) not in ";.,:(){}" else ""))
    elif call == "x":
        exit()
    else:
        print("Please enter a valid character.")
