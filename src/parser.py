
from sys import path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.linkedStack import LinkedStack

class Parser:
    def __init__(self):
        stack = LinkedStack()
        stack.push("$")
