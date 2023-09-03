class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def animals_by_color(self, color):
        pass

    def animals_by_legs(self, legs):
        pass

    def number_of_legs(self):
        pass


class Cage:
    def __init__(self, id):
        self.id = id
        self.animals = []
    def add_animals(self, *cage_animals):
        for i in cage_animals:
            self.animals.append(i)

    '''def __repr__(self):
        return f'cage ID: {self.id}\n {", ".join([repr(i) for i in self.animals])}'
    '''
    def __repr__(self):
        output = f'Cage {self.id}\n'
        output += '\n'.join(
            '\t' + str(animal) for animal in self.animals)
        return output


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
