#!/usr/bin/python3

from sys import argv

# pass in arg for path to flair program
if len(argv) > 1:
    if "cleanup.py" in argv[0]:
        FILE_PATH = argv[1]
    elif "cleanup.py" in argv[1]:
        FILE_PATH = argv[2]
    else:
        error_msg = ("Unexpected call from the command line: {}")
        raise SyntaxError(error_msg.format(" ".join(argv)))
else:
    error_msg = ("Please pass an arg for the path to the output file")
    raise SyntaxError(error_msg)

new = "\nTM Debugging Output:\n"
foundHalt = False
with open(FILE_PATH, "r") as f:
    for line in f:
        if "Halted" in line:
            foundHalt = True
            break
        elif "Enter command: " in line and "Tracing" not in line:
            if any(x in line for x in ["IN","OUT","ADD","SUB","MUL","DIV","HALT","LD","ST","J"]):
                new += "________________________________________\n\n" + line[15:]
            else:
                new += "Registers:\n" + line[15:]
        elif "OK" not in line and "TM" not in line and "Tracing" not in line:
            new += line
if not foundHalt:
    new += "!!!\n!!! Incomplete output. Please increase simulation size.\n!!!\n"
with open(FILE_PATH, "w") as f:
    f.write(new)
