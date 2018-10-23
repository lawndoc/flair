#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.errors import *
from src import AST

class Analyzer:
    def __init__(self, ast):
        self.ast = ast
        self.ast.annotate()

#whats the plan

# I think we should make a function first that annotates the AST with types and then call it in the __init__
# kind of like that day in class when he talked about annotating the tree . fun
# this one is probably gonna be less cut and paste and more thinking =/
# alright so first we have a program node which should have a body, defs,
# formals and an identifier. We only need to look into formals, defs, and body
# I think we're gonna need some kind of loop and then if checks to handle
# different types of nodes. sounds good. I'll play around with some stuff
# and may not keep all of it but I'll try to layout what I was thinking just now.
# I think we also need to modify each AST node to be able to hold and set
# a self.type variable. Do you wanna add that to those? basically we just need
# it declared in __init__ and then set with a setType method and we also need
# a getType method for each AST node class.
# i'm putting the AST class next to this so I can see both

    def analyze(self):
        pass
