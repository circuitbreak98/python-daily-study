def hex_output():
    acc = 0
    num_str = input('type your hexadecimal number: ')
    for i,n in enumerate(reversed(num_str)):
        #acc += eval('0x'+n)*(16**i)
        acc += int(n, 16)*(16**i)
    return acc
print(hex_output())
