"""Generic Python Utilities

These are optional utilities .
They are just to make your code better & l-o-c lesser.
"""


def is_empty_string(value: str):
    """returns True if a variable is a empty string
    returns False :
        - if not a string
        - if not empty
    """

    if isinstance(value, str) and len(value) == 0:
        return True


def is_positive_number(value: (int, str), zero=False):
    """returns True if a variable is a positive number
    returns False :
        - if not an integer or string
        - if string is not a integer string
        - if not positive or zero(if True)

    : Note :
    if zero = true :
        checks for whole numbers
    if zero = False
        checks for natural numbers
    use isdigit() in case only a string check required
    """

    check = 0 if zero else 1
    try:
        assert isinstance(value, (int, str))
        assert not isinstance(value, (bool))
        value = int(value)
        assert value >= check
    except ValueError:
        return False
    except AssertionError:
        return False

    return True


def is_number(value: (int, str)):

    try:
        assert isinstance(value, (int, str))
        assert not isinstance(value, (bool))
        value = int(value)
    except ValueError:
        return False

    return True


def is_negative_number(value: (int, str)):
    check = -1
    try:
        assert isinstance(value, (int, str))
        assert not isinstance(value, (bool))
        value = int(value)
        assert value <= check
    except ValueError:
        return False
    except AssertionError:
        return False

    return True


def oint(value: (str, int, bool), default=None):
    """Overloaded int()
    returns `default` value if unable to cast to int
    """
    try:
        value = int(value)
    except ValueError:
        return default

    return value
