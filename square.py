def area(a):
    if type(a) == str:
        return "Error: Length must be an integer >0"

    if type(a) == float:
        return "Error: Length must be an integer >0"

    if a == 0:
        return "Length can't be zero"

    if a < 0:
        return "Error: Length must be an integer >0"
    # Returns the area of the square given its side
    return a * a


def perimeter(a):
    if type(a) == str:
        return "Error: Length must be an integer >0"

    if type(a) == float:
        return "Error: Length must be an integer >0"

    if a == 0:
        return "Length can't be zero"

    if a < 0:
        return "Error: Length must be an integer >0"
    # Returns the perimeter of the square given its side
    return 4 * a
