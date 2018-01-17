
class Peple():
    '''定义了人类'''
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def getName(self):
        return self.name

    country = 'China'

# 先创造实例
p1 =  Peple('Su', 21, 'male')
p2 = Peple('Zheng', 20, 'male')

# 1 属性： 实例.属性   类名.类属性  内置函数访问属性
# print(p1.name)
# print(p1.age)
# print(p1.sex)
#
# print(p2.name)
# print(p2.age)
# print(p2.sex)
#
# print(p1.getName())
#
# print(p1.country)

# print(getattr(p1, 'name'))
# print(getattr(p1, 'age'))
#
# # 判断
# print(hasattr(p1, '1'))
#
# #设置属性
# setattr(p1, 'name', 'almen')
# print(p1.name)
#
#
# #删除对象属性
# delattr(p1, 'name')
# print(p2.name)
#
#
# # 查看属性
# print(Peple.__dict__)
# print(p1.__dict__)

# 查看文档
print(Peple.__doc__)