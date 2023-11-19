def area(a, b):
    if type(a) == str or type(b) == str:
        return "Error: Length must be an integer >0"

    if type(a) == float or type(b) == float:
        return "Error: Length must be an integer >0"

    if (a == 0) or (b == 0):
        return "Length can't be zero"

    if (a < 0) or (b < 0):
        return "Error: Length must be an integer >0"
    # Returns the area of the rectangle given two of its sides (vertical and horizontal)
    return a * b


def perimeter(a, b):
    if type(a) == str or type(b) == str:
        return "Error: Length must be an integer >0"

    if type(a) == float or type(b) == float:
        return "Error: Length must be an integer >0"

    if (a == 0) or (b == 0):
        return "Length can't be zero"

    if (a < 0) or (b < 0):
        return "Error: Length must be an integer >0"
    # Returns the perimeter of the rectangle given two of its sides (vertical and horizontal)
    return (a + b) * 2
