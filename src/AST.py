#!/usr/bin/python3

class ASTnode():
    def __init__(self, last, semanticStack):
        pass

class PrintStatement(ASTnode):
    def __init__(self, last, semanticStack):
        expr = semanticStack.pop()

class LessThan(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()

class EqualTo(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()

class PlusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        right = semanticStack.pop()
        left = semanticStack.pop()

"""TODO"""

class Identifier(ASTnode):
    def __init__(self, last, semanticStack):
        value = last

"""TODO"""

class Program(ASTnode):
    def __init__(self, last, semanticStack):
        body = semanticStack.pop()
        definitions = semanticStack.pop()
        if isinstance(semanticStack.peek(), Formals):
            semanticStack.pop()
        identifier = semanticStack.pop()

class Formals(ASTnode):
    def __init__(self, last, semanticStack):
        formals = []
        while isinstance(semanticStack.peek(), Formal):
            formals.append(semanticStack.pop())
        formals.reverse()
    def __iter__(self):
        for formal in self.formals:
            yield formal
        raise StopIteration

class Formal(ASTnode):
    def __init__(self, last, semanticStack):
        type = semanticStack.pop()
        identifier = semanticStack.pop()

"""TODO"""
