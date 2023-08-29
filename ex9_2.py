def even_odd_sums(lst):
    evens = sum(lst[0::2])
    odds = sum(lst[1::2])

    return [evens,odds]


print(even_odd_sums([10,20,30,40,50,60]))
print(even_odd_sums([10,20,30,40,50,60,70]))

