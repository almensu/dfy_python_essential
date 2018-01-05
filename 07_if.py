# -*- coding: utf-8 -*-

cars = ['ford', 'land rover', 'mercedes-Benz','bmw','audi','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


if cars:
    print(cars)
else:
    print('列表为空')