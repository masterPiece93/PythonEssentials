"""
Let's suppose this is some module `b`
This is the main module which will import all other helper modules
"""
from .a import *
from .c import *
from .c2 import *

__all__ = [ "b",  "CONST_B2", "B"]

CONST_B = "CONSTANT B"
CONST_B2 = "CONSTANT B2"


class B:

    def method_b(self):
        print("method_b")


class B2:

    def method_b(self):
        print("method_b")

def b():
    print("function `b`")

def _b():
    print("private function _b")

_MODULE_C2.c # <--- using module C2
_MODULE_C.c # <--- using module C

print("Module B :\n", dir())
