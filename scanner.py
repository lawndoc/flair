#!/usr/bin/python3

from enum import Enum
from token import Token, TokenType

class State(Enum):
    looking = 1
    zero = 2
    integer_state = 3
    string_state = 4
    comment = 5
    pr_state = 6
    print_state = 7
    program_state = 8
    and_state = 9
    f_state = 10
    function_state = 11
    false_state = 12
    e_state = 13
    end_state = 14
    else_state = 15
    b_state = 16
    begin_state = 17
    boolean_state = 18
    t_state = 19
    true_state = 20
    then_state = 21
    identifier_state = 22
    and_state = 23
    return_state = 24
    not_state = 25
    or_state = 26
    i_state = 27
    if_state = 28
    integer_type_state = 29




class Scanner:
    def __init__(self, program=""):
        self.program = program

    def scan(program):
        tokens = []
        accum = ''

        state = State.looking
        pos = 0
        while pos < len(program):
            if state == State.looking:
                if program[pos].isspace():
                    continue
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
                    state = State.comment
                elif program[pos] == "}":
                    error_msg = "Unmatched right bracket : '}''"
                elif program[pos] in '0':
                    state = State.zero
                elif program[pos] in '123456789':
                    accum = program[pos]
                    state = State.integer_state
                    raise ValueError(error_msg)
                elif program[pos].isalpha():
                    accum = program[pos]
                    state = State.string_state
                elif program[pos] == "_":
                    error_msg = "Identifiers must start with a letter, not an '_'"
                    raise ValueError(error_msg)
                else:
                    error_msg = "Not a recognized character : {} ."
                    raise ValueError(error_msg.format(program[pos]))
                pos += 1
            elif state == State.zero:
                if program[pos].isspace():
                    tokens.append(Token(TokenType.integer_token, 0))
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.terminator))
                elif program[pos].isdigit():
                    error_msg = "Integers do not have leading zeros : {}"
                    raise ValueError(error_msg.format(program[pos]))
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    state = State.looking
                elif program[pos] == ".":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.period, "."))
                    state = State.looking
                elif program[pos] == ",":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.comma, ","))
                    state = State.looking
                elif program[pos] == ":":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.colon, ":"))
                    state = State.looking
                elif program[pos] == "(":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.left_parenthesis, "("))
                    state = State.looking
                elif program[pos] == ")":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.right_parenthesis, ")"))
                    state = State.looking
                elif program[pos] in "+-*/":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.operator, program[pos]))
                    state = State.looking
                elif program[pos] in "<=":
                    tokens.append(Token(TokenType.integer_token, 0))
                    tokens.append(Token(TokenType.comparison, program[pos]))
                    state = State.looking
                elif program[pos] == "{":
                    tokens.append(Token(TokenType.integer_token, 0))
                    state = State.comment
                elif program[pos] == "}":
                    error_msg = "Unmatched right bracket : '}''"
                else:
                    error_msg = "Invalid character after a 0: 0{}"
                    raise ValueError(error_msg.format(program[pos]))
                accum = ''
                state = State.looking
                pos += 1
            elif state == State.integer_state:
                if program[pos].isdigit():
                    accum += program[pos]
                elif program[pos].isspace():
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    accum = ''
                    state = State.looking
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.integer_token, int(accum)))
                    tokens.append(Token(TokenType.terminator))
                else:
                    error_msg = "Invalid character in integer {}*{}*"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1
            elif state == State.string_state:
                if program[pos].isspace():
                    tokens.append(Token(TokeyType.identifier, accum))
                elif program[pos] ==';':
                    pass
                elif program[pos] == 'i':
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
                    state = State.p
                else:
                    accum += program[pos]
                    state = State.identifier_state
                pos += 1
            elif state == State.comment:
                if program[pos] != "}":
                    continue
                state = State.looking
            #found an i
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
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1
            # f followed the i
            elif state == State.if_state:
                if program[pos].isspace():
                    tokens.append(Token(TokenType.statement, str(accum)))
                    accum = ""
                    state = State.looking
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.statement, str(accum)))
                    tokens.append(Token(TokenType.semicolon, ";"))
                    accum = ""
                    state = State.looking
                else:
                    accum += program[pos]
                    state = State.identifier_state
                pos += 1
            elif state == State.integer_state:
                letters = ["r","e","g","e","t"] # we got here because an 'n' was already read
                if program[pos] == letters[-1]: # if next letter is what it's supposed to be
                    accum += program[pos]
                    if len(letters) == 0:
                        tokens.append(Token(TokenType.type, str(accum)))
                        accum = ""
                        state = State.looking
                    else:
                        letters.pop() # get rid of letter just read so we know what is supposed to be next
                elif program[pos].isalpha() or program[pos] == "_" or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier
                else:
                    error_msg = "Illegal character in identifer {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
                pos += 1
            #found an f
            elif state == State.f_state:
                if program[pos] == 'a':
                    accum += program[pos]
                    state = State.false_state
                elif program[pos] == 'u':
                    accum += program[pos]
                    state = State.function_state
                elif program[pos].isalpha() or program[pos] == '_' or program[pos].isdigit():
                    accum += program[pos]
                    state = State.identifier
                else:
                    error_msg = "Illegal character in identifier {} : {}"
                    raise ValueError(error_msg.format(accum, program[pos]))
            #found an a after the f
            elif state == State.false_state
