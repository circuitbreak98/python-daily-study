def how_many_different_numbers(numbers):
    return len(set(numbers))
      
print(how_many_different_numbers([1,2,3,1,2,3,4,1]))

numbers = [1,2,3,1,2,3,4,1]
unique_numbers = set()
for number in numbers:
    unique_numbers.add(number)
    print(unique_numbers)

unique_numbers = set()
unique_numbers.update(numbers)
print(unique_numbers)

#unique_numbers = {numbers} //TypeError: unhashable type: 'list'

unique_numbers = set()
unique_numbers = {*numbers}
print("* operator")
print(unique_numbers)