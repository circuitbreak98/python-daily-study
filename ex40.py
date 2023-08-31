class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)
            '''
            else:
                print(f"the number of scoops is already 3")
            '''
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('vanila')
s2 = Scoop('Orange')
s3 = Scoop('persimmon')

b = Bowl()

b.add_scoops(s3)
b.add_scoops(s3)
b.add_scoops(s1, s2)
print(b)