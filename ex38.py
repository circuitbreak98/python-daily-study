'''class ScoreList():
    def __init__(self, scores):
        self.scores = scores
    
    def average(self):
        return sum(self.scores) // len(self.scores)

scores = ScoreList([1,2,5,7,9,13,20])
print(f'final score is {scores.average()}')'''


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops1():
    s1 = Scoop('vanila')
    s2 = Scoop('Orange')
    s3 = Scoop('persimmon')
    return [s1,s2,s3]

scoops = create_scoops1()

for i, s in enumerate(scoops):
    print(f"{i+1}th scoop's flavor is {s.flavor}")

def create_scoops():
    scoops = [Scoop('chocolate'),
              Scoop('vanilla'),
              Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)

create_scoops()