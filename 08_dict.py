# -*- coding: utf-8 -*-


# dict = {'name':'almensu', 'age':'21'}
#
# print(dict['name'])
#
# dict['sex'] = 'male'
#
# print(dict)


dict = {
    'lily':'21',
    'lilei':'22',
    'He ing': '21',
    'Liu ing':'24',
    'Zheng oucheng':'21',
    'Wu ong':'26',
    'Du an':'27',
}

for n in dict:
    print(sorted(n))

print('------')

for n in sorted(dict):
    print(n)

# 输出keys
print('------')
for n in dict.keys():
    print(n)

# 输出values
print('------')
for a in dict.values():
    print(a)

# 输出set 去重复
print('------')
for a in set(dict.values()):
    print(a)