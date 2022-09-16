class abc:
    age = 21
    def __init__(self ,name):
        self.name=name
    @classmethod
    def change(cls,age):
        cls.age=age
    @staticmethod
    def checkage(age):
        if age >= 18:
            print("Adult")
person=abc("Akash")
abc.age=21
print(person.name)
abc.checkage(person.age)