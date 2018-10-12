#!/usr/bin/python3

class colors():
    blue = "\033[34m"
    green = "\033[4m"
    yellow = "\33[33m"
    red = "\033[91m"
    brown = "033[36m"
    white = "\033[0m"

class ASTnode(object):
    def __init__(self, last, semanticStack):
        pass

class PrintStatement(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + colors.green + "print\n" + colors.white
        rep += self.expr.__str__(level+1)
        return rep

class LessThan(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " < " + colors.white + self.right.__str__()

class EqualTo(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " = " + colors.white + self.right.__str__()

class PlusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " + "+ colors.white + self.right.__str__()

class MinusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " - " + colors.white + self.right.__str__()

class TimesExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " * " + colors.white + self.right.__str__()

class DivideExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " / " + colors.white + self.right.__str__()

class AndExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " and " + colors.white + self.right.__str__()

class OrExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " or " + colors.white + self.right.__str__()

class NotExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
    def __str__(self, level = 0):
        return "\t" * level + colors.blue + "not " + colors.white + self.expr.__str__()

class IfStatement(ASTnode):
    def __init__(self, last, semanticStack):
        self.elseExpr = semanticStack.pop()
        self.thenExpr = semanticStack.pop()
        self.ifExpr = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + colors.red + "if " + colors.white
        rep += self.ifExpr.__str__()
        rep += colors.red + " then \n" + colors.white
        rep += self.thenExpr.__str__(level+1) + "\n"
        rep += "\t" * level + colors.red + "else \n" + colors.white
        rep += self.elseExpr.__str__(level+1) + "\n"
        return rep

class Identifier(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
    def __str__(self, level = 0):
        return "\t" * level + colors.brown + str(self.value) + colors.white

class IntegerLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white

class BooleanLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white

class Type(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white

class NegateExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.factor = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + colors.blue + "- " + colors.white + self.factor.__str__()
        return rep

class Program(ASTnode):
    def __init__(self, last, semanticStack):
        self.body = semanticStack.pop()
        self.definitions = semanticStack.pop()
        if isinstance(semanticStack.peek(), Formals):
            self.formals = semanticStack.pop()
        else:
            self.formals = None
        self.identifier = semanticStack.pop()
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

class Definitions(ASTnode):
    def __init__(self, last, semanticStack):
        self.definitions = []
        while isinstance(semanticStack.peek(), Function):
            self.definitions.append(semanticStack.pop())
        self.definitions.reverse()
    def __iter__(self):
        for function in self.definitons:
            yield function
        raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for function in self.definitions:
            rep += function.__str__(level+1)
        return rep

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

class Body(ASTnode):
    def __init__(self, last, semanticStack):
        self.returnStatement = semanticStack.pop()
        self.printStatements = []
        while isinstance(semanticStack.peek(), PrintStatement):
            self.printStatements.append(semanticStack.pop())
        self.printStatements.reverse()
    def __str__(self, level = 0):
        rep = ""
        if self.printStatements:
            for p in self.printStatements:
                rep += p.__str__(level)
                rep += "\n"
        rep += self.returnStatement.__str__(level)
        rep += "\n"
        return rep


class ReturnStatement(ASTnode):
    def __init__(self, last, semanticStack):
        self.retStatement = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + colors.green + "return \n" + colors.white
        rep += self.retStatement.__str__(level+1)
        return rep

class FunctionCall(ASTnode):
    def __init__(self, last, semanticStack):
        if isinstance(semanticStack.peek(), Actuals):
            self.actuals = semanticStack.pop()
        else:
            self.actuals = None
        self.identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + self.identifier.__str__()
        rep += "("
        if self.actuals:
            rep += self.actuals.__str__()
        rep += ")"
        return rep

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

class Actual(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
    def __str__(self, level=0):
        rep = self.expr.__str__()
        return rep
