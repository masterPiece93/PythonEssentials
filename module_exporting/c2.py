"""
Let's suppose this is some module `c2`
This will represent a helper module
This is an upgraded version of module `c`
"""
def export(fname=__file__):
    from pathlib import Path
    fname = Path(fname).stem.upper()
    obj = type(f"_MODULE_{fname}", (object, ), {})
    return obj

_MODULE_C2 = export()
__all__ = ["_MODULE_C2"]

CONST_C = "CONSTANT C"
CONST_C2 = "CONSTANT C2"


class C:

    def method_c(self):
        print("method_c")


class C2:

    def method_c(self):
        print("method_c")

def c():
    print("function `c`")

def _c():
    print("private function _c")

_MODULE_C2.C = C
_MODULE_C2.c = c
_MODULE_C2.CONST_C2 = CONST_C2

print("Module C2 :\n", dir())
