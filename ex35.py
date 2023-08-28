import string
def gematria_dict1():
    return {chr(i+96):i for i in range(1,27)}

def gematria_dict2():
    return {ch:(ord(ch)-96) for ch in string.ascii_lowercase}

def gematria_dict():
    return {char:index for index,char in enumerate(string.ascii_lowercase,1)}

def gematria_for(word):
    dic = gematria_dict()
    return sum(dic.get(ch, 0) for ch in word)

def gematria_equal_words(input_word):
    gematria_num = gematria_for(input_word.lower())
    return [word.strip() for word in open("./text_ex34.txt") 
            if gematria_num == gematria_for(word.lower())]

#print(gematria_dict())
print(gematria_for('cat'))
print(gematria_equal_words('cat'))
