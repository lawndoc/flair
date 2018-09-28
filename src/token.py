
from enum import Enum


class TokenType(Enum):
    semicolon = 0
    integer_token = 1       # value
    # v
    program_keyword = 2
    function_keyword = 19
    return_keyword = 20
    begin_keyword = 21
    end_keyword = 22
    # ^
    period = 3
    left_parenthesis = 4
    right_parenthesis = 5
    boolean_token = 6       # value
    # v
    plus = 7
    minus = 28
    times = 29
    divide = 30
    # ^
    # v
    integer_type = 8        # type keyword
    boolean_type = 18       # type keyword
    # ^
    # v
    and_operator = 9
    or_operator = 23
    not_operator = 24
    # ^
    print_statement = 10
    # v
    if_statement = 11
    then_statement = 25
    else_statement = 26
    # ^
    # v
    less_than = 12
    equal_to = 27
    # ^
    comma = 13
    colon = 14
    leftbrace = 15
    rightbrace = 16
    identifier = 17


class Token:
    def __init__(self, token_type, token_value=";"):
        self.token_type = token_type
        self.token_value = token_value

    def isInteger(self):
        return self.token_type == TokenType.integer_token

    def isSemicolon(self):
        return self.token_type == TokenType.semicolon

    def isProgramKeyword(self):
        return self.token_type == TokenType.program_keyword

    def isFunctionKeyword(self):
        return self.token_type == TokenType.function_keyword

    def isReturnKeyword(self):
        return self.token_type == TokenType.return_keyword

    def isBeginKeyword(self):
        return self.token_type == TokenType.begin_keyword

    def isEndKeyword(self):
        return self.token_type == TokenType.end_keyword

    def isPeriod(self):
        return self.token_type == TokenType.period

    def isLeftParen(self):
        return self.token_type == TokenType.left_parenthesis

    def isRightParen(self):
        return self.token_type == TokenType.right_parenthesis

    def isBoolean(self):
        return self.token_type == TokenType.boolean_token

    def isPlus(self):
        return self.token_type == TokenType.plus

    def isMinus(self):
        return self.token_type == TokenType.minus

    def isTimes(self):
        return self.token_type == TokenType.times

    def isDivide(self):
        return self.token_type == TokenType.divide

    def isIntegerType(self):
        return self.token_type == TokenType.integer_type

    def isBooleanType(self):
        return self.token_type == TokenType.boolean_type

    def isAndOperator(self):
        return self.token_type == TokenType.and_operator

    def isOrOperator(self):
        return self.token_type == TokenType.or_operator

    def isNotOperator(self):
        return self.token_type == TokenType.not_operator

    def isPrintStatement(self):
        return self.token_type == TokenType.print_statement

    def isIfStatement(self):
        return self.token_type == TokenType.if_statement

    def isThenStatement(self):
        return self.token_type == TokenType.then_statement

    def isElseStatement(self):
        return self.token_type == TokenType.else_statement

    def isLessThan(self):
        return self.token_type == TokenType.less_than

    def isEqualTo(self):
        return self.token_type == TokenType.equal_to

    def isComma(self):
        return self.token_type == TokenType.comma

    def isColon(self):
        return self.token_type == TokenType.colon

    def isLeftBrace(self):
        return self.token_type == TokenType.leftbrace

    def isRightBrace(self):
        return self.token_type == TokenType.rightbrace

    def isIdentifier(self):
        return self.token_type == TokenType.identifier

    def getValue(self):
        return self.token_value

    def getType(self):
        return self.token_type

    def __repr__(self):
        if self.isInteger():
            return "integer = " + str(self.token_value)
        elif self.isSemicolon():
            return "semicolon"
        elif self.isProgramKeyword():
            return "keyword = " + str(self.token_value)
        elif self.isFunctionKeyword():
            return "keyword = " + str(self.token_value)
        elif self.isReturnKeyword():
            return "keyword = " + str(self.token_value)
        elif self.isBeginKeyword():
            return "keyword = " + str(self.token_value)
        elif self.isEndKeyword():
            return "keyword = " + str(self.token_value)
        elif self.isPeriod():
            return "period"
        elif self.isLeftParen():
            return "left parenthesis"
        elif self.isRightParen():
            return "right parenthesis"
        elif self.isBoolean():
            return "boolean = " + str(self.token_value)
        elif self.isPlus():
            return "arithmetic operator = " + str(self.token_value)
        elif self.isMinus():
            return "arithmetic operator = " + str(self.token_value)
        elif self.isTimes():
            return "arithmetic operator = " + str(self.token_value)
        elif self.isDivide():
            return "arithmetic operator = " + str(self.token_value)
        elif self.isIntegerType():
            return "type = " + str(self.token_value)
        elif self.isBooleanType():
            return "type = " + str(self.token_value)
        elif self.isAndOperator():
            return "boolean operator = " + str(self.token_value)
        elif self.isOrOperator():
            return "boolean operator = " + str(self.token_value)
        elif self.isNotOperator():
            return "boolean operator = " + str(self.token_value)
        elif self.isPrintStatement():
            return "print statement"
        elif self.isIfStatement():
            return "if statement"
        elif self.isThenStatement():
            return "then statement"
        elif self.isElseStatement():
            return "else statement"
        elif self.isLessThan():
            return "comparison = " + str(self.token_value)
        elif self.isEqualTo():
            return "comparison = " + str(self.token_value)
        elif self.isComma():
            return "comma"
        elif self.isColon():
            return "colon"
        elif self.isLeftBrace():
            return "left brace"
        elif self.isRightBrace():
            return "right brace"
        elif self.isIdentifier():
            return "identifier = " + str(self.token_value)
