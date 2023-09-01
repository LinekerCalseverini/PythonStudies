import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def convertToNumber(string: str):
    if not isValidNumber(string):
        return 0

    number = -float(string)

    if number.is_integer():
        number = int(number)

    return number


def isValidNumber(string: str):
    try:
        float(string)
        return True
    except ValueError:
        ...

    return False


def isEmpty(string: str):
    return len(string) == 0
