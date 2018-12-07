#!/usr/bin/python3

from enum import Enum
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.errors import LexicalError
from src.token import Token, TokenType

def excepthook(type, value, traceback):
    print(str(value))

sys.excepthook = excepthook

class State(Enum):
    looking_state = 1
    zero_state = 2
    integer_state = 3
    comment_state = 4
    i_state = 5
    if_state = 6
    integer_type_state = 7
    f_state = 8
    false_state = 9
    function_state = 10
    pr_state = 11
    print_state = 12
    program_state = 13
    e_state = 14
    end_state = 15
    else_state = 16
    b_state = 17
    begin_state = 18
    boolean_state = 19
    t_state = 20
    true_state = 21
    then_state = 22
    and_state = 23
    or_state = 24
    return_state = 25
    not_state = 26
    identifier_state = 27


class Scanner:
    def __init__(self, program=""):
        self.program = program
        self.tokens = self.scan()
        self.tokenIndex = 0

    def next(self):
        if self.tokenIndex < len(self.tokens):
            self.tokenIndex += 1
        else:
            return "EOF"
        return self.tokens[self.tokenIndex-1]

    def peek(self):
        if self.tokenIndex >= len(self.tokens):
            return "EOF"
        return self.tokens[self.tokenIndex]

    def replaceNext(self, new):
        if self.tokenIndex >= len(self.tokens):
            pass
        else:
            self.tokens[self.tokenIndex] = new

    def scan(self):
        program = self.program
        tokens = []
        accum = ''

        state = State.looking_state
        pos = 0

        # rest of letters for keyword states
        integer_ltrs = ["r", "e", "g", "e", "t"]
        false_ltrs = ["e", "s", "l"]
        function_ltrs = ["n", "o", "i", "t", "c", "n"]
        print_ltrs = ["t", "n"]
        program_ltrs = ["m", "a", "r", "g"]
        end_ltrs = ["d"]
        else_ltrs = ["e", "s"]
        begin_ltrs = ["n", "i", "g"]
        boolean_ltrs = ["n", "a", "e", "l", "o"]
        true_ltrs = ["e", "u"]
        then_ltrs = ["n", "e"]
        and_ltrs = ["d", "n"]
        or_ltrs = ["r"]
        return_ltrs = ["n", "r", "u", "t", "e"]
        not_ltrs = ["t", "o"]

        while pos < len(program):
            # beginning of program or identifying new token after a delimiter
            if state == State.looking_state:
                if program[pos].isspace():
                    pass
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.semicolon, ";"))
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.period, "."))
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.comma, ","))
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.colon, ":"))
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                elif program[pos] in "+-*/":
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                elif program[pos] in "<=":
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                elif program[pos] == "{":
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                elif program[pos] == '0':
                    state = State.zero_state
                elif program[pos] in '123456789':
                    accum = program[pos]
                    state = State.integer_state
                elif program[pos].isalpha():
                    if program[pos] == 'i':
                        accum += program[pos]
                        state = State.i_state
                    elif program[pos] == 'f':
                        accum += program[pos]
                        state = State.f_state
                    elif program[pos] == 'a':
                        accum += program[pos]
                        state = State.and_state
                    elif program[pos] == 'r':
                        accum += program[pos]
                        state = State.return_state
                    elif program[pos] == 'e':
                        accum += program[pos]
                        state = State.e_state
                    elif program[pos] == 'b':
                        accum += program[pos]
                        state = State.b_state
                    elif program[pos] == 't':
                        accum += program[pos]
                        state = State.t_state
                    elif program[pos] == 'n':
                        accum += program[pos]
                        state = State.not_state
                    elif program[pos] == 'p':
                        accum += program[pos]
                        state = State.pr_state
                    elif program[pos] == "o":
                        accum += program [pos]
                        state = State.or_state
                    else:
                        accum += program[pos]
                        state = State.identifier_state
                elif program[pos] == "_":
                    error_msg = "Identifiers must start with a letter, not an '_'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Not a recognized character : {} ."
                    raise LexicalError(error_msg.format(program[pos]))
                pos += 1

            # '0' was read... next character should be a delimiter
            elif state == State.zero_state:
                if program[pos].isdigit():
                    error_msg = "Integers do not have leading zeros : {}"
                    raise LexicalError(error_msg.format(program[pos]))
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.integer_token, 0))
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.period, "."))
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.comma, ","))
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.colon, ":"))
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.integer_token, 0))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.integer_token, 0))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.integer_token, 0))
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Invalid character after a 0: 0{}"
                    raise LexicalError(error_msg.format(program[pos]))
                accum = ''
                pos += 1

            # integer detected... read digits until delimiter is found
            elif state == State.integer_state:
                if int(accum) >= 2**31 and not tokens[-1].isMinus():
                    error_msg = "Integer beginning with {}... is too large"
                    raise LexicalError(error_msg.format(accum))
                elif int(accum) > 2**31 and tokens[-1].isMinus():
                    error_msg = "Integer beginning with -{}... is too small"
                    raise LexicalError(error_msg.format(accum))
                if program[pos].isdigit():
                    accum += program[pos]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Invalid character in integer : {}*{}*"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # '{' was read... skip over comment until '}' is found
            elif state == State.comment_state:
                if program[pos] == "}":
                    state = State.looking_state
                elif program[pos] == "EOF":
                    error_msg = "Unclosed comment at end of file."
                    raise LexicalError(error_msg)
                pos += 1

            # 'i' was read... could be 'if', 'integer', or an identifier
            elif state == State.i_state:
                if program[pos] == 'f':
                    accum += program[pos]
                    state = State.if_state
                elif program[pos] == 'n':
                    accum += program[pos]
                    state = State.integer_type_state
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'if' has been read... could be 'if' or an identifier
            elif state == State.if_state:
                if program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.if_statement, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'in' was read... could be 'integer' or an identifier
            elif state == State.integer_type_state:
                # rest of 'integer' in integer_ltrs
                if integer_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.integer_type, str(accum)))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                    continue
                elif program[pos] == integer_ltrs[-1]:
                    accum += program[pos]
                    integer_ltrs.pop()
                    if len(integer_ltrs) == 0:      # push '$' if empty list
                        integer_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    integer_ltrs = ["r", "e", "g", "e", "t"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'f' was read... could be 'false', 'function', or an identifier
            elif state == State.f_state:
                if program[pos] == 'a':
                    accum += program[pos]
                    state = State.false_state
                elif program[pos] == 'u':
                    accum += program[pos]
                    state = State.function_state
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # "fa" has been read... could be 'false' or an identifier
            elif state == State.false_state:
                # rest of 'false' in false_ltrs
                if false_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.boolean_token, str(accum)))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                    continue
                elif program[pos] == false_ltrs[-1]:
                    accum += program[pos]
                    false_ltrs.pop()
                    if len(false_ltrs) == 0:      # push '$' if empty list
                        false_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    false_ltrs = ["e", "s", "l"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'fu' has been read... could be 'function' or an identifier
            elif state == State.function_state:
                # rest of 'function' in function_ltrs
                if function_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.function_keyword, str(accum)))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                    continue
                elif program[pos] == function_ltrs[-1]:
                    accum += program[pos]
                    function_ltrs.pop()
                    if len(function_ltrs) == 0:      # push '$' if empty list
                        function_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    function_ltrs = ["n", "o", "i", "t", "c", "n"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'p' or 'pr' has been read... could be 'print', 'program', or an identifier
            elif state == State.pr_state:   # technically a combined state ('p'+'pr')
                if accum == "p":    # 'p' has been read... looking for 'r'
                    if program[pos] == "r":
                        accum += program[pos]
                    elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                        accum += program[pos]
                        state = State.identifier_state
                    elif program[pos].isspace():
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ';':
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.semicolon, ';'))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ".":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.period, "."))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ",":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.comma, ","))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ":":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.colon, ":"))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == "(":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.left_parenthesis, "("))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ")":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.right_parenthesis, ")"))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] in "+-*/":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        if program[pos] == "+":
                            tokens.append(Token(TokenType.plus, program[pos]))
                        elif program[pos] == "-":
                            tokens.append(Token(TokenType.minus, program[pos]))
                        elif program[pos] == "*":
                            tokens.append(Token(TokenType.times, program[pos]))
                        else:
                            tokens.append(Token(TokenType.divide, program[pos]))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] in "<=":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        if program[pos] == "<":
                            tokens.append(Token(TokenType.less_than, program[pos]))
                        else:
                            tokens.append(Token(TokenType.equal_to, program[pos]))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == "{":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        accum = ""
                        state = State.comment_state
                    elif program[pos] == "}":
                        error_msg = "Unmatched end of comment character : '}'"
                        raise LexicalError(error_msg)
                    else:
                        error_msg = "Illegal character in identifier {} : {}"
                        raise LexicalError(error_msg.format(accum, program[pos]))
                elif accum == "pr":     # 'pr' has been read... looking for 'i' or 'o'
                    if program[pos] == 'i':
                        accum += program[pos]
                        state = State.print_state
                    elif program[pos] == 'o':
                        accum += program[pos]
                        state = State.program_state
                    elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                        accum += program[pos]
                        state = State.identifier_state
                    elif program[pos].isspace():
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ';':
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.semicolon, ';'))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ".":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.period, "."))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ",":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.comma, ","))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ":":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.colon, ":"))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == "(":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.left_parenthesis, "("))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == ")":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        tokens.append(Token(TokenType.right_parenthesis, ")"))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] in "+-*/":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        if program[pos] == "+":
                            tokens.append(Token(TokenType.plus, program[pos]))
                        elif program[pos] == "-":
                            tokens.append(Token(TokenType.minus, program[pos]))
                        elif program[pos] == "*":
                            tokens.append(Token(TokenType.times, program[pos]))
                        else:
                            tokens.append(Token(TokenType.divide, program[pos]))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] in "<=":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        if program[pos] == "<":
                            tokens.append(Token(TokenType.less_than, program[pos]))
                        else:
                            tokens.append(Token(TokenType.equal_to, program[pos]))
                        accum = ""
                        state = State.looking_state
                    elif program[pos] == "{":
                        tokens.append(Token(TokenType.identifier, str(accum)))
                        accum = ""
                        state = State.comment_state
                    elif program[pos] == "}":
                        error_msg = "Unmatched end of comment character : '}'"
                        raise LexicalError(error_msg)
                    else:
                        error_msg = "Illegal character in identifier {} : {}"
                        raise LexicalError(error_msg.format(accum, program[pos]))
                else:
                    error_msg = "{} has been read, but scanner stuck in 'pr' state."
                    raise LexicalError(error_msg.format(accum))
                pos += 1

            # 'pri' has been read... could be 'print' or an identifier
            elif state == State.print_state:
                # rest of 'print' in print_ltrs
                if print_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.print_statement, str(accum)))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                    continue
                elif program[pos] == print_ltrs[-1]:
                    accum += program[pos]
                    print_ltrs.pop()
                    if len(print_ltrs) == 0:      # push '$' if empty list
                        print_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    print_ltrs = ["t", "n"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    print_ltrs = ["t", "n"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'pro' has been read... could be 'program' or an identifier
            elif state == State.program_state:
                # rest of 'program' in program_ltrs
                if program_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.program_keyword, str(accum)))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                    continue
                elif program[pos] == program_ltrs[-1]:
                    accum += program[pos]
                    program_ltrs.pop()
                    if len(program_ltrs) == 0:      # push '$' if empty list
                        program_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    program_ltrs = ["m", "a", "r", "g"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'e' has been read... could be 'end', 'else', or an identifier
            elif state == State.e_state:
                if program[pos] == 'n':
                    accum += program[pos]
                    state = State.end_state
                elif program[pos] == 'l':
                    accum += program[pos]
                    state = State.else_state
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'en' has been read... could be 'end' or an identifier
            elif state == State.end_state:
                # rest of 'end' in end_ltrs
                if end_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.end_keyword, str(accum)))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                    continue
                elif program[pos] == end_ltrs[-1]:
                    accum += program[pos]
                    end_ltrs.pop()
                    if len(end_ltrs) == 0:      # push '$' if empty list
                        end_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    end_ltrs = ["d"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    end_ltrs = ["d"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    end_ltrs = ["d"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'el' has been read... could be 'else' or an identifier
            elif state == State.else_state:
                # rest of 'else' in else_ltrs
                if else_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.else_statement, str(accum)))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                    continue
                elif program[pos] == else_ltrs[-1]:
                    accum += program[pos]
                    else_ltrs.pop()
                    if len(else_ltrs) == 0:      # push '$' if empty list
                        else_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    else_ltrs = ["e", "s"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    else_ltrs = ["e", "s"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'b' has been read... could be 'begin', 'boolean', or an identifier
            elif state == State.b_state:
                if program[pos] == 'e':
                    accum += program[pos]
                    state = State.begin_state
                elif program[pos] == 'o':
                    accum += program[pos]
                    state = State.boolean_state
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'be' has been read... could be 'begin' or an identifier
            elif state == State.begin_state:
                # rest of 'begin' in begin_ltrs
                if begin_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.begin_keyword, str(accum)))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                    continue
                elif program[pos] == begin_ltrs[-1]:
                    accum += program[pos]
                    begin_ltrs.pop()
                    if len(begin_ltrs) == 0:      # push '$' if empty list
                        begin_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    begin_ltrs = ["n", "i", "g"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'bo' has been read... could be 'boolean' or an identifier
            elif state == State.boolean_state:
                # rest of 'boolean' in boolean_ltrs
                if boolean_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.boolean_type, str(accum)))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                    continue
                elif program[pos] == boolean_ltrs[-1]:
                    accum += program[pos]
                    boolean_ltrs.pop()
                    if len(boolean_ltrs) == 0:      # push '$' if empty list
                        boolean_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    boolean_ltrs = ["n", "a", "e", "l", "o"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 't' has been read... could be 'true', 'then', or an identifier
            elif state == State.t_state:
                if program[pos] == 'r':
                    accum += program[pos]
                    state = State.true_state
                elif program[pos] == 'h':
                    accum += program[pos]
                    state = State.then_state
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'tr' has been read... could be 'true' or an identifier
            elif state == State.true_state:
                # rest of 'true' in true_ltrs
                if true_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.boolean_token, str(accum)))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                    continue
                elif program[pos] == true_ltrs[-1]:
                    accum += program[pos]
                    true_ltrs.pop()
                    if len(true_ltrs) == 0:      # push '$' if empty list
                        true_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    true_ltrs = ["e", "u"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    true_ltrs = ["e", "u"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'th' has been read... could be 'then' or an identifier
            elif state == State.then_state:
                # rest of 'then' in then_ltrs
                if then_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.then_statement, str(accum)))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                    continue
                elif program[pos] == then_ltrs[-1]:
                    accum += program[pos]
                    then_ltrs.pop()
                    if len(then_ltrs) == 0:      # push '$' if empty list
                        then_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    then_ltrs = ["n", "e"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    then_ltrs = ["n", "e"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'a' has been read... could be 'and' or an identifier
            elif state == State.and_state:
                # rest of 'and' in and_ltrs
                if and_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.and_operator, str(accum)))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                    continue
                elif program[pos] == and_ltrs[-1]:
                    accum += program[pos]
                    and_ltrs.pop()
                    if len(and_ltrs) == 0:      # push '$' if empty list
                        and_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    and_ltrs = ["d", "n"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    and_ltrs = ["d", "n"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'o' has been read... could be 'or' or an identifier
            elif state == State.or_state:
                # rest of 'or' in or_ltrs
                if or_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.or_operator, str(accum)))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                    continue
                elif program[pos] == or_ltrs[-1]:
                    accum += program[pos]
                    or_ltrs.pop()
                    if len(or_ltrs) == 0:      # push '$' if empty list
                        or_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    or_ltrs = ["r"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    or_ltrs = ["r"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    or_ltrs = ["r"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'r' has been read... could be 'return' or an identifier
            elif state == State.return_state:
                # rest of 'return' in return_ltrs
                if return_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.return_keyword, str(accum)))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                    continue
                elif program[pos] == return_ltrs[-1]:
                    accum += program[pos]
                    return_ltrs.pop()
                    if len(return_ltrs) == 0:      # push '$' if empty list
                        return_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    return_ltrs = ["n", "r", "u", "t", "e"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'n' has been read... could be 'not' or an identifier
            elif state == State.not_state:
                # rest of 'not' in not_ltrs
                if not_ltrs[-1] == "$" and not program[pos].isalpha() and program[pos] != "_" and not program[pos].isdigit():
                    tokens.append(Token(TokenType.not_operator, str(accum)))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                    continue
                elif program[pos] == not_ltrs[-1]:
                    accum += program[pos]
                    not_ltrs.pop()
                    if len(not_ltrs) == 0:      # push '$' if empty list
                        not_ltrs.append("$")
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                    not_ltrs = ["t", "o"]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                    not_ltrs = ["t", "o"]
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

            # identifier detected... read alphabetical characters, digits, and '_' until a delimiter is found
            elif state == State.identifier_state:
                if len(accum) > 256:
                    error_msg = "Identifier name {} too long"
                    raise LexicalError(error_msg.format(accum))
                if program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ';'))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "+":
                        tokens.append(Token(TokenType.plus, program[pos]))
                    elif program[pos] == "-":
                        tokens.append(Token(TokenType.minus, program[pos]))
                    elif program[pos] == "*":
                        tokens.append(Token(TokenType.times, program[pos]))
                    else:
                        tokens.append(Token(TokenType.divide, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    if program[pos] == "<":
                        tokens.append(Token(TokenType.less_than, program[pos]))
                    else:
                        tokens.append(Token(TokenType.equal_to, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    accum = ""
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise LexicalError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise LexicalError(error_msg.format(accum, program[pos]))
                pos += 1

        # end of program... return list of tokens
        return tokens
