class CycleIterator:
    def __next__(self):
        #if self.count
        if self.index >= len(self.data):
            self.index = 0
        
        
class Cycle:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.count = 0
    
    def __iter__(self):
        return CycleIterator(self)