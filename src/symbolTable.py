#!/usr/bin/python3

class SymbolTable():
    def __init__(self):
        self.table = {}
        self.errors = False
    def __getitem__(self, key):
        return self.table[key]
    def __setitem__(self, key, value):
        self.table[key] = value
    def newError(self):
        self.errors = True
    def hasError(self):
        return self.errors

class FormalRecord:
    def __init__(self, formalNode):
        self.id = formalNode.getName()
        self.type = formalNode.getType()
        self.called = False
    def newCall(self):
        self.called = True
    def isCalled(self):
        return self.called
    def getName(self):
        return self.id
    def getType(self):
        return self.type

class FunctionRecord:
    def __init__(self, functionNode):
        self.id = functionNode.getName()
        self.type = functionNode.getType()
        self.formals = {}
        if functionNode.getFormals():
            for formal in functionNode.getFormals():
                ## TODO: Make sure each identifier is only defined once
                self.formals[formal.getName()] = FormalRecord(formal)
        self.callers = []
    def addCaller(self, functionID):
        self.callers.append(functionID)
    def getName(self):
        return self.id
    def getType(self):
        return self.type
    def getFormals(self):
        return self.formals
