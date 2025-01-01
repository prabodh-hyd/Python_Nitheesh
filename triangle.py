def equilateral(sides):

    return sides[0] == sides[1] == sides[2] and all(side > 0 for side in sides)

def isosceles(sides):

    return (sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]) and is_valid_triangle(sides)

def scalene(sides):

    return sides[0] != sides[1] != sides[2] != sides[0] and is_valid_triangle(sides)

def is_valid_triangle(sides):

    return (
        sides[0] + sides[1] > sides[2] and
        sides[1] + sides[2] > sides[0] and
        sides[2] + sides[0] > sides[1]
    )

