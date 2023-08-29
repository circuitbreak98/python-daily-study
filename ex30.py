def flatten1(lists):
    acc = []
    [acc.extend(lst) for lst in lists]
    return acc

def flatten2(lists):
    return [x for lst in lists for x in lst]
     
def flatten(mylist):
    return [one_element 
            for one_sublist in mylist 
            for one_element in one_sublist]
'''
lists = [[1,2], [3,4]]

for lst in lists:
    for x in lst:
        print(x)
'''

lists = flatten([[1,2],[3,4]])
print(lists)