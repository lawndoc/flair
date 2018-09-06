from enum import Enum


class TokenType(Enum):
    terminator = 0
    int_token = 1
    str_token = 2


class Token:
    def __init__(self, token_type, token_value=";"):
        self.token_type = token_type
        self.token_value = token_value

    def isTerminator(self):
        return self.token_type == TokenType.terminator

    def isInteger(self):
        return self.token_type == TokenType.int_token

    def isString(self):
        return self.token_type == TokenType.str_token

    def value(self):
        return self.token_value

    def __repr__(self):
        if self.isTerminator():
            return 'terminator'
        elif self.isInteger():
            return 'integer = ' + str(self.token_value)
        else:  # isString()
            return 'string = ' + self.token_value
