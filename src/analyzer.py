#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def excepthook(type, value, traceback):
    print(str(value))

sys.excepthook = excepthook

class Analyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbolTable = self.ast.analyze()
        self.checkWarnings()
        self.terminate()

    def checkWarnings(self):
        # Check for unused functions (warning) -- ignore program function
        for function in self.symbolTable.values():
            if function.getName() == self.ast.getName():
                continue
            if not function.getCallers():
                print("Warning: function {} is never called".format(function.getName()))
            # Check for unused identifiers (warning)
            for formal in function.getFormals().values():
                if not formal.isCalled():
                    print("Warning: identifier {} in function {} is never called".format(formal.getName(), function.getName()))

    def terminate(self):
        if self.symbolTable.hasError():
            exit()
        else:
            print("Program has no semantic errors.")

    def getSymbolTable(self):
        return self.symbolTable
