def join_numbers(numbers):
    return ','.join(str(number)
                    for number in numbers
                    if number in range(10))

print(join_numbers(range(15)))