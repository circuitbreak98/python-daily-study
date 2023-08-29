def mysum(*args):
    acc = 0
    for i in args:
        acc += i
    return acc
a = (1,2,3,4)
b = [1,2,3,4]
print(mysum(1,2,3,4))
print(mysum(*a))
print(mysum(*b))


