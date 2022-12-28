import false_position_method
import math


def function(x):
    return math.cos(x) - 3 * x + 1


n1 = -9
n2 = 10
decimal = 4

false_position_method.false_position(function, n1, n2, decimal)
