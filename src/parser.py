
from sys import path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.linkedStack import LinkedStack

class NonTerminal(Enum):
    Program     = 0
    

class Parser:
    def __init__(self):
        stack = LinkedStack()
        stack.push("$")
