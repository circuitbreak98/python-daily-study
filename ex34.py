def get_sv1(filename):
    vowels = {'a','e','i','o','u'}
    with open(filename) as f:
        for Line in f:
            if vowels.issubset(set(Line)):
                print(Line)

def get_sv(filename):
    vowels = {'a','e','i','o','u'}
    return {word.strip()
            for word in open(filename)
            if vowels < set(word.lower())}

#get_sv("./text_ex34.txt")
print(get_sv("./text_ex34.txt"))