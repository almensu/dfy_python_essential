
class A():
    def a(self):
        print('我是A类a方法')

class B():
    def a(self):
        print('我是B类a方法')

class C():
    def c(self):
        print('我是C类c方法')

class D(A, B, C):
    def __init__(self, name, address):
        self.name =  name
        self.__address = address

    def d(self):
        print('我是D类d方法')

    def get_address(self):
        return self.__address


dd = D('Su', 'Guangdong')
print(dd.name)
print(dd.get_address())

dd.__address = 'Shenzhen'
print(dd.__address)
print(dd.get_address())
print(dd.__dict__)




