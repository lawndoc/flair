#!/usr/bin/python3

class SymbolTable:
    def __init__(self, name, myType):
        pass

class FunctionTable(SymbolTable):
    def __init__(self, name, myType, formalsTable):
        self.id = name
        self.type = myType
        self.formals = formalsTable
        self.callers = []

    def addCaller(self, functionID):
        self.callers.append(functionID)
