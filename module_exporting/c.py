"""
Let's suppose this is some module `c`
This will represent a helper module
"""
__all__ = []

def export(fn,fname,v):
    from pathlib import Path
    fname = Path(fname).stem.upper()
    obj = type(f"_MODULE_{fname}", (object, ), {})
    fn[f"_MODULE_{fname}"]=obj
    if isinstance(v, list):
        v.append(f"_MODULE_{fname}")
    else:
        raise Exception(f"__all__ must be declared of type {list}")
    return obj

_export=export(globals(), __file__, __all__)

CONST_C = "CONSTANT C"
CONST_D = "CONSTANT D"


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

_export.C = C
_export.c = c
_export.CONST_D = CONST_D

print("Module C :\n", dir())