#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.errors import *
from src import AST

class Analyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbolTable = self.ast.annotate()
        ## TODO: Check for unused functions (warning)
        ## TODO: Check for unused identifiers (warning)
        self.analyze()

    def analyze(self):
        if self.symbolTable.hasError():
            exit()
        else:
            print("Program has no semantic errors.")
