def secant(function, n1, n2, lim):
    result = 0
    if function(n1) * function(n2) >= 0:
        return print("Not valid values")
    while n2 - n1 >= lim:
        subtractionOfFuncs = function(n1) - function(n2)
        result = n2 - ((n1 - n2) / subtractionOfFuncs * function(n2))

        if function(result) == 0:
            break
        if function(result) * function(n1) < 0:
            n2 = result
        else:
            n1 = result

    print(round(result, str(lim).count("0")))
