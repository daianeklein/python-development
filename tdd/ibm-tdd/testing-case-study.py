from typing import Type


def area_of_a_triangle(base: float, height: float) -> float:
    '''Calculates area of a triangle given non-negative numbers'''
    print("test")

    #check if we have the correct parameters types
    if type(base) not in [int, float]:
        raise TypeError('Base must be a number')
    if type(height) not in [int, float]:
        raise TypeError('Height must be a number')

    #check if we have the correct parameters values
    if base < 0:
        raise ValueError('Base must be a positive number')
    if height < 0:
        raise ValueError('Height must be a positive number')

    return (base / 2) * height
    