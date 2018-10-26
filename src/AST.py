#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.errors import semanticError
from src.symbolTable import FunctionRecord, FormalRecord

class colors():
    blue = "\033[34m"
    green = "\033[92m"
    yellow = "\033[33m"
    red = "\033[91m"
    brown = "\033[35m"
    white = "\033[0m"

class ASTnode(object):
    def __init__(self, last, semanticStack):
        pass

class PrintStatement(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        rep = "\t" * level + colors.green + "print\n" + colors.white
        rep += self.expr.__str__(level+1)
        return rep
    def annotate(self, defs, ids, fName):
        self.expr.annotate(defs, ids, fName)
        self.setType(self.expr.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class LessThan(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " < " + colors.white + self.right.__str__()
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "integer" and self.left.getType() == "integer":
            self.setType("boolean")
        else:
            self.setType("error | bad comparison operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class EqualTo(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " = " + colors.white + self.right.__str__()
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "integer" and self.left.getType() == "integer":
            self.setType("boolean")
        else:
            self.setType("error | bad comparison operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class PlusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " + "+ colors.white + self.right.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "integer" and self.left.getType() == "integer":
            self.setType("integer")
        else:
            self.setType("error | bad arithmetic operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class MinusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " - " + colors.white + self.right.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "integer" and self.left.getType() == "integer":
            self.setType("integer")
        else:
            self.setType("error | bad arithmetic operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class TimesExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " * " + colors.white + self.right.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "integer" and self.left.getType() == "integer":
            self.setType("integer")
        else:
            self.setType("error | bad arithmetic operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class DivideExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " / " + colors.white + self.right.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "integer" and self.left.getType() == "integer":
            self.setType("integer")
        else:
            self.setType("error | bad arithmetic operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class AndExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " and " + colors.white + self.right.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "boolean" and self.left.getType() == "boolean":
            self.setType("boolean")
        else:
            self.setType("error | bad boolean operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class OrExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " or " + colors.white + self.right.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.right.annotate(defs, ids, fName)
        self.left.annotate(defs, ids, fName)
        if self.right.getType() == "boolean" and self.left.getType() == "boolean":
            self.setType("boolean")
        else:
            self.setType("error | bad boolean operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class NotExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + "(" + colors.blue + "not " + colors.white + self.expr.__str__() + ")"
    def annotate(self, defs, ids, fName):
        self.expr.annotate(defs, ids, fName)
        if self.expr.getType() == "boolean":
            self.setType("boolean")
        else:
            self.setType("error | bad boolean operation")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class IfStatement(ASTnode):
    def __init__(self, last, semanticStack):
        self.elseExpr = semanticStack.pop()
        self.thenExpr = semanticStack.pop()
        self.ifExpr = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        rep = "\t" * level + colors.red + "if " + colors.white
        rep += self.ifExpr.__str__()
        rep += colors.red + " then \n" + colors.white
        rep += self.thenExpr.__str__(level+1) + "\n"
        rep += "\t" * level + colors.red + "else \n" + colors.white
        rep += self.elseExpr.__str__(level+1) + "\n"
        return rep
    def annotate(self, defs, ids, fName):
        self.ifExpr.annotate(defs, ids, fName)
        self.thenExpr.annotate(defs, ids, fName)
        self.elseExpr.annotate(defs, ids, fName)
        if any("error" in t.getType() for t in [self.ifExpr, self.thenExpr, self.elseExpr]):
            self.setType("error | inherited")
        elif self.ifExpr.getType() != "boolean":
            self.setType("error | non-boolean if")
        elif self.thenExpr.getType() == self.elseExpr.getType():
            self.setType(self.thenExpr.getType())
        else:
            self.setType("error | inconsistent return type")
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Identifier(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
        self.type = None
    def __str__(self, level = 0):
        return "\t" * level + colors.brown + str(self.value) + colors.white
    def annotate(self, defs, ids, fName):
        try:
            self.setType(ids[self.getName()].getType())
        except:
            self.setType("error | bad id call")
    def getName(self):
        return self.value
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class IntegerLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
        self.type = "integer"
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white
    def annotate(self, defs, ids, fName):
        pass
    def setType(self, myType):
        if myType != "integer":
            error_msg = "tried to assign {} type to integer literal {}"
            raise semanticError(error_msg.format(myType, self.value))
    def getType(self):
        return self.type

class BooleanLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
        self.type = "boolean"
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white
    def annotate(self, defs, ids, fName):
        pass
    def setType(self, myType):
        if myType != "boolean":
            error_msg = "tried to assign {} type to boolean literal {}"
            raise semanticError(error_msg.format(myType, self.value))
    def getType(self):
        return self.type

class Type(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white
    def getType(self):
        return self.value

class NegateExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.factor = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        rep = "\t" * level + "(" + colors.blue + "- " + colors.white + self.factor.__str__() + ")"
        return rep
    def annotate(self, defs, ids, fName):
        self.factor.annotate(defs, ids, fName)
        self.setType(self.factor.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Program(ASTnode):
    def __init__(self, last, semanticStack):
        self.body = semanticStack.pop()
        self.definitions = semanticStack.pop()
        if isinstance(semanticStack.peek(), Formals):
            self.formals = semanticStack.pop()
        else:
            self.formals = None
        self.identifier = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        rep = colors.green + "program " + colors.white
        rep += self.identifier.__str__()
        rep += " ( "
        if self.formals:
            rep += self.formals.__str__()
        rep += " );\n"
        rep += self.definitions.__str__(level+1)
        rep += colors.green + "begin\n" + colors.white
        rep += self.body.__str__(level+1)
        rep += colors.green + "end" + colors.white + ".\n"
        return rep
    def annotate(self):
        defs = {}
        ids = {}
        for function in self.definitons:
            defs[function.getName()] = FunctionRecord(function)
        for formal in self.formals:
            ids[formal.getName()] = FormalRecord(formal)
        self.definitions.annotate(defs)
        self.body.annotate(defs, ids, self.getName())
        self.setType(self.body.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type
    def getName(self):
        return self.identifier.getName()

class Formals(ASTnode):
    def __init__(self, last, semanticStack):
        self.formals = [semanticStack.pop()]
        while isinstance(semanticStack.peek(), Formal):
            self.formals.append(semanticStack.pop())
        self.formals.reverse()
    def __iter__(self):
        for formal in self.formals:
            yield formal
        raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for formal in self.formals:
            rep += formal.__str__()
            rep += ", "
        rep = rep[:-2]
        return rep

class Formal(ASTnode):
    def __init__(self, last, semanticStack):
        self.type = semanticStack.pop()
        self.identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.identifier.__str__()
        rep += " : "
        rep += self.type.__str__()
        return rep
    def getName(self):
        return self.identifier.getName()
    def getType(self):
        return self.type.getType()

class Definitions(ASTnode):
    def __init__(self, last, semanticStack):
        self.definitions = []
        while isinstance(semanticStack.peek(), Function):
            self.definitions.append(semanticStack.pop())
        self.definitions.reverse()
        self.type = None
    def __iter__(self):
        for function in self.definitons:
            yield function
        raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for function in self.definitions:
            rep += function.__str__(level+1)
        return rep
    def annotate(self, defs):
        for function in self.definitions:
            function.annotate(defs)
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Function(ASTnode):
    def __init__(self, last, semanticStack):
        self.body = semanticStack.pop()
        self.type = semanticStack.pop()
        if isinstance(semanticStack.peek(), Formals):
            self.formals = semanticStack.pop()
        else:
            self.formals = None
        self.identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + colors.green + "function " + colors.white
        rep += self.identifier.__str__()
        rep += " ( "
        if self.formals:
            rep += self.formals.__str__()
        rep += " ) : "
        rep += self.type.__str__()
        rep += "\n" + "\t" * level + colors.green + "begin\n" + colors.white
        rep += self.body.__str__(level+1)
        rep += "\t" * level + colors.green + "end" + colors.white + ";\n"
        return rep
    def annotate(self, defs):
        self.body.annotate(defs, defs[self.getName()].getFormals(), self.getName())
        if self.body.getType() != self.getType():
            self.setType("error | wrong return type")
    def getFormals(self):
        return self.formals
    def getName(self):
        return self.identifier.getName()
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Body(ASTnode):
    def __init__(self, last, semanticStack):
        self.returnStatement = semanticStack.pop()
        self.printStatements = []
        while isinstance(semanticStack.peek(), PrintStatement):
            self.printStatements.append(semanticStack.pop())
        self.printStatements.reverse()
        self.type = None
    def __str__(self, level = 0):
        rep = ""
        if self.printStatements:
            for p in self.printStatements:
                rep += p.__str__(level)
                rep += "\n"
        rep += self.returnStatement.__str__(level)
        rep += "\n"
        return rep
    def annotate(self, defs, ids, fName):
        for ps in self.printStatements:
            ps.annotate(defs, ids, fName)
        self.returnStatement.annotate(defs, ids, fName)
        if any(ps.getType() == "error" for ps in self.printStatements):
            self.setType("error | inherited from print statement")
        else:
            self.setType(self.returnStatement.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class ReturnStatement(ASTnode):
    def __init__(self, last, semanticStack):
        self.retStatement = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        rep = "\t" * level + colors.green + "return \n" + colors.white
        rep += self.retStatement.__str__(level+1)
        return rep
    def annotate(self, defs, ids, fName):
        self.retStatement.annotate(defs, ids, fName)
        self.setType(self.retStatement.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class FunctionCall(ASTnode):
    def __init__(self, last, semanticStack):
        if isinstance(semanticStack.peek(), Actuals):
            self.actuals = semanticStack.pop()
        else:
            self.actuals = None
        self.identifier = semanticStack.pop()
        self.type = None
    def __str__(self, level = 0):
        rep = "\t" * level + self.identifier.__str__()
        rep += "("
        if self.actuals:
            rep += self.actuals.__str__()
        rep += ")"
        return rep
    def annotate(self, defs, ids, fName):
        self.actuals.annotate(defs, ids, fName)
        try:
            self.setType(defs[self.getName()].getType())
            defs.addCaller(fName)
            ## TODO: return defs
        except:
            self.setType("error | bad function call")
            defs[self.getName()].addCaller(fName)
            ## TODO: return defs
    def getName(self):
        return self.identifier.getName()
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Actuals(ASTnode):
    def __init__(self, last, semanticStack):
        self.actuals = [semanticStack.pop()]
        while isinstance(semanticStack.peek(), Actual):
            self.actuals.append(semanticStack.pop())
        self.actuals.reverse()
    def __iter__(self):
        for actual in self.actuals:
            yield actual
        raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for actual in self.actuals:
            rep += actual.__str__()
            rep += ", "
        rep = rep[:-2]
        return rep
    def annotate(self, defs, ids, fName):
        for actual in self.actuals:
            actual.annotate(defs, ids, fName)
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Actual(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
        self.type = None
    def __str__(self, level=0):
        rep = self.expr.__str__()
        return rep
    def annotate(self, defs, ids, fName):
        self.expr.annotate(defs, ids, fName)
        self.setType(self.expr.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type
