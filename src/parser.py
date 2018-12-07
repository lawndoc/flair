#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.token import TokenType, Token
from src.linkedStack import LinkedStack
from src.errors import ParseError
from src import AST
from src.parseTable import NonTerminal, parse_table

def excepthook(type, value, traceback):
    print(str(value))

sys.excepthook = excepthook

class Parser:
    def __init__(self, scanner):
        self.parseStack = LinkedStack()
        self.semanticStack = LinkedStack()
        self.last = None
        self.scanner = scanner



    def parse(self):
        self.parseStack.push("$")
        self.parseStack.push(NonTerminal.Program)
        while self.parseStack.peek() != "$":
            A = self.parseStack.peek()
            if self.scanner.peek() == "EOF":
                t = "EOF"
                tVal = "EOF"
            else:
                t = self.scanner.peek().getType()
                tVal = self.scanner.peek().getValue()
            # print("\nSemantic Stack:")
            # for node in self.semanticStack:
            #     print(type(node))
            # print("Top of Parse Stack:", A)
            # print("Next token:", t, "(", tVal, ")")

            if isinstance(A, TokenType):
                if A == t:
                    self.last = tVal
                    self.parseStack.pop()
                    self.scanner.next()
                else:
                    # If print is declared as a function identifier, recast print_statement token as identifier token
                    if not (A == TokenType.identifier and t == TokenType.print_statement):
                        error_msg = "Parsing error: Expected {} but found {}"
                        raise ParseError(error_msg.format(A,t))
                    else:
                        self.scanner.replaceNext(Token(TokenType.identifier, "print"))
            elif isinstance(A, NonTerminal):
                if (A,t) in parse_table:
                    self.parseStack.pop()
                    if "ε" in parse_table[(A,t)]:  # rule is ε, push nothing onto stack
                        continue
                    else:
                        reversedRule = parse_table[(A,t)].copy()
                        reversedRule.reverse()
                        for y in reversedRule:
                            self.parseStack.push(y)
                else:
                    # If print is declared as a function identifier, recast print_statement token as identifier token
                    if not ((A == NonTerminal.Expr or A == NonTerminal.Term or A == NonTerminal.Factor) and t == TokenType.print_statement):
                        error_msg = "Parsing Error: No transition for {} from {}"
                        raise ParseError(error_msg.format(A,t))
                    else:
                        self.scanner.replaceNext(Token(TokenType.identifier, "print"))
            elif issubclass(A, AST.ASTnode):
                self.parseStack.pop()
                self.semanticStack.push(A(self.last, self.semanticStack))
            else:
                error_msg = "Parsing Error: An unidentified object is on the stack: {}"
                raise ParseError(error_msg.format(A))

        # end of loop, program threw no errors
        if self.scanner.peek() != "EOF":
            error_msg = "Parsing Error: Code found after end of program."
            raise ParseError(error_msg)
        else:
            return self.semanticStack.pop()
