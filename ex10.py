def mysum1(*args):
    acc = args[0]
    for i in args[1:]:
        acc += i
    return acc

def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum())
print(mysum(1,2,3))
print(mysum('abc','def'))
print(mysum([1,2,3],[4,5,6]))
