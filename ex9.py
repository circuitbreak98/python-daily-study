def firstlast1(seq):
    if type(seq) == str:
        return seq[0]+seq[-1]
    elif type(seq) == list:
        return [seq[0],seq[-1]]
    else:
        return (seq[0],seq[-1])

def firstlast(seq):
    return seq[:1]+seq[-1:]

print(firstlast('abc'))
print(firstlast([1,2,3,4]))
print(firstlast((10.0, 20.0, 30.0, 40.0)))
