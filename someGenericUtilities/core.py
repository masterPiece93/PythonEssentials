from datetime import date
from dataclasses import dataclass, astuple

class DateRange:
    EXC = {
        "NOT_DATE_TYPE": lambda parameter: Exception(
            f"{parameter} type should be {date}"
        ),
        "START_BEFORE_END": Exception("start value should be before end"),
    }

    def __init__(self, start: date, end: date):
        if not isinstance(start, date):
            raise self.EXC["NOT_DATE_TYPE"](f"start")
        if not isinstance(end, date):
            raise self.EXC["NOT_DATE_TYPE"](f"end")
        self.start: date = start
        self.end: date = end
        self.validate()

    def validate(self):
        if not self.start <= self.end:
            raise self.EXC["START_BEFORE_END"]

    def __eq__(self, other):

        if self.end < other.start or self.start > other.end:
            return False
        return True

    def __str__(self):
        _format = "%d %b %Y"
        return str([self.start.strftime(_format), self.end.strftime(_format)])

@dataclass(frozen=True)
class Query:
    """
    Representation of a SQL Query in two components -
    - sql : textual sql part
    - params : params that bind with the placeholders in SQL
    """
    sql: str
    params: dict
    __iter__ = lambda self: iter(astuple(self))

def default_class(attr_name):
    def class_init(self,param):
        setattr(self,attr_name,param)
    return type("Default",(object,),{'__init__':class_init})
