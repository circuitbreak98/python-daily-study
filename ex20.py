from collections import defaultdict
def wc1(filename):
    w, c, l = 0,0,0
    #uw = {}
    uw = defaultdict(int)
    with open(filename) as f:
        for line in f:
            l += 1
            if line == '\n':
                c += 1

            for word in line.split():
                w += 1
                c += 1
                #uw[word] = uw.get(word,0) + 1
                uw[word] += 1
                for ch in word:
                    c += 1

    print(f'words: {w}, unique words:{len(uw)}, character: {c}, lines: {l}')

def wc(filename):
    counts = {'lines': 0,
              'characters': 0,
              'words' :0,}
    unique_words = set()
    
    with open(filename) as f:
        for line in f:
            counts['lines'] += 1
            counts['characters'] += len(line)
            counts['words'] += len(line.split())
            unique_words.update(line.split())
    counts['unique_words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')


wc1("./testfile_ex20.txt")