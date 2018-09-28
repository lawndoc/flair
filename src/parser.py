#!/usr/bin/python3

from enum import Enum
from sys import path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.token import TokenType
from src.linkedStack import LinkedStack


class NonTerminal(Enum):
    Program             = 0
    Definitions         = 1
    Def                 = 2
    Formals             = 3
    Nonempty_Formals    = 4
    Nonempty_Formals_p  = 5
    Formal              = 6
    Body                = 7
    Statement_List      = 8
    Type                = 9
    Expr                = 10
    Expr_p              = 11
    Simple_Expr         = 12
    Simple_Expr_p       = 13
    Term                = 14
    Term_p              = 15
    Factor              = 16
    Factor_p            = 17
    Actuals             = 18
    Nonempty_Actuals    = 19
    Nonempty_Actuals_p  = 20
    Literal             = 21
    Print_Statement     = 22


class Parser:
    def __init__(self):
        stack = LinkedStack()
        stack.push("$")
        parse_table = {
            (NonTerminal.Program, TokenType.program_keyword)     :   [TokenType.program_keyword,
                                                                      TokenType.identifier,
                                                                      TokenType.left_parenthesis,
                                                                      NonTerminal.Formals,
                                                                      TokenType.right_parenthesis,
                                                                      TokenType.semicolon,
                                                                      NonTerminal.Definitions,
                                                                      NonTerminal.Body,
                                                                      TokenType.period],
            (NonTerminal.Definitions, TokenType.function_keyword):   [NonTerminal.Def,
                                                                      NonTerminal.Definitions],
            (NonTerminal.Definitions, TokenType.begin_keyword)   :   ["ε"],
            (NonTerminal.Def, TokenType.function_keyword)        :   [TokenType.function_keyword,
                                                                      TokenType.identifier,
                                                                      TokenType.left_parenthesis,
                                                                      NonTerminal.Formals,
                                                                      TokenType.right_parenthesis,
                                                                      TokenType.colon,
                                                                      NonTerminal.Type,
                                                                      NonTerminal.Body],
            (NonTerminal.Formals, TokenType.right_parenthesis)   :   ["ε"],
            (NonTerminal.Formals, TokenType.identifier)          :   [NonTerminal.Nonempty_Formals],
            (NonTerminal.Nonempty_Formals, TokenType.right_parenthesis): ["ε"],
            (NonTerminal.Nonempty_Formals, TokenType.identifier) :   [NonTerminal.Formal,
                                                                      NonTerminal.Nonempty_Formals_p],
            (NonTerminal.Nonempty_Formals_p, TokenType.right_parenthesis): ["ε"],
            (NonTerminal.Nonempty_Formals_p, TokenType.comma)    :   [TokenType.comma,
                                                                      NonTerminal.Nonempty_Formals],
            (NonTerminal.Formal, TokenType.identifier)           :   [TokenType.identifier,
                                                                      TokenType.colon,
                                                                      NonTerminal.Type],
            (NonTerminal.Body, TokenType.begin_keyword)          :   [TokenType.begin_keyword,
                                                                      NonTerminal.Statement_List,
                                                                      TokenType.end_keyword],
            (NonTerminal.Statement_List, TokenType.return_keyword):  [TokenType.return_keyword,
                                                                      NonTerminal.Expr],
            (NonTerminal.Statement_List, TokenType.print_statement): [NonTerminal.Print_Statement,
                                                                      NonTerminal.Statement_List],
            (NonTerminal.Type, TokenType.integer_type)           :   [TokenType.integer_type],
            (NonTerminal.Type, TokenType.boolean_type)           :   [TokenType.boolean_type],
            (NonTerminal.Expr, TokenType.left_parenthesis)       :   [NonTerminal.Simple_Expr,
                                                                      NonTerminal.Expr_p],
            (NonTerminal.Expr, TokenType.identifier)             :   [NonTerminal.Simple_Expr,
                                                                      NonTerminal.Expr_p],
            (NonTerminal.Expr, TokenType.minus)                  :   [NonTerminal.Simple_Expr,
                                                                      NonTerminal.Expr_p]
            (NonTerminal.Expr, TokenType.if_statement)           :   [NonTerminal.Simple_Expr,
                                                                      NonTerminal.Expr_p]
            # not done
        }

    def parse(self):
        pass
