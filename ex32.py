def flipdict(dic):
    flipd = {}
    return {v:k for k,v in dic.items()}

d = {'a':1, 'b':2, 'c':3}

print(flipdict(d))