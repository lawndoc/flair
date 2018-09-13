#!/usr/bin/python3

from enum import Enum
from token import Token, TokenType


class State(Enum):
    looking_state = 1
    zero_state = 2
    integer_state = 3
    comment_state = 4
    pr_state = 5
    print_state = 6
    program_state = 7
    and_state = 8
    f_state = 9
    function_state = 10
    false_state = 11
    e_state = 12
    end_state = 13
    else_state = 14
    b_state = 15
    begin_state = 16
    boolean_state = 17
    t_state = 18
    true_state = 19
    then_state = 20
    identifier_state = 21
    and_state = 22
    return_state = 23
    not_state = 24
    or_state = 25
    i_state = 26
    if_state = 27
    integer_type_state = 28




class Scanner:
    def __init__(self, program=""):
        self.program = program

    def scan(program):
        tokens = []
        accum = ''

        state = State.looking_state
        pos = 0
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
                    tokens.append(Token(TokenType.operator, program[pos]))
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.comparison, program[pos]))
                elif program[pos] == "{":
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                elif program[pos] == '0':
                    state = State.zero_state
                elif program[pos] in '123456789':
                    accum = program[pos]
                    state = State.integer_state
                    raise ValueError(error_msg)
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
                    else:
                        accum += program[pos]
                        state = State.identifier_state
                elif program[pos] == "_":
                    error_msg = "Identifiers must start with a letter, not an '_'"
                    raise ValueError(error_msg)
                else:
                    error_msg = "Not a recognized character : {} ."
                    raise ValueError(error_msg.format(program[pos]))
                pos += 1
            # '0' was read... next character should be a delimiter
            elif state == State.zero_state:
                if program[pos].isdigit():
                    error_msg = "Integers do not have leading zeros : {}"
                    raise ValueError(error_msg.format(program[pos]))
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
                    tokens.append(Token(TokenType.operator, program[pos]))
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.comparison, program[pos]))
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.integer_token, 0))
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise ValueError(error_msg)
                else:
                    error_msg = "Invalid character after a 0: 0{}"
                    raise ValueError(error_msg.format(program[pos]))
                accum = ''
                pos += 1
            # integer detected... read digits until delimiter is found
            elif state == State.integer_state:
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
                    tokens.append(Token(TokenType.operator, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.comparison, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise ValueError(error_msg)
                else:
                    error_msg = "Invalid character in integer : {}*{}*"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1
            # '{' was read... skip over comment until '}' is found
            elif state == State.comment_state:
                if program[pos] == "}":
                    state = State.looking_state
                pos += 1
            # 'i' was read... could be 'if', 'integer', or an identifier
            elif state == State.i_state:
                if program[pos] == 'f':
                    accum += program[pos]
                    state = State.if_state
                elif program[pos] == 'n':
                    accum += program[pos]
                    state = State.integer_state
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
                    tokens.append(Token(TokenType.operator, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    tokens.append(Token(TokenType.comparison, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.identifier, str(accum)))
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise ValueError(error_msg)
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1
            # 'if' has been read... could be 'if' or an identifier
            elif state == State.if_state:
                if program[pos].isspace():
                    tokens.append(Token(TokenType.statement, str(accum)))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    accum = ""
                    state = State.looking_state
                else:
                    accum += program[pos]
                    state = State.identifier_state
                pos += 1
            # 'in' was read... could be 'integer' or an identifier
            elif state == State.integer_state:
                letters = ["r","e","g","e","t"]     # rest of 'integer'
                if program[pos] == letters[-1]:
                    accum += program[pos]
                    if len(letters) == 0:
                        tokens.append(Token(TokenType.type, str(accum)))
                        accum = ""
                        state = State.looking_state
                    else:
                        letters.pop()
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1
            # 'f' was read... could be 'function', 'false', or an identifier
            elif state == State.f_state:
                if program[pos] == 'a':
                    accum += program[pos]
                    state = State.false_state
                elif program[pos] == 'u':
                    accum += program[pos]
                    state = State.function_state
                elif program[pos].isalpha() or program[pos] == '_' or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
            #found an a after the f
            elif state == State.false_state:
                pass # to do



        return tokens
