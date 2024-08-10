from PyQt5 import QtWidgets


def isfloat(num) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


# TODO: if condition not met, tell user invalid input and clear line edit
def isNumFloat(input: str) -> bool:
    if not (input.isnumeric() or isfloat(input)):
        return False
    return True
