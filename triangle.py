def area(a, h):
    if type(a) == str or type(h) == str:
        return "Error: Length must be an integer >0"

    if type(a) == float or type(h) == float:
        return "Error: Length must be an integer >0"

    if (a == 0) or (h == 0):
        return "Length can't be zero"

    if (a < 0) or (h < 0):
        return "Error: Length must be an integer >0"
    # Returns the area of the triangle given its altitude and a side its drawn to
    return a * h / 2


def perimeter(a, b, c):
    if type(a) == str or type(b) == str or type(c) == str:
        return "Error: Length must be an integer >0"

    if type(a) == float or type(b) == float or type(c) == float:
        return "Error: Length must be an integer >0"

    if (a == 0) or (b == 0) or (c == 0):
        return "Length can't be zero"

    if (a < 0) or (b < 0) or (c < 0):
        return "Error: Length must be an integer >0"
    # Returns the perimeter of the triangle given all of its sides
    return a + b + c
