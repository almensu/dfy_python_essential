# -*- coding: utf-8 -*-

lists = [1,2,3,4,5,6,7,8,9,0]


# for item in lists:
#     # 循环体
#     print(item)
#     print('for in middle')
# # 循环外
# print('for in end')


# for item in lists:
#     # 循环体
#     print(item)
#     print('for in middle')
#     print('for in end')


# for num in range(1,10):
#     print(num)
# print('-----------------')
#
# for num in range(1,10,2):
#     print(num)


# nums = list(range(1,10))
# print(nums)
#
# # 查看类型 type
# print(type(nums))
# print(type(range(1,10)))


# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)


# squares = [value**2 for value in range(1,11)]
# print(squares)
#
# print(max(squares))
# print(min(squares))
# print(sum(squares))

# # 切片
# colors = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#
# print(colors)
# print('--------------')
# print(colors[0:2])
# print(colors[0:4])
# print('--------------')
#
# print(colors[:2])
# print(colors[2:])
# print(colors[-2:])
# print('--------------')
#
# print(colors[4:])
# print(colors[:])
# print('--------------')

L = []

for r in range(100):
    L.append(r)

print(L[50:60])
print('--------------')
print(L[:10])
print('--------------')
print(L[-10:])
print('--------------')
print(L[70:])
print('--------------')
print(L[::2])
print('--------------')
print('--------------')
print(L[60::2])


# 元祖 小括号，起到保护机制