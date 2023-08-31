class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        self.scoops.extend(args)
    
    def __str__(self):
        string_list = [f'{i+1}th flavor is {s.flavor}' for i, s in 
                       enumerate(self.scoops)]
    
        return '\n'.join(string_list)


s1 = Scoop('vanila')
s2 = Scoop('Orange')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)