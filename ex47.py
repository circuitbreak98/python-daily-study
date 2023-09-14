class Cycle1:
    def __init__(self, data, count):
        self.data = data
        self.count = count
    
    def __iter__(self):
        return CycleIterator(self.data, self.count)
    

class CycleIterator:
    def __init__(self, data, count):
        self.data = data
        self.index = 0
        self.count = count
        self.current_count = 0

    def __next__(self):
        #if self.count
        if self.current_count == self.count:
            raise StopIteration
        
        elif self.index >= len(self.data):
            self.index = 0

        value = self.data[self.index]
        self.index+=1
        self.current_count+=1
        return value


class Circle1():

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        n = len(self.data)
        return (self.data[x%n] for x in range(self.max_times))

    

c = Circle1('abc', 10)
print(list(c))