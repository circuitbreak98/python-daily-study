def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    
    return f'{word[1:]}{word[0]}ay'

def pig_latin_my(word):
    vowels = ('a','e','i','o','u')
    if word.startswith(vowels):
        return word+'way'
    else:
         return word[1:]+word[0]+'ay'

print(pig_latin('air'))
print(pig_latin('eat'))
print(pig_latin('python'))
print(pig_latin('computer'))

