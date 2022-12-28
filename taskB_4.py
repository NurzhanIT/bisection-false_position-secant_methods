import false_position_method
import math


def function(x):
    return 2*x-math.log(x)-7


n1 = -9
n2 = 10
decimal = 3

false_position_method.false_position(function, n1, n2, decimal)
