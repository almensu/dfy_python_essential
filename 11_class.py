# -*- coding: utf-8 -*-

# class Dog():
#     def __init__(self, name, age, weight=10):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def eat_bone(self):
#         print(self.name + ' eatting bone!')
#
#     def bark(self):
#         print(self.name + ' is barking!')
#
#     def set_weight(self, weight):
#         self.weight = weight
#
#
#
# tudou = Dog('Tudou', '3', weight=15)
#
# print(tudou.name)
# print(tudou.age)
# print(tudou.weight)
#
# tudou.eat_bone()
# tudou.bark()
# tudou.set_weight(999)
# print(tudou.weight)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

luo = Student('MX Luo', 80)
su = Student('YH Su', 90)

print(luo.print_score())
print(su.print_score())

print('Grade of Luo: ' + luo.get_grade())