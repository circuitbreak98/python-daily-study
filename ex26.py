import operator
def add(a,b):
    return operator.add(a,b)

def sub(a,b):
    return operator.sub(a,b)

def mul(a,b):
    return operator.mul(a,b)

def div(a,b):
    return operator.truediv(a,b)

def mod(a,b):
    return operator.mod(a,b)

def pow(a,b):
    return operator.pow(a,b)

def calc(to_solve):
    operation = {'+': add,
                 '-': sub,
                 '*': mul,
                 '/': div,
                 '%': mod,
                 '**': pow,}
    op, first_s, second_s = to_solve.split()
    first, second = int(first_s), int(second_s)
    return operation[op](first, second)


print(calc('+ 1 2'))