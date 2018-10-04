#!/usr/bin/python3
# errors thrown by the scanner
class LexicalError(ValueError):
    def __str__(self):
        return "Lexical Error: " + ValueError

# errors thrown by the parser
class ParseError(ValueError):
    def __str__(self):
        return "Parse Error: " + ValueError

# errors thrown by the type checker
class SemanticError(ValueError):
    def __str__(self):
        return "Semantic Error: " + ValueError
