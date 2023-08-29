def ubbi_dubbi(word):
    ubbi_word = []
    for c in word:
        if c in 'aeiou':
            ubbi_word.append(f'ub{c}')
        else:
            ubbi_word.append(f'{c}')
    return ''.join(ubbi_word)

print(ubbi_dubbi('milk'))
print(ubbi_dubbi('octopus'))
