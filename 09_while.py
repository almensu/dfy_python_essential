# -*- coding: utf-8 -*-

# ative = True
# while ative:
#     msg = input('输入信息：')
#     if(msg == 'quit'):
#         ative = False
#     else:
#         print('输出信息：' + msg)
# print('输入结束')


students = {}
doing = True

while doing:
    name = input('姓名：')
    age = input('年龄：')
    students[name] = age
    is_continue = input('还继续输入吗？yes／no')

    if(is_continue == 'no'):
        doing = False
print('End.')

for name, age in students.items():
    print(name+ ':' +age)







