import glob
import os
def find_longest_word(filename):
    with open(filename, encoding='utf-8-sig') as f:
        longest_word = ""
        for line in f:
            for word in line.split():
                if len(longest_word) < len(word):
                    longest_word = word
    return longest_word
    
def find_all_longest_word1(directory):
    dic = {}
    files = glob.glob(directory+'/*.txt')
    for file in files:
        longest_word = find_longest_word(file)
        dic[file] = longest_word
    
    return dic

def find_all_longest_word2(directory):    
    return {file: find_longest_word(file) 
            for file in glob.glob(directory+'/*.txt')}

def find_all_longest_word(dirname):
    return {
        filename:
            find_longest_word(os.path.join(dirname, filename))
            for filename in os.listdir(dirname)

            if os.path.isfile(os.path.join(dirname, filename))
    }


print(find_all_longest_word('./books'))
