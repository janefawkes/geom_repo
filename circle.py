import math


def area(r):
    if type(r) == str:
        return "Error: Length must be an integer >0"

    if type(r) == float:
        return "Error: Length must be an integer >0"

    if r == 0:
        return "Length can't be zero"

    if r < 0:
        return "Error: Length must be an integer >0"
    # Returns the area of the circle given its radius
    return math.pi * r * r



def circumference(r):
    if type(r) == str:
        return "Error: Length must be an integer >0"

    if type(r) == float:
        return "Error: Length must be an integer >0"

    if r == 0:
        return "Length can't be zero"

    if r < 0:
        return "Error: Length must be an integer >0"
    # Returns the circumference of the circle given its radius
    return 2 * math.pi * r