def false_position(function, n1, n2, decimal):
    iterate_num = 1000000
    result = 0
    if function(n1) * function(n2) >= 0:
        return print("Not valid values")

    for i in range(iterate_num):
        subtractionOfFuncs = function(n2) - function(n1)
        result = (n1 * function(n2) - n2 * function(n1)) / subtractionOfFuncs
        if function(result) == 0:
            break
        if function(result)*function(n1)<0:
            n2 = result
        else:
            n1 = result

    print(round(result, decimal))
