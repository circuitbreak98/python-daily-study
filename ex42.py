class FlexibleDict(dict):
    '''def __missing__(self,key):
        if type(key) is int:
            return self[str(key)]
        elif type(key) is str:
            return self[int(key)]
    '''
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)

fd = FlexibleDict()

fd['a'] = 100
print(fd['a'])

fd[5] = 500
print(fd[5])

fd[1] = 100
print(fd['1'])

fd['2'] = 200
print(fd[2])