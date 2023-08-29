def hex_output():
    acc = 0
    num = input("enter your hex number: ")
    for i,n in enumerate(reversed(num)):
        acc += int('0x'+n)*(16**i)
        return acc

print(hex_output())
