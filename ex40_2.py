class Person:
    population = 0
    def __init__(self):
        Person.population+=1
    def __del__(self):
        Person.population-=1

p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
print(f'p1\'s population is {p1.population}')
del p1
del p2
del p3
del p4
del p5
print(f'Person\'s population is {Person.population}')

