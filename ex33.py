def transform_values(func, dic):
    return {k:func(v) for k,v in dic.items()}

d = {'a':1, 'b':2, 'c':3}
print(transform_values(lambda x:x*x, d))