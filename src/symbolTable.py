#!/usr/bin/python3


class FormalRecord:
    def __init__(self, formalNode):
        self.id = formalNode.getName()
        self.type = formalNode.getType()
    def getName(self):
        return self.id
    def getType(self):
        return self.type

class FunctionRecord:
    def __init__(self, functionNode):
        self.id = functionNode.getName()
        self.type = functionNode.getType()
        self.formals = {}
        for formal in functionNode.getFormals():
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
