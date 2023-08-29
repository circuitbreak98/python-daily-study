def plus_minus(lst):
    plus = sum(lst[1::2])
    minus = sum(lst[2::2])
    output = lst[0]+plus-minus
    return output

print(plus_minus([10,20,30,40,50,60]))
