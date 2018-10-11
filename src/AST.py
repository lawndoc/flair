#!/usr/bin/python3

class ASTnode():
    def __init__(self, last, semanticStack):
        pass

class PrintStatement(ASTnode):
    def __init__(self, last, semanticStack):
        expr = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "print: \n"
        rep += self.expr.__str__(level+1)
        return rep

class LessThan(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "< \n"
        rep += self.right.__str__(level+1)
        return rep

class EqualTo(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "= \n"
        rep += self.right.__str__(level+1)
        return rep

class PlusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "+ \n"
        rep += self.right.__str__(level+1)
        return rep

class MinusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "- \n"
        rep += self.right.__str__(level+1)
        return rep

class TimesExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "* \n"
        rep += self.right.__str__(level+1)
        return rep

class DivideExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "/ \n"
        rep += self.right.__str__(level+1)
        return rep

class AndExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "and \n"
        rep += self.right.__str__(level+1)
        return rep

class OrExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.left.__str__(level+1)
        rep += "\t" * level + "or \n"
        rep += self.right.__str__(level+1)
        return rep

class NotExpr(ASTnode):
    def __init__(self, last, semanticStack):
        expr = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "not \n"
        rep += self.expr.__str__(level+1)
        return rep

class IfStatement(ASTnode):
    def __init__(self, last, semanticStack):
        elseExpr = semanticStack.pop()
        thenExpr = semanticStack.pop()
        ifExpr = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "if: \n"
        rep += self.ifExpr.__str__(level+1)
        rep += "\t" * level + "then: \n"
        rep += self.thenExpr.__str__(level+1)
        rep += "\t" * level + "else: \n"
        rep += self.elseExpr.__str__(level+1)
        return rep

class Identifier(ASTnode):
    def __init__(self, last, semanticStack):
        value = last
    def __str__(self, level = 0):
        rep = "\t" * level + self.value + "\n"
        return rep

class IntegerLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        value = last
    def __str__(self, level = 0):
        rep = "\t" * level + self.value + "\n"
        return rep

class BooleanLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        value = last
    def __str__(self, level = 0):
        rep = "\t" * level + self.value + "\n"
        return rep

class Type(ASTnode):
    def __init__(self, last, semanticStack):
        value = last
    def __str__(self, level = 0):
        rep = "\t" * level + self.value + "\n"
        return rep

class NegateExpr(ASTnode):
    def __init__(self, last, semanticStack):
        factor = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "- \n"
        rep += self.factor.__str__(level+1)
        return rep

class Program(ASTnode):
    def __init__(self, last, semanticStack):
        body = semanticStack.pop()
        definitions = semanticStack.pop()
        if isinstance(semanticStack.peek(), Formals):
            formals = semanticStack.pop()
        else:
            formals = None
        identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "program: \n"
        rep += self.identifier.__str__(level+1)
        if self.formals:
            rep += self.formals.__str__(level+1)
        rep += self.definitions.__str__(level+1)
        rep += self.body.__str__(level+1)
        return rep


class Formals(ASTnode):
    def __init__(self, last, semanticStack):
        formals = [semanticStack.pop()]
        while isinstance(semanticStack.peek(), Formal):
            formals.append(semanticStack.pop())
        formals.reverse()
    def __iter__(self):
        for formal in self.formals:
            yield formal
        raise StopIteration
    def __str__(self, level = 0):
        rep = "\t" * level + "formals: \n"
        for formal in self.formals:
            rep += formal.__str__(level+1)
        return rep

class Formal(ASTnode):
    def __init__(self, last, semanticStack):
        type = semanticStack.pop()
        identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.identifier.__str__(level+1)
        rep += "\t" * level + "formal: \n"
        rep += self.type.__str__(level+1)
        return rep

class Definitions(ASTnode):
    def __init__(self, last, semanticStack):
        definitions = []
        while isinstance(semanticStack.peek(), Function):
            definitions.append(semanticStack.pop())
        self.definitons.reverse()
    def __iter__(self):
        for function in self.definitons:
            yield function
        raise StopIteration
    def __str__(self, level = 0):
        rep = "\t" * level + "definitons: \n"
        for function in self.definitons:
            rep += function.__str__(level+1)
        return rep

class Function(ASTnode):
    def __init__(self, last, semanticStack):
        body = semanticStack.pop()
        type = semanticStack.pop()
        if isinstance(semanticStack.peek(), Formals):
            formals = semanticStack.pop()
        else:
            formals = None
        identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "function: \n"
        rep += self.identifier.__str__(level+1)
        if self.formals:
            rep += self.formals.__str__(level+1)
        rep += "\t" * level+1 + "returns type: \n"
        rep += self.type.__str__(level+1)
        rep += self.body.__str__(level+1)
        return rep

class Body(ASTnode):
    def __init__(self, last, semanticStack):
        returnStatement = semanticStack.pop()
        printStatements = []
        while isinstance(semanticStack.peek(), PrintStatement):
            printStatements.append(semanticStack.pop())
        printStatements.reverse()
    def __str__(self, level = 0):
        rep = ""
        if self.printStatments:
            for p in self.printStatements:
                rep += p.__str__(level+1)
        rep += self.returnStatement.__str__(level+1)


class ReturnStatement(ASTnode):
    def __init__(self, last, semanticStack):
        retStatement = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "return: \n"
        rep += self.retStatement.__str__(level+1)
        return rep

class FunctionCall(ASTnode):
    def __init__(self, last, semanticStack):
        if isinstance(semanticStack.peek(), Actuals):
            actuals = semanticStack.pop()
        else:
            actuals = None
        identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = "\t" * level + "program: \n"
        rep += self.identifier.__str__(level+1)
        if self.actuals:
            rep += self.actuals.__str__(level+1)
        return rep

class Actuals(ASTnode):
    def __init__(self, last, semanticStack):
        actuals = [semanticStack.pop()]
        while isinstance(semanticStack.peek(), (LessThan, EqualTo, PlusExpr,
            MinusExpr, TimesExpr, DivideExpr, AndExpr, OrExpr, NotExpr,
            IfStatement, Identifier, IntegerLiteral, BooleanLiteral, Type,
            NegateExpr, FunctionCall)):
            actuals.append(semanticStack.pop())
        actuals.reverse()
    def __iter__(self):
        for expr in self.actuals:
            yield expr
        raise StopIteration
    def __str__(self, level = 0):
        rep = "\t" * level + "actuals: \n"
        for expr in self.actuals:
            rep += expr.__str__(level+1)
