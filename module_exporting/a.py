"""
Let's suppose this is some module `a`
This will represent a helper module
"""
__all__ = [ "a",  "CONST_A2", "A"]

CONST_A = "CONSTANT A"
CONST_A2 = "CONSTANT A2"


class A:

    def method_a(self):
        print("method_a")


class A2:

    def method_a(self):
        print("method_a")

def a():
    print("function `a`")

def _a():
    print("private function _a")


print("Module A :\n", dir())