#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.errors import SemanticError
from src.symbolTable import SymbolTable, FunctionRecord, FormalRecord

# def excepthook(type, value, traceback):
#     print(str(value))
#
# sys.excepthook = excepthook


def lineRO(symbolTable, instruction, r1, r2, r3, comment = ""):
    if comment:
        comment = "\t# {}".format(comment)
    return "{}: {} {},{},{}{}\n".format(str(symbolTable.nextLine()),instruction,str(r1),str(r2),str(r3),comment)

def lineRM(symbolTable, instruction, r1, offset, r2, comment = ""):
    if comment:
        comment = "\t# {}".format(comment)
    return "{}: {} {},{}({}){}\n".format(str(symbolTable.nextLine()),instruction,str(r1),str(offset),str(r2),comment)

def header(name):
    return "*\n* {}\n*\n".format(name)

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
    def analyze(self, symbolTable, ids, fName):
        # Analyze expression to be printed and annotate symbolTable
        self.expr.analyze(symbolTable, ids, fName)
        self.setType(self.expr.getType())
    # TODO: 6th -- genCode() for printStatements (do last)
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class LessThan(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "boolean"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " < " + colors.white + self.right.__str__()
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure both sides of the comparison are integer expressions
        if not (self.right.getType() == "integer" and self.left.getType() == "integer"):
            symbolTable.newError()
            print("Semantic error: non-integer < comparison in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRO(symbolTable,"SUB",1,1,2,"subtract right operand from the left")
        code += lineRM(symbolTable,"JLT",1,2,7,"jump if left < right")
        code += lineRM(symbolTable,"ST",0,-1,6,"load false into new temp var")
        code += lineRM(symbolTable,"LDA",7,2,7,"skip not equal")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 (true) into r1")
        code += lineRM(symbolTable,"ST",1,-1,6,"load true into new temp var")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class EqualTo(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "boolean"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + self.left.__str__() + colors.blue + " = " + colors.white + self.right.__str__()
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure both sides of the comparison are integer expressions
        if not (self.right.getType() == "integer" and self.left.getType() == "integer"):
            symbolTable.newError()
            print("Semantic error: non-integer = comparison in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRO(symbolTable,"SUB",1,1,2,"subtract right operand from the left")
        code += lineRM(symbolTable,"JEQ",1,2,7,"jump if left equals right")
        code += lineRM(symbolTable,"ST",0,-1,6,"load false into new temp var")
        code += lineRM(symbolTable,"LDA",7,2,7,"skip not equal")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 (true) into r1")
        code += lineRM(symbolTable,"ST",1,-1,6,"load true into new temp var")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class PlusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "integer"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " + "+ colors.white + self.right.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure both sides of the addition are integer expressions
        if not (self.right.getType() == "integer" and self.left.getType() == "integer"):
            symbolTable.newError()
            print("Semantic error: non-integer + operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRO(symbolTable,"ADD",1,1,2,"add the two values")
        code += lineRM(symbolTable,"ST",1,-1,6,"store sum into new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class MinusExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "integer"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " - " + colors.white + self.right.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure both sides of the subraction are integer expressions
        if not (self.right.getType() == "integer" and self.left.getType() == "integer"):
            symbolTable.newError()
            print("Semantic error: non-integer - operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRO(symbolTable,"SUB",1,1,2,"subtract the two values")
        code += lineRM(symbolTable,"ST",1,-1,6,"store difference into new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class TimesExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "integer"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " * " + colors.white + self.right.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure both sides of the multiply are integer expressions
        if not (self.right.getType() == "integer" and self.left.getType() == "integer"):
            symbolTable.newError()
            print("Semantic error: non-integer * operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRO(symbolTable,"MUL",1,1,2,"multiply the two values")
        code += lineRM(symbolTable,"ST",1,-1,6,"store product into new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class DivideExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "integer"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " / " + colors.white + self.right.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure both sides of the divide are integer expressions
        if not (self.right.getType() == "integer" and self.left.getType() == "integer"):
            symbolTable.newError()
            print("Semantic error: non-integer / operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRO(symbolTable,"DIV",1,1,2,"divide the r1 by r2")
        code += lineRM(symbolTable,"ST",1,-1,6,"store quotient into new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class AndExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "boolean"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " and " + colors.white + self.right.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure things being and'd are boolean expressions
        if not (self.right.getType() == "boolean" and self.left.getType() == "boolean"):
            symbolTable.newError()
            print("Semantic error: non-boolean 'and' operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRM(symbolTable,"LDC",3,2,0,"load 2 into r3 (true + true)")
        code += lineRO(symbolTable,"ADD",1,1,2,"add left and right boolean")
        code += lineRO(symbolTable,"SUB",1,3,1,"subtract the added booleans from 2")
        code += lineRM(symbolTable,"JNE",1,2,7,"jump if left and right is false")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 (true) into r1")
        code += lineRM(symbolTable,"LDA",7,1,7,"skip loading 0 (false)")
        code += lineRM(symbolTable,"LDC",1,0,0,"load 0 (false) into r1")
        code += lineRM(symbolTable,"ST",1,-1,6,"store boolean into new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class OrExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.right = semanticStack.pop()
        self.left = semanticStack.pop()
        self.type = "boolean"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + self.left.__str__() + colors.blue + " or " + colors.white + self.right.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze left and right expressions and annotate symbolTable
        self.right.analyze(symbolTable, ids, fName)
        self.left.analyze(symbolTable, ids, fName)
        # Make sure things being or'd are boolean expressions
        if not (self.right.getType() == "boolean" and self.left.getType() == "boolean"):
            symbolTable.newError()
            print("Semantic error: non-boolean 'or' operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.left.genCode(symbolTable, code, fName)
        leftValOffset = self.left.getValueOffset()
        code = self.right.genCode(symbolTable, code, fName)
        rightValOffset = self.right.getValueOffset()
        code += lineRM(symbolTable,"LD",1,leftValOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"LD",2,rightValOffset,5,"load right operand value into r2")
        code += lineRM(symbolTable,"JNE",1,3,7,"jump if left is true")
        code += lineRM(symbolTable,"JNE",2,2,7,"jump if right is true")
        code += lineRM(symbolTable,"LDC",1,0,0,"load 0 (false) into r1")
        code += lineRM(symbolTable,"LDA",7,1,7,"skip loading 1 (true)")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 (true) into r1")
        code += lineRM(symbolTable,"ST",1,-1,6,"store boolean into new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class NotExpr(ASTnode):
    def __init__(self, last, semanticStack):
        self.expr = semanticStack.pop()
        self.type = "boolean"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + "(" + colors.blue + "not " + colors.white + self.expr.__str__() + ")"
    def analyze(self, symbolTable, ids, fName):
        # Analyze boolean expression to be negated and annotate symbolTable
        self.expr.analyze(symbolTable, ids, fName)
        # Make sure thing being negated is a boolean expression
        if self.expr.getType() != "boolean":
            symbolTable.newError()
            print("Semantic error: non-boolean 'not' operation in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.expr.genCode(symbolTable, code, fName)
        childValOffset = self.expr.getValueOffset()
        code += lineRM(symbolTable,"LD",1,childValOffset,5,"load operand value into r1")
        code += lineRM(symbolTable,"JNE",1,3,7,"jump if operand is true")
        code += lineRM(symbolTable,"LDC",1,1,0,"change operand to true")
        code += lineRM(symbolTable,"ST",1,0,6,"load true into same temp value")
        code += lineRM(symbolTable,"LDA",7,1,7,"skip switching temp to false")
        code += lineRM(symbolTable,"ST",0,0,6,"load false into same temp value")
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
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
        self.valueOffset = 0
    def __str__(self, level = 0):
        rep = "\t" * level + colors.red + "if " + colors.white
        rep += self.ifExpr.__str__()
        rep += colors.red + " then \n" + colors.white
        rep += self.thenExpr.__str__(level+1) + "\n"
        rep += "\t" * level + colors.red + "else \n" + colors.white
        rep += self.elseExpr.__str__(level+1) + "\n"
        return rep
    def analyze(self, symbolTable, ids, fName):
        # Analyze if, then, and else expressions and annotate symbolTable
        self.ifExpr.analyze(symbolTable, ids, fName)
        self.thenExpr.analyze(symbolTable, ids, fName)
        self.elseExpr.analyze(symbolTable, ids, fName)
        # Make sure the if check is a boolean expression
        if self.ifExpr.getType() != "boolean":
            symbolTable.newError()
            print("Semantic error: non-boolean 'if' check in function '{}'".format(fName))
        # Make sure the then and else expressions return the same type
        if self.thenExpr.getType() == self.elseExpr.getType():
            self.setType(self.thenExpr.getType())
        else:
            self.setType("unknown")
            symbolTable.newError()
            print("Semantic error: inconsistent return type under if-then-else in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.ifExpr.genCode(symbolTable, code, fName)
        ifValOffset = self.ifExpr.getValueOffset()
        code = self.thenExpr.genCode(symbolTable, code, fName)
        thenValOffset = self.thenExpr.getValueOffset()
        code = self.elseExpr.genCode(symbolTable, code, fName)
        elseValOffset = self.elseExpr.getValueOffset()
        code += lineRM(symbolTable,"LD",1,ifValOffset,5,"load if check value into r1")
        code += lineRM(symbolTable,"LD",2,thenValOffset,5,"load then value into r2")
        code += lineRM(symbolTable,"LD",3,elseValOffset,5,"load else value into r3")
        code += lineRM(symbolTable,"JEQ",1,2,7,"jump to else value if false")
        code += lineRM(symbolTable,"ST",2,-1,6,"store then value to new temp value")
        code += lineRM(symbolTable,"LDA",7,1,7,"skip else case")
        code += lineRM(symbolTable,"ST",3,-1,6,"store else value to new temp value")
        code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1")
        code += lineRO(symbolTable,"SUB",6,6,1,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Identifier(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
        self.type = None
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + colors.brown + str(self.value) + colors.white
    def analyze(self, symbolTable, ids, fName):
        # Make sure identifier references an argument passed into the current function
        try:
            self.setType(ids[self.getName()].getType())
            ids[self.getName()].newCall()
        except:
            self.setType("unknown")
            symbolTable.newError()
            print("Semantic error: reference to unknown identifier '{}' in function '{}'".format(self.value, fName))
    def genCode(self, symbolTable, code, fName):
        self.valueOffset = -(symbolTable[fName].getFormals()[self.value].getPos() + 8)
        return code
    def getValueOffset(self):
        return self.valueOffset
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
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white
    def analyze(self, symbolTable, ids, fName):
        pass
    def setType(self, myType):
        if myType != "integer":
            error_msg = "tried to assign {} type to integer literal '{}'"
            raise SemanticError(error_msg.format(myType, self.value))
    def getType(self):
        return self.type
    def getValueOffset(self):
        return self.valueOffset
    def genCode(self, symbolTable, code, fName):
        code += lineRM(symbolTable,"LDC",1,self.value,0,"load {} into r1".format(self.value))
        code += lineRM(symbolTable,"ST",1,-1,6,"copy r1 into new temp value")
        code += lineRM(symbolTable,"LDC",2,1,0,"load 1 into r2")
        code += lineRO(symbolTable,"SUB",6,6,2,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code

class BooleanLiteral(ASTnode):
    def __init__(self, last, semanticStack):
        self.value = last
        self.type = "boolean"
        self.valueOffset = 0
    def __str__(self, level = 0):
        return "\t" * level + colors.yellow + str(self.value) + colors.white
    def analyze(self, symbolTable, ids, fName):
        pass
    def setType(self, myType):
        if myType != "boolean":
            error_msg = "tried to assign {} type to boolean literal '{}'"
            raise SemanticError(error_msg.format(myType, self.value))
    def genCode(self, symbolTable, code, fName):
        if self.value == "true":
            code += lineRM(symbolTable,"LDC",1,1,0,"load 1 (true) into r1")
        else: # value == "false"
            code += lineRM(symbolTable,"LDC",1,0,0,"load 0 (false) into r1")
        code += lineRM(symbolTable,"ST",1,-1,6,"copy r1 into new temp value")
        code += lineRM(symbolTable,"LDC",2,1,0,"load 1 into r2")
        code += lineRO(symbolTable,"SUB",6,6,2,"increment end of stack pointer")
        symbolTable.decrementOffset()
        self.valueOffset = symbolTable.getOffset()
        return code
    def getType(self):
        return self.type
    def getValueOffset(self):
        return self.valueOffset

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
        self.type = "integer"
        self.valueOffset = 0
    def __str__(self, level = 0):
        rep = "\t" * level + "(" + colors.blue + "- " + colors.white + self.factor.__str__() + ")"
        return rep
    def analyze(self, symbolTable, ids, fName):
        # Analyze integer or factor to be negated and annotate symbolTable
        self.factor.analyze(symbolTable, ids, fName)
        # Make sure thing being negated is integer type
        if self.factor.getType() != "integer":
            symbolTable.newError()
            print("Semantic error: '-' negation applied to non-integer in function '{}'".format(fName))
    def genCode(self, symbolTable, code, fName):
        code = self.factor.genCode(symbolTable, code, fName)
        childValOffset = self.factor.getValueOffset()
        code += lineRM(symbolTable,"LD",1,childValOffset,5,"load operand value into r1")
        code += lineRO(symbolTable,"SUB",1,0,1,"negate integer")
        code += lineRM(symbolTable,"ST",1,0,6,"load negated integer into same temp value")
        self.valueOffset = symbolTable.getOffset()
        return code
    def getValueOffset(self):
        return self.valueOffset
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
    def analyze(self):
        symbolTable = SymbolTable()
        ids = {}
        # Add all function records to symbolTable
        if self.definitions.hasDefinitions():
            for function in self.definitions:
                # Make sure function is only defined once
                if function.getName() in symbolTable:
                    symbolTable.newError()
                    print("Semantic error: function '{}' is defined more than once".format(function.getName()))
                symbolTable[function.getName()] = FunctionRecord(function)
                # Make sure each formal is only defined once (handled on creation of FunctionRecord)
                if symbolTable[function.getName()].hasFormalError():
                    symbolTable.newError()
        # Add program to symbolTable as a function record
        symbolTable[self.getName()] = FunctionRecord(self)
        symbolTable[self.getName()].setAsProgram()
        # Make sure there is no user defined function 'print'
        if "print" in symbolTable:
            symbolTable.newError()
            print("Semantic error: cannot define a function called 'print'")
        # Pass program's formals to 'ids' for program body analysis
        if self.formals:
            pos = 0
            for formal in self.formals:
                ids[formal.getName()] = FormalRecord(formal, pos)
                pos += 1
        # Analyze each function and annotate symbolTable
        self.definitions.analyze(symbolTable)
        # Analyze program body and annotate symbolTable
        self.body.analyze(symbolTable, ids, self.getName())
        self.setType(self.body.getType())
        return symbolTable
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type
    def getName(self):
        return self.identifier.getName()
    def getFormals(self):
        return self.formals
    def genCode(self, symbolTable):
        symbolTable.setLineNum(0)
        code = lineRM(symbolTable, "LD",1,0,0,"load max memory address into r1")
        code += lineRM(symbolTable,"LDA",5,0,1,"set r5 to bottom of dmem".format(self.getName()))
        code += lineRM(symbolTable,"LDA",6,0,1,"set r6 to bottom of dmem".format(self.getName()))
        ## add Activation Record for MAIN
        # load r5 and r6 into AR
        code += lineRM(symbolTable,"ST",6,-7,5,"save register 6 to AR")
        code += lineRM(symbolTable,"ST",5,-6,5,"save register 5 to AR")
        # set r6 to end of MAIN's AR
        code += lineRM(symbolTable,"LDC",2,7,0,"load 7 into r2")
        code += lineRO(symbolTable,"SUB",6,5,2,"set r6 to end of {}'s AR".format(self.getName()))
        symbolTable.setOffset(-7)
        # optionally generate code if function takes arguments
        if len(symbolTable[self.getName()].getFormals()) > 0:
            code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1 for decrementing r6")
            for i in range(0,len(symbolTable[self.getName()].getFormals())):
                code += lineRM(symbolTable,"LD",2,i+1,0,"load arg{} into r2".format(str(i+1)))
                code += lineRM(symbolTable,"ST",2,-(i+8),5,"load arg{} into AR".format(str(i+1)))
                code += lineRO(symbolTable,"SUB",6,6,1,"decrement end of stack pointer")
                symbolTable.decrementOffset()
        # add return address to MAIN'S AR
        code += lineRM(symbolTable,"LDA",1,2,7,"set r1 to return address")
        code += lineRM(symbolTable,"ST",1,-1,5,"store return address into {}'s AR".format(self.getName()))
        # jump to MAIN
        code += lineRM(symbolTable,"LDA",7,"<{}>".format(self.getName()),0,"jump to {}".format(self.getName()))
        # MAIN done, print returned value
        code += lineRM(symbolTable, "LD",2,0,5,"put return value from {} into r2".format(self.getName()))
        # add activation record for PRINT
        code += lineRM(symbolTable, "ST",2,-8,5,"move returned value into arg for PRINT's AR")
        # load r5 and r6 to AR
        code += lineRM(symbolTable,"ST",6,-7,5,"save register 6 to AR")
        code += lineRM(symbolTable,"ST",5,-6,5,"save register 5 to AR")
        # add return address to PRINT's AR
        code += lineRM(symbolTable,"LDA",3,2,7,"put return address for PRINT into r3")
        code += lineRM(symbolTable,"ST",3,-1,5,"move return address into PRINT's AR")
        # jump to PRINT
        code += lineRM(symbolTable,"LDA",7,"<PRINT>",0,"jump to PRINT")
        # final PRINT done, HALT
        code += lineRO(symbolTable,"HALT",0,0,0)
        # begin PRINT function code
        code += header("PRINT")
        symbolTable.setPrintAddress(symbolTable.getLineNum())
        code += lineRM(symbolTable,"LD",1,-8,5,"load arg from AR into r1")
        code += lineRO(symbolTable,"OUT",1,0,0,"print value")
        # restore registers
        code += lineRM(symbolTable,"LD",1,-2,5,"restore r1")
        code += lineRM(symbolTable,"LD",2,-3,5,"restore r2")
        code += lineRM(symbolTable,"LD",3,-4,5,"restore r3")
        code += lineRM(symbolTable,"LD",4,-5,5,"restore r4")
        code += lineRM(symbolTable,"LD",6,-7,5,"restore r6")
        code += lineRM(symbolTable,"LD",5,-6,5,"restore r5")
        if symbolTable.stackIsEmpty():
            code += lineRM(symbolTable,"LD",7,-1,5,"load return address into r7")
        else:
            code += lineRM(symbolTable,"LD",7,2,6,"load return address into r7")
        # generate program body code
        code += header(self.getName())
        symbolTable[self.getName()].setAddress(symbolTable.getLineNum())
        code = self.body.genCode(symbolTable, code, self.getName())
        # generate each function's code
        code = self.definitions.genCode(symbolTable, code)
        # done generating code. replace function address placeholders
        for function in symbolTable:
            placeholder = "<{}>".format(function)
            phLen = len(placeholder)
            while placeholder in code:
                code = code[:code.index(placeholder)] + \
                       symbolTable[function].getAddress() + \
                       code[code.index(placeholder)+phLen:]
        placeholder = "<PRINT>"
        phLen = len(placeholder)
        while placeholder in code:
            code = code[:code.index(placeholder)] + \
                   symbolTable.getPrintAddress() + \
                   code[code.index(placeholder)+phLen:]
        return code


class Formals(ASTnode):
    def __init__(self, last, semanticStack):
        self.formals = [semanticStack.pop()]
        while isinstance(semanticStack.peek(), Formal):
            self.formals.append(semanticStack.pop())
        self.formals.reverse()
    def __iter__(self):
        for formal in self.formals:
            yield formal
        # raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for formal in self.formals:
            rep += formal.__str__()
            rep += ", "
        rep = rep[:-2]
        return rep

class Formal(ASTnode):
    def __init__(self, last, semanticStack):
        self.type = semanticStack.pop().getType()
        self.identifier = semanticStack.pop()
    def __str__(self, level = 0):
        rep = self.identifier.__str__()
        rep += " : "
        rep += self.type.__str__()
        return rep
    def getName(self):
        return self.identifier.getName()
    def getType(self):
        return self.type

class Definitions(ASTnode):
    def __init__(self, last, semanticStack):
        self.definitions = []
        while isinstance(semanticStack.peek(), Function):
            self.definitions.append(semanticStack.pop())
        self.definitions.reverse()
        self.type = None
    def __iter__(self):
        for function in self.definitions:
            yield function
        # raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for function in self.definitions:
            rep += function.__str__(level+1)
        return rep
    def analyze(self, symbolTable):
        for function in self.definitions:
            function.analyze(symbolTable)
    def genCode(self, symbolTable, code):
        for function in self.definitions:
            code = function.genCode(symbolTable, code)
        return code
    def hasDefinitions(self):
        if self.definitions:
            return True
        else:
            return False
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type

class Function(ASTnode):
    def __init__(self, last, semanticStack):
        self.body = semanticStack.pop()
        self.type = semanticStack.pop().getType()
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
    def analyze(self, symbolTable):
        # Analyze function body and annotate symbolTable
        self.body.analyze(symbolTable, symbolTable[self.getName()].getFormals(), self.getName())
        # Make sure function returns the declared type
        if self.body.getType() != self.getType():
            symbolTable.newError()
            print("Semantic error: '{}' function's returned value doesn't match the declared return type".format(self.getName()))
    def genCode(self, symbolTable, code):
        code += header(self.getName())
        symbolTable[self.getName()].setAddress(symbolTable.getLineNum())
        code = self.body.genCode(symbolTable, code, self.getName())
        return code
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
    def analyze(self, symbolTable, ids, fName):
        # Analyze each print statement and annotate symbolTable
        for ps in self.printStatements:
            ps.analyze(symbolTable, ids, fName)
        # Analyze return statement and annotate symbolTable
        self.returnStatement.analyze(symbolTable, ids, fName)
        self.setType(self.returnStatement.getType())
    def genCode(self, symbolTable, code, fName):
        for ps in self.printStatements:
            code = ps.genCode(symbolTable, code, fName)
        code = self.returnStatement.genCode(symbolTable, code, fName)
        return code
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
    def analyze(self, symbolTable, ids, fName):
        # Analyze expression to be returned and annotate symbolTable
        self.retStatement.analyze(symbolTable, ids, fName)
        self.setType(self.retStatement.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type
    def genCode(self, symbolTable, code, fName):
        code = self.retStatement.genCode(symbolTable, code, fName) # return value is at end of stack
        valOffset = self.retStatement.getValueOffset()
        code += lineRM(symbolTable,"LD",1,valOffset,5,"load left operand value into r1")
        code += lineRM(symbolTable,"ST",1,0,5,"put value from r1 into return value")
        # restore registers
        code += lineRM(symbolTable,"LD",1,-2,5,"restore r1")
        code += lineRM(symbolTable,"LD",2,-3,5,"restore r2")
        code += lineRM(symbolTable,"LD",3,-4,5,"restore r3")
        code += lineRM(symbolTable,"LD",4,-5,5,"restore r4")
        code += lineRM(symbolTable,"LD",6,-7,5,"restore r6")
        code += lineRM(symbolTable,"LD",5,-6,5,"restore r5")
        if symbolTable.stackIsEmpty():
            code += lineRM(symbolTable,"LD",7,-1,5,"load return address into r7")
        else:
            code += lineRM(symbolTable,"LD",7,2,6,"load return address into r7")
        return code

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
    def analyze(self, symbolTable, ids, fName):
        # Analyze function call arguments (if any) and annotate symbolTable
        if self.actuals:
            self.actuals.analyze(symbolTable, ids, fName)
        # Make sure function that is being called exists
        try:
            self.setType(symbolTable[self.getName()].getType())
            symbolTable[self.getName()].addCaller(fName)
        except:
            self.setType("unknown")
            symbolTable.newError()
            print("Semantic error: call to unknown function '{}' in body of function '{}'".format(self.getName(), fName))
            return
        # Make sure call passes in correct number of args (if any)
        if self.actuals:
            if len(self.actuals) == len(symbolTable[self.getName()].getFormals()):
                # Make sure args are correct types
                for a, f in zip(self.actuals, symbolTable[self.getName()].getFormals().values()):
                    if a.getType() != f.getType():
                        symbolTable.newError()
                        print("Semantic error: in function '{}', in call to function '{}', an argument is not of the correct type".format(fName, self.getName()))
            else:
                symbolTable.newError()
                print("Semantic error: in function '{}', the call to function '{}' does not pass in the correct number of arguments".format(fName, self.getName()))
        else:
            if len(symbolTable[self.getName()].getFormals()) > 0:
                symbolTable.newError()
                print("Semantic error: in function '{}', the call to function '{}' does not pass in the correct number of arguments".format(fName, self.getName()))
    def genCode(self, symbolTable, code, fName):
        ## add Activation Record for function
        # load registers into AR
        code += lineRM(symbolTable,"ST",6,-8,6,"save register 6 to AR")
        code += lineRM(symbolTable,"ST",5,-7,6,"save register 5 to AR")
        code += lineRM(symbolTable,"ST",4,-6,6,"save register 4 to AR")
        code += lineRM(symbolTable,"ST",3,-5,6,"save register 3 to AR")
        code += lineRM(symbolTable,"ST",2,-4,6,"save register 2 to AR")
        code += lineRM(symbolTable,"ST",1,-3,6,"save register 1 to AR")
        # set r5 and r6 to beginning and end of function's AR, respectively
        code += lineRM(symbolTable,"LDA",5,-1,6,"set r5 to beginning of {}'s AR".format(self.getName()))
        code += lineRM(symbolTable,"LDC",2,7,0,"load 7 into r2")
        code += lineRO(symbolTable,"SUB",6,5,2,"set r6 to end of {}'s AR".format(self.getName()))
        symbolTable.newOffset(-7)
        # optionally generate code if function takes arguments
        if len(symbolTable[self.getName()].getFormals()) > 0:
            code += lineRM(symbolTable,"LDC",1,1,0,"load 1 into r1 for decrementing r6")
            for i in range(0,len(symbolTable[self.getName()].getFormals())):
                code += lineRM(symbolTable,"LD",2,i+1,0,"load arg{} into r2".format(str(i+1)))
                code += lineRM(symbolTable,"ST",2,-(i+8),5,"load arg{} into AR".format(str(i+1)))
                code += lineRO(symbolTable,"SUB",6,6,1,"decrement end of stack pointer")
                symbolTable.decrementOffset()
        # add return address to MAIN'S AR
        code += lineRM(symbolTable,"LDA",1,2,7,"set r1 to return address")
        code += lineRM(symbolTable,"ST",1,-1,5,"store return address into {}'s AR".format(self.getName()))
        # jump to function body
        code += lineRM(symbolTable,"LDA",7,"<{}>".format(self.getName()),0,"jump to {}".format(self.getName()))
        return code
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
        # raise StopIteration
    def __str__(self, level = 0):
        rep = ""
        for actual in self.actuals:
            rep += actual.__str__()
            rep += ", "
        rep = rep[:-2]
        return rep
    def __len__(self):
        return len(self.actuals)
    def analyze(self, symbolTable, ids, fName):
        for actual in self.actuals:
            actual.analyze(symbolTable, ids, fName)
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
    def analyze(self, symbolTable, ids, fName):
        # Analyze expression passed into function as an argument and annotate symbolTable
        self.expr.analyze(symbolTable, ids, fName)
        self.setType(self.expr.getType())
    def setType(self, myType):
        self.type = myType
    def getType(self):
        return self.type
