class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f'{self.color} {self.species} {self.number_of_legs} legs'
    
class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color,4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color,0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color,2)


sheep = Sheep('white')
wolf = Wolf('black')
snake = Snake('red')
parrot = Parrot('red')

print(sheep)
print(wolf)
print(snake)
print(parrot)