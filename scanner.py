#!/usr/bin/python3

from enum import Enum
from token import Token, TokenType


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
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.period, "."))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.comma, ","))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.colon, ":"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.operator, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.comparison, program[pos]))
                    accum = ""
                    state = State.looking_state
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.statement, str(accum)))
                    state = State.comment_state
                elif program[pos] == "}":
                    error_msg = "Unmatched end of comment character : '}'"
                    raise ValueError(error_msg)
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1

            # 'in' was read... could be 'integer' or an identifier
            elif state == State.integer_type_state:
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

            # 'f' was read... could be 'false', 'function', or an identifier
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

            # "fa" has been read... could be 'false' or an identifier
            elif state == State.false_state:
                letters = ["e","s","l"]     # rest of 'false'
                if program[pos] == letters[-1]:
                    accum += program[pos]
                    if len(letters) == 0:
                        tokens.append(Token(TokenType.boolean_operator, str(accum)))
                        accum = ""
                        state = State.looking_state
                    else:
                        letters.pop()
                elif program[pos].isalpha() or program[pos] == '_' or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier_state
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))

            # 'fu' has been read... could be 'function' or an identifier
            elif state == State.function_state:
                letters = ["n","o","i","t","c","n"]     # rest of 'function'
                pass # to do

            # 'p' has been read... could be 'print', 'program', or an identifier
            elif state == State.pr_state:
                letters = ["r"]     # rest of 'pr...'
                pass # to do

            # 'pri' has been read... could be 'print' or an identifier
            elif state == State.print_state:
                letters = ["t","n"]     # rest of 'print'
                pass # to do

            # 'pro' has been read... could be 'program' or an identifier
            elif state == State.program_state:
                letters = ["m","a","r","g"]     # rest of 'program'
                pass # to do

            # 'e' has been read... could be 'end', 'else', or an identifier
            elif state == State.e_state:
                pass # to do

            # 'en' has been read... could be 'end' or an identifier
            elif state == State.end_state:
                letters = ["d"]     # rest of 'end'
                pass # to do

            # 'el' has been read... could be 'else' or an identifier
            elif state == State.else_state:
                letters = ["e","s"]     # rest of 'else'
                pass # to do

            # 'b' has been read... could be 'begin', 'boolean', or an identifier
            elif state == State.b_state:
                pass # to do

            # 'be' has been read... could be 'begin' or an identifier
            elif state == State.begin_state:
                letters = ["n","i","g"]     # rest of 'begin'
                pass # to do

            # 'bo' has been read... could be 'boolean' or an identifier
            elif state == State.boolean_state:
                letters = ["n","a","e","l","o"]     # rest of 'boolean'
                pass # to do

            # 't' has been read... could be 'true', 'then', or an identifier
            elif state == State.t_state:
                pass # to do

            # 'tr' has been read... could be 'true' or an identifier
            elif state == State.true_state:
                letters = ["e","u"]     # rest of 'true'
                pass # to do

            # 'th' has been read... could be 'then' or an identifier
            elif state == State.then_state:
                letters = ["n","e"]     # rest of 'then'
                pass # to do

            # 'a' has been read... could be 'and' or an identifier
            elif state == State.and_state:
                letters = ["d","n"]     # rest of 'and'
                pass # to do

            # 'o' has been read... could be 'or' or an identifier
            elif state == State.or_state:
                letters = ["r"]     # rest of 'or'
                pass # to do

            # 'r' has been read... could be 'return' or an identifier
            elif state == State.return_state:
                letters = ["n","r","u","t","e"]     # rest of 'return'
                pass # to do

            # 'n' has been read... could be 'not' or an identifier
            elif state == State.not_state:
                letters = ["t","o"]     # rest of 'not'
                pass # to do

            # identifier detected... read alphabetical characters, digits, and '_' until a delimiter is found
            elif state == State.identifier_state:
                pass # to do


        # end of program... return list of tokens
        return tokens
