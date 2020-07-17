class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print('I am a cat, my name is',self.name,'.')

class Dog(Animal):
    def talk(self):
        print('I am a dog, my name is',self.name,'.')

def animal_talk(obj):
    obj.talk()

cat = Cat('Tom')
dog = Dog('HaHa')

animal_talk(cat)
animal_talk(dog)