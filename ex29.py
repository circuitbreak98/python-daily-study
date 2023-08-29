def sum_numbers(string):
    return sum([int(word) for word 
                in string.split()
                if word.isdigit()])

def sum_numbers(string):
    return sum(int(word) for word 
                in string.split()
                if word.isdigit())

print(sum_numbers('10 abc 20 de44 30 55fg 40'))