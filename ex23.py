import json
import glob
def print_scores(dirname):
    for filename in glob.glob(dirname+'*.json'):
        print(filename)
        with open(filename) as f:
            dic = {'math':[],
                   'literature':[],
                   'science':[]}
            scores = json.load(f)
            for score in scores:
                for course in ['math', 'literature', 'science']:
                    dic[course].append(score[course])

            for course in ['science', 'math', 'literature']:
                l = dic[course]
                print(f'{course}: min {min(l)}, max {max(l)}, average {sum(l)/len(l)}') 





print_scores('./scores/')
