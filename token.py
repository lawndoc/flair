class TokenType(Enum):
    semicolon = 0
    integer = 1
    keyword = 2
    period = 3
    leftparen = 4
    rightparen = 5
    boolean = 6
    operator = 7
    type = 8
    boolean_operator = 9
    print_statement = 10
    statement = 11
    comparison = 12
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
        return self.token_type == TokenType.integer
    def isSemicolon(self):
        return self.token_type == TokenType.semicolon
    def isKeyword(self):
        return self.token_type == TokenType.keyword
    def isPeriod(self):
        return self.token_type == TokenType.period
    def isLeftParen(self):
        return self.token_type == TokenType.leftparen
    def isRightParen(self):
        return self.token_type == TokenType.rightparen
    def isBoolean(self):
        return self.token_type == TokenType.boolean
    def isOperator(self):
        return self.token_type == TokenType.operator
    def isType(self):
        return self.token_type == TokenType.type
    def isBooleanOperator(self):
        return self.token_type == TokenType.boolean_operator
    def isPrintStatement(self):
        return self.token_type == TokenType.print_statement
    def isStatement(self):
        return self.token_type == TokenType.statement
    def isComparison(self):
        return self.token_type == TokenType.comparison
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
    def value(self):
        return self.token_value



    def __repr__(self):
        if self.isInteger():
            return "integer = " + str(self.token_value)
        elif self.isSemicolon():
            return "semicolon"
        elif self.isKeyword():
            return "keyword = " + str(self.token_value)
        elif self.isPeriod():
            return "period"
        elif self.isLeftParen():
            return "left parenthesis"
        elif self.isRightParen():
            return "right parenthesis"
        elif self.isBoolean():
            return "boolean = " + str(self.token_value)
        elif self.isOperator():
            return "operator = " + str(self.token_value)
        elif self.isType():
            return "type = " + str(self.token_value)
        elif self.isBooleanOperator():
            return "boolean operator = " + str(self.token_value)
        elif self.isPrintStatement():
            return "print statement"
        elif self.isStatement():
            return "statement = " + str(self.token_value)
        elif self.isComparison():
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
