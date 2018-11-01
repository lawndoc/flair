#!/usr/bin/python3

class SymbolTable():
    def __init__(self):
        self.table = {}
        self.errors = False
        self.lineNum = 0
    def __iter__(self):
        if self.table:
            for f in self.table:
                yield f
        else:
            return None
    def __getitem__(self, key):
        return self.table[key]
    def __setitem__(self, key, value):
        self.table[key] = value
    def __contains__(self, key):
        return any(f == key for f in self.table)
    def __str__(self):
        rep = ""
        for function in self.table.values():
            rep += str(function)
        return rep
    def values(self):
        for f in self.table.values():
            yield f
    def newError(self):
        self.errors = True
    def hasError(self):
        return self.errors
    def setLineNum(self, num):
        self.lineNum = num
    def getLineNum(self):
        return self.lineNum
    def nextLine(self):
        self.lineNum += 1
        return str(self.lineNum - 1)
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
        self.formalError = False
        self.programFunction = False
        if functionNode.getFormals():
            for formal in functionNode.getFormals():
                # Make sure each identifier is only defined once
                if formal.getName() in self.formals:
                    self.formalError = True
                    print("Semantic error: identifier '{}' is defined more than once in function '{}'".format(formal.getName(), self.id))
                self.formals[formal.getName()] = FormalRecord(formal)
        self.callers = []
        self.codeAddress = 0
    def __str__(self):
        if self.isProgram():
            rep = " Program '" + self.id + "'\n"
        else:
            rep = " Function '" + self.id + "'\n"
        if not self.isProgram():
            rep += "> type: " + self.type + "\n"
        rep += "> formals:\n"
        for id, record in zip(self.formals, self.formals.values()):
            rep += ">\t" + id + " : " + record.getType() + "\n"
        rep += "> callers:\n"
        for caller in self.callers:
            rep += ">\t" + caller + "\n"
        return rep
    def addCaller(self, functionID):
        self.callers.append(functionID)
    def getCallers(self):
        return self.callers
    def getName(self):
        return self.id
    def getType(self):
        return self.type
    def getFormals(self):
        return self.formals
    def hasFormalError(self):
        return self.formalError
    def setAsProgram(self):
        self.programFunction = True
    def isProgram(self):
        return self.programFunction
    def setAddress(self, addr):
        self.codeAddress = addr
    def getAddress(self):
        return self.codeAddress
