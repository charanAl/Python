class Father:
    def fun1(self):
        print('This is a father')
class Mother:
    def fun2(self):
        print('This is a Mother')
class Child(Father,Mother):
    def fun3(self):
        print('This is  child')
object = Child()
object.fun1()
object.fun2()
object.fun3()