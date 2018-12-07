#!/usr/bin/python3

import sys

def excepthook(type, value, traceback):
    print("Unexpected Compiler Error in SymbolTable")

sys.excepthook = excepthook

class SymbolTable():
    def __init__(self):
        self.table = {}
        self.errors = False
        self.lineNum = 0
        self.stack = []
        self.printAddress = 0
        self.fromFCall = False
        self.ifNum = -1
        self.elses = []
        self.fis = []
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
    def setPrintAddress(self, addr):
        self.printAddress = addr
    def getPrintAddress(self):
        return str(self.printAddress)
    def setLineNum(self, num):
        self.lineNum = num
    def getLineNum(self):
        return self.lineNum
    def nextLine(self):
        self.lineNum += 1
        return str(self.lineNum - 1)
    def stackPush(self,new):
        self.stack.append(new)
    def stackPop(self):
        return self.stack.pop()
    def stackPeek(self):
        return self.stack[-1]
    def stackLast(self):
        return self.stack[-2]
    def stackIsEmpty(self):
        if len(self.stack) == 1:
            return True
        else:
            return False
    def fromCall(self):
        self.fromFCall = True
    def notFromCall(self):
        self.fromFCall = False
    def isFromCall(self):
        return self.fromFCall
    def nextIfNum(self):
        self.ifNum += 1
    def getIfNum(self):
        return self.ifNum
    def newElse(self, address):
        self.elses.append(address)
    def getElse(self, i):
        return str(self.elses[i])
    def newFi(self, address):
        self.fis.append(address)
    def getFi(self, i):
        return str(self.fis[i])


class FormalRecord:
    def __init__(self, formalNode, pos):
        self.id = formalNode.getName()
        self.type = formalNode.getType()
        self.pos = pos
        self.called = False
    def newCall(self):
        self.called = True
    def isCalled(self):
        return self.called
    def getPos(self):
        return self.pos
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
        self.node = functionNode
        self.tail = functionNode.checkIfTail()
        if functionNode.getFormals():
            pos = 0
            for formal in functionNode.getFormals():
                # Make sure each identifier is only defined once
                if formal.getName() in self.formals:
                    self.formalError = True
                    print("Semantic error: identifier '{}' is defined more than once in function '{}'".format(formal.getName(), self.id))
                self.formals[formal.getName()] = FormalRecord(formal, pos)
                pos += 1
        self.callers = []
        self.codeAddress = 0
        self.offsets = []
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
        return str(self.codeAddress)
    def setOffset(self, value):
        if self.offsets:
            self.offsets[-1] = value
        else:
            self.offsets.append(value)
    def decrementOffset(self, amount = 1):
        if self.offsets:
            self.offsets[-1] -= amount
    def getOffset(self):
        if self.offsets:
            return self.offsets[-1]
        else:
            return -7
    def newOffset(self, new):
        self.offsets.append(new)
    def lastOffset(self):
        self.offsets.pop()
    def peekLastOffset(self):
        return self.offsets[-2]
    def isNotTail(self):
        return self.tail
    def getBody(self):
        return self.node.body
