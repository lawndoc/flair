#!/usr/bin/python3

from enum import Enum
import sys
from token import TokenType
from linkedStack import LinkedStack
from errors import ParseError
import AST

def excepthook(type, value, traceback):
    print(str(value))

sys.excepthook = excepthook


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


parse_table = {
    (NonTerminal.Program, TokenType.program_keyword)     :   [TokenType.program_keyword,
                                                              TokenType.identifier,
                                                              AST.Identifier,
                                                              TokenType.left_parenthesis,
                                                              NonTerminal.Formals,
                                                              TokenType.right_parenthesis,
                                                              TokenType.semicolon,
                                                              NonTerminal.Definitions,
                                                              AST.Definitions,
                                                              NonTerminal.Body,
                                                              TokenType.period,
                                                              AST.Program],
    (NonTerminal.Definitions, TokenType.function_keyword):   [NonTerminal.Def,
                                                              NonTerminal.Definitions],
    (NonTerminal.Definitions, TokenType.begin_keyword)   :   ["ε"],
    (NonTerminal.Def, TokenType.function_keyword)        :   [TokenType.function_keyword,
                                                              TokenType.identifier,
                                                              AST.Identifier,
                                                              TokenType.left_parenthesis,
                                                              NonTerminal.Formals,
                                                              TokenType.right_parenthesis,
                                                              TokenType.colon,
                                                              NonTerminal.Type,
                                                              NonTerminal.Body,
                                                              TokenType.semicolon,
                                                              AST.Function],
    (NonTerminal.Formals, TokenType.right_parenthesis)   :   ["ε"],
    (NonTerminal.Formals, TokenType.identifier)          :   [NonTerminal.Nonempty_Formals,
                                                              AST.Formals],
    (NonTerminal.Nonempty_Formals, TokenType.right_parenthesis): ["ε"],
    (NonTerminal.Nonempty_Formals, TokenType.identifier) :   [NonTerminal.Formal,
                                                              NonTerminal.Nonempty_Formals_p],
    (NonTerminal.Nonempty_Formals_p, TokenType.right_parenthesis): ["ε"],
    (NonTerminal.Nonempty_Formals_p, TokenType.comma)    :   [TokenType.comma,
                                                              NonTerminal.Nonempty_Formals],
    (NonTerminal.Formal, TokenType.identifier)           :   [TokenType.identifier,
                                                              AST.Identifier,
                                                              TokenType.colon,
                                                              NonTerminal.Type,
                                                              AST.Formal],
    (NonTerminal.Body, TokenType.begin_keyword)          :   [TokenType.begin_keyword,
                                                              NonTerminal.Statement_List,
                                                              TokenType.end_keyword,
                                                              AST.Body],
    (NonTerminal.Statement_List, TokenType.return_keyword):  [TokenType.return_keyword,
                                                              NonTerminal.Expr,
                                                              AST.ReturnStatement],
    (NonTerminal.Statement_List, TokenType.print_statement): [NonTerminal.Print_Statement,
                                                              NonTerminal.Statement_List],
    (NonTerminal.Type, TokenType.integer_type)           :   [TokenType.integer_type,
                                                              AST.Type],
    (NonTerminal.Type, TokenType.boolean_type)           :   [TokenType.boolean_type,
                                                              AST.Type],
    (NonTerminal.Expr, TokenType.left_parenthesis)       :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr, TokenType.identifier)             :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr, TokenType.minus)                  :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr, TokenType.if_statement)           :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr, TokenType.not_operator)           :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr, TokenType.integer_token)          :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr, TokenType.boolean_token)          :   [NonTerminal.Simple_Expr,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr_p, TokenType.right_parenthesis)    :   ["ε"],
    (NonTerminal.Expr_p, TokenType.comma)                :   ["ε"],
    (NonTerminal.Expr_p, TokenType.end_keyword)          :   ["ε"],
    (NonTerminal.Expr_p, TokenType.less_than)            :   [TokenType.less_than,
                                                              NonTerminal.Simple_Expr,
                                                              AST.LessThan,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr_p, TokenType.equal_to)             :   [TokenType.equal_to,
                                                              NonTerminal.Simple_Expr,
                                                              AST.EqualTo,
                                                              NonTerminal.Expr_p],
    (NonTerminal.Expr_p, TokenType.or_operator)          :   ["ε"],
    (NonTerminal.Expr_p, TokenType.plus)                 :   ["ε"],
    (NonTerminal.Expr_p, TokenType.minus)                :   ["ε"],
    (NonTerminal.Expr_p, TokenType.and_operator)         :   ["ε"],
    (NonTerminal.Expr_p, TokenType.times)                :   ["ε"],
    (NonTerminal.Expr_p, TokenType.divide)               :   ["ε"],
    (NonTerminal.Expr_p, TokenType.then_statement)       :   ["ε"],
    (NonTerminal.Expr_p, TokenType.else_statement)       :   ["ε"],
    (NonTerminal.Simple_Expr, TokenType.left_parenthesis):   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr, TokenType.identifier)      :   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr, TokenType.minus)           :   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr, TokenType.if_statement)    :   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr, TokenType.not_operator)    :   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr, TokenType.integer_token)   :   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr, TokenType.boolean_token)   :   [NonTerminal.Term,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr_p, TokenType.right_parenthesis): ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.comma)         :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.end_keyword)   :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.less_than)     :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.equal_to)      :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.or_operator)   :   [TokenType.or_operator,
                                                              NonTerminal.Term,
                                                              AST.OrExpr,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr_p, TokenType.plus)          :   [TokenType.plus,
                                                              NonTerminal.Term,
                                                              AST.PlusExpr,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr_p, TokenType.minus)         :   [TokenType.minus,
                                                              NonTerminal.Term,
                                                              AST.MinusExpr,
                                                              NonTerminal.Simple_Expr_p],
    (NonTerminal.Simple_Expr_p, TokenType.and_operator)  :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.times)         :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.divide)        :   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.then_statement):   ["ε"],
    (NonTerminal.Simple_Expr_p, TokenType.else_statement):   ["ε"],
    (NonTerminal.Term, TokenType.left_parenthesis)       :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term, TokenType.identifier)             :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term, TokenType.minus)                  :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term, TokenType.if_statement)           :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term, TokenType.not_operator)           :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term, TokenType.integer_token)          :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term, TokenType.boolean_token)          :   [NonTerminal.Factor,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term_p, TokenType.right_parenthesis)    :   ["ε"],
    (NonTerminal.Term_p, TokenType.comma)                :   ["ε"],
    (NonTerminal.Term_p, TokenType.end_keyword)          :   ["ε"],
    (NonTerminal.Term_p, TokenType.less_than)            :   ["ε"],
    (NonTerminal.Term_p, TokenType.equal_to)             :   ["ε"],
    (NonTerminal.Term_p, TokenType.or_operator)          :   ["ε"],
    (NonTerminal.Term_p, TokenType.plus)                 :   ["ε"],
    (NonTerminal.Term_p, TokenType.minus)                :   ["ε"],
    (NonTerminal.Term_p, TokenType.and_operator)         :   [TokenType.and_operator,
                                                              NonTerminal.Factor,
                                                              AST.AndExpr,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term_p, TokenType.times)                :   [TokenType.times,
                                                              NonTerminal.Factor,
                                                              AST.TimesExpr,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term_p, TokenType.divide)               :   [TokenType.divide,
                                                              NonTerminal.Factor,
                                                              AST.DivideExpr,
                                                              NonTerminal.Term_p],
    (NonTerminal.Term_p, TokenType.then_statement)       :   ["ε"],
    (NonTerminal.Term_p, TokenType.else_statement)       :   ["ε"],
    (NonTerminal.Factor, TokenType.left_parenthesis)     :   [TokenType.left_parenthesis,
                                                              NonTerminal.Expr,
                                                              TokenType.right_parenthesis],
    (NonTerminal.Factor, TokenType.identifier)           :   [TokenType.identifier,
                                                              AST.Identifier,
                                                              NonTerminal.Factor_p],
    (NonTerminal.Factor, TokenType.minus)                :   [TokenType.minus,
                                                              NonTerminal.Factor,
                                                              AST.NegateExpr],
    (NonTerminal.Factor, TokenType.if_statement)         :   [TokenType.if_statement,
                                                              NonTerminal.Expr,
                                                              TokenType.then_statement,
                                                              NonTerminal.Expr,
                                                              TokenType.else_statement,
                                                              NonTerminal.Expr,
                                                              AST.IfStatement],
    (NonTerminal.Factor, TokenType.not_operator)         :   [TokenType.not_operator,
                                                              NonTerminal.Factor,
                                                              AST.NotExpr],
    (NonTerminal.Factor, TokenType.integer_token)        :   [NonTerminal.Literal],
    (NonTerminal.Factor, TokenType.boolean_token)        :   [NonTerminal.Literal],
    (NonTerminal.Factor_p, TokenType.left_parenthesis)   :   [TokenType.left_parenthesis,
                                                              NonTerminal.Actuals,
                                                              TokenType.right_parenthesis,
                                                              AST.FunctionCall],
    (NonTerminal.Factor_p, TokenType.right_parenthesis)  :   ["ε"],
    (NonTerminal.Factor_p, TokenType.comma)              :   ["ε"],
    (NonTerminal.Factor_p, TokenType.end_keyword)        :   ["ε"],
    (NonTerminal.Factor_p, TokenType.less_than)          :   ["ε"],
    (NonTerminal.Factor_p, TokenType.equal_to)           :   ["ε"],
    (NonTerminal.Factor_p, TokenType.or_operator)        :   ["ε"],
    (NonTerminal.Factor_p, TokenType.plus)               :   ["ε"],
    (NonTerminal.Factor_p, TokenType.minus)              :   ["ε"],
    (NonTerminal.Factor_p, TokenType.and_operator)       :   ["ε"],
    (NonTerminal.Factor_p, TokenType.times)              :   ["ε"],
    (NonTerminal.Factor_p, TokenType.divide)             :   ["ε"],
    (NonTerminal.Factor_p, TokenType.then_statement)     :   ["ε"],
    (NonTerminal.Factor_p, TokenType.else_statement)     :   ["ε"],
    (NonTerminal.Actuals, TokenType.left_parenthesis)    :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Actuals, TokenType.right_parenthesis)   :   ["ε"],
    (NonTerminal.Actuals, TokenType.identifier)          :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Actuals, TokenType.minus)               :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Actuals, TokenType.if_statement)        :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Actuals, TokenType.not_operator)        :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Actuals, TokenType.integer_token)       :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Actuals, TokenType.boolean_token)       :   [NonTerminal.Nonempty_Actuals,
                                                              AST.Actuals],
    (NonTerminal.Nonempty_Actuals, TokenType.left_parenthesis): [NonTerminal.Expr,
                                                                 NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals, TokenType.identifier) :   [NonTerminal.Expr,
                                                              NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals, TokenType.minus)      :   [NonTerminal.Expr,
                                                              NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals, TokenType.if_statement):  [NonTerminal.Expr,
                                                              NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals, TokenType.not_operator):  [NonTerminal.Expr,
                                                              NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals, TokenType.integer_token): [NonTerminal.Expr,
                                                              NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals, TokenType.boolean_token): [NonTerminal.Expr,
                                                              NonTerminal.Nonempty_Actuals_p],
    (NonTerminal.Nonempty_Actuals_p, TokenType.right_parenthesis): ["ε"],
    (NonTerminal.Nonempty_Actuals_p, TokenType.comma)    :   [TokenType.comma,
                                                              NonTerminal.Nonempty_Actuals],
    (NonTerminal.Literal, TokenType.integer_token)       :   [TokenType.integer_token,
                                                              AST.IntegerLiteral],
    (NonTerminal.Literal, TokenType.boolean_token)       :   [TokenType.boolean_token,
                                                              AST.BooleanLiteral],
    (NonTerminal.Print_Statement, TokenType.print_statement): [TokenType.print_statement,
                                                               TokenType.left_parenthesis,
                                                               NonTerminal.Expr,
                                                               TokenType.right_parenthesis,
                                                               TokenType.semicolon,
                                                               AST.PrintStatement]
}  # end of parse table

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
            # print("\nParse Stack: [", self.parseStack, "]")
            A = self.parseStack.peek()
            t = self.scanner.peek().getType()
            tVal = self.scanner.peek().getValue()
            # print("A =", A, "t =", t, "(", tVal, ")")
            if isinstance(A, TokenType):
                if A == t:
                    self.last = tVal
                    self.parseStack.pop()
                    self.scanner.next()
                else:
                    error_msg = "Parsing error: Expected {} but found {}"
                    raise ParseError(error_msg.format(A,t))
            elif isinstance(A, NonTerminal):
                if (A,t) in parse_table:
                    # print("PT Rule: '", parse_table[(A,t)], "'")
                    self.parseStack.pop()
                    if "ε" in parse_table[(A,t)]:  # rule is ε, push nothing onto stack
                        continue
                    else:
                        reversedRule = parse_table[(A,t)].copy()
                        reversedRule.reverse()
                        for y in reversedRule:
                            self.parseStack.push(y)
                else:
                    error_msg = "Parsing Error: No transition for {} from {}"
                    raise ParseError(error_msg.format(A,t))
            elif isinstance(A, AST.ASTnode):
                self.semanticStack.push(A(self.last, self.semanticStack))
            else:
                error_msg = "Parsing Error: An unidentified object is on the stack: {}"
                raise ParseError(error_msg.format(A))

        # end of loop, program threw no errors
        if self.scanner.peek() == "EOF":
            return True
        else:
            error_msg = "Parsing Error: Code found after end of program."
            raise ParseError(error_msg)
