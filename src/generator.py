#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# def excepthook(type, value, traceback):
#     print(str(value))
#
# sys.excepthook = excepthook

class Generator:
    def __init__(ast, symbolTable)
