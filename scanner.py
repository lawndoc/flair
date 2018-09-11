#!/usr/bin/python3

from enum import Enum
from token import *

class State(Enum):
    looking = 1
    zero = 2
    integer = 3
    identifier = 4
    self_delimeted = 5
    keyword = 6
    boolean = 7
    type = 8
    boolean_operator = 9
    print_statement = 10
    statement = 11

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
                    pass
                elif program[pos] == ';':
                    tokens.append(Token(TokenType.semicolon))
                elif program[position] in '0':
                    accum = program[pos]
                    state = State.zero
                elif program[pos] in '123456789':
                    accum = program[pos]
                    state = State.integer
            elif state == State.zero:
                pass
            elif state == State.integer:
                pass
            elif state == State.identifier:
                pass
            elif state == State.self_delimeted:
                pass
            elif state == State.keyword:
                pass
            elif state == State.boolean:
                pass
            elif state == State.type:
                pass
            elif state == State.boolean_operator:
                pass
            elif state == State.print_statement:
                pass
            elif state == State.statement:
                pass
