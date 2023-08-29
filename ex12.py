from collections import Counter
def most_repeating_word1(words):
    most_word = ''
    most_count = 0
    for word in words[1:]:
        count = Counter(word).most_common()[0][1]
        if(most_count<count):
            most_word = word
            most_count = count
    return most_word

def most_repeating_word2(words):
    def most_repeating_letter_count(word):
        return Counter(word).most_common(1)[0][1]    
    return sorted(words, key=most_repeating_letter_count, reverse=True)[0]

def most_repeating_word(words):
    def most_repeating_letter_count(word):
        return Counter(word).most_common(1)[0][1]    
    return max(words, key=most_repeating_letter_count)

words = 'this is an elementary test example'.split()
print(most_repeating_word(words))

