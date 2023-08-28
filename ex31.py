def pig_latin(text):
    if text[0] in 'aeiou':
        return f'{text}way'
    else:
        return f'{text[1:]}{text[0]}ay'

def pig_file(filename):
    with open(filename) as f:
        #return [pig_latin(word) for line in f.read() for word in line]
        return [(pig_latin(word)) for line in f.read().split('\n') for word in line.split()]
    

print(pig_file('./piglatin_ex31.txt'))

def plword(text):
    if text[0] in 'aeiou':
        return f'{text}way'

    return f'{text[1:]}{text[0]}ay'

def plfile(filename):
    return ' '.join(plword(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())

print(plfile('./piglatin_ex31.txt'))
