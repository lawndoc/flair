#!/usr/bin/python3

class SymbolTable():
    def __init__(self):
        self.table = {}
        self.errors = False
    def __iter__(self):
        for f in self.table:
            yield f
        raise StopIteration
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
        raise StopIteration
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
        self.formalError = False
        if functionNode.getFormals():
            for formal in functionNode.getFormals():
                # Make sure each identifier is only defined once
                if formal.getName() in self.formals:
                    self.formalError = True
                    print("Semantic error: identifier '{}' is defined more than once in function '{}'".format(formal.getName(), self.id))
                self.formals[formal.getName()] = FormalRecord(formal)
        self.callers = []
    def __str__(self):
        rep = "Function '" + self.id + "'\n"
        rep += "formals:\n"
        for id, record in zip(self.formals, self.formals.values()):
            rep += id + " " + record.getType() + "\n"
        rep += "callers:\n"
        for caller in self.callers:
            rep += caller + "\n"
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
