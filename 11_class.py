# -*- coding: utf-8 -*-

class Dog():
    def __init__(self, name, age, weight=10):
        self.name = name
        self.age = age
        self.weight = weight

    def eat_bone(self):
        print(self.name + ' eatting bone!')

    def bark(self):
        print(self.name + ' is barking!')

    def set_weight(self, weight):
        self.weight = weight



tudou = Dog('Tudou', '3', weight=15)

print(tudou.name)
print(tudou.age)
print(tudou.weight)

tudou.eat_bone()
tudou.bark()
tudou.set_weight(999)
print(tudou.weight)