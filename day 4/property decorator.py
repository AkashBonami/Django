class person:
    def __init__(self):
        self.__name=''

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, val):
        self.__name=val
    @name.deleter
    def name(self):
        del self.__name
p=person()
p.name="Akash Mittal"
print(p.name)
del p.name
print(p.name)
