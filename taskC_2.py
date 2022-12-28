import false_position_method
import math

def function(x):
    return pow(x, 10)-1


n1 = 0
n2 = 10
decimal = 3

false_position_method.false_position(function, n1, n2, decimal)
