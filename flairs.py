#!/usr/bin/python3

from sys import argv
import Scanner

# pass in arg for path to flair program
if len(argv) > 1:
    FILE_PATH = argv[1]
else:
    print("Please pass an arg for the path to a flair program.")
    exit()

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
