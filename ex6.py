def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    
    return f'{word[1:]}{word[0]}ay'

def pl_sentence(sentence):
    result = ''
    for w in sentence.split():
       result += pig_latin(w)
       result += ' '
    return result

def pl_sentence2(sentence):
    return ' '.join(map(pig_latin, sentence.split()))

def pl_sentence3(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

print(pl_sentence('this is a test translation'))
print(pl_sentence2('this is a test translation'))
print(pl_sentence3('this is a rest translation'))
