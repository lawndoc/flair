#!/usr/bin/python3

from sys import argv
import Scanner

# pass in arg for path to flair program
if len(argv) > 1:
    if argv[0] == 'flairs':
        FILE_PATH = argv[1]
    elif argv[1] == "flairs":
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
for t in tokens:
    print(t, end=", ")
    print()
