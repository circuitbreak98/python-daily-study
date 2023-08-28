def dictdiff1(dict1, dict2):
    diff = {}
    for k in dict1.keys():
        if k in dict2:
            if dict1[k] == dict2[k]:
                pass
            else:
                diff[k] = [dict1[k], dict2[k]]
        else:
            diff[k] = [dict1.get(k), dict2.get(k)]
    
    for k in dict2.keys():
        if k in dict1:
            if dict1[k] == dict2[k]:
                pass
            else:
                diff[k] = [dict1[k], dict2[k]]
        else:
            diff[k] = [dict1.get(k), dict2.get(k)]
    return diff

def dictdiff2(first,second):
    output = {}
    all_keys = first.keys() | second.keys()
    same_keys = first.keys() & second.keys()

    for k in all_keys:
        if k in same_keys:
            if first[k]==second[k]:
                pass
            else:
                output[k]  = [first[k],second[k]]
        else:
            output[k] = [first.get(k), second.get(k)]
    return output

def dictdiff(first,second):
    output = {}
    all_keys = first.keys() | second.keys()

    for k in all_keys:
        if first.get(k)!=second.get(k):
            output[k] = [first.get(k), second.get(k)]
    return output


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1,d1))
print(dictdiff(d1,d2))

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3,d4))

d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1,d5))