#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.errors import *
from src import AST

class Analyzer:
    def __init__(self, ast):
        self.ast = ast
        self.ast.annotate()

    def analyze(self):
        pass
