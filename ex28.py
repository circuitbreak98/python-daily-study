def join_numbers1(numbers):
    return ','.join([str(n) for n in numbers])

def join_numbers(numbers):
    return ','.join(str(number)
                    for number in numbers)

print(join_numbers(range(15)))