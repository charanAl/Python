class A:
    def __init__(self):
        print('This is a A')
    def fun1(self):
        print('This is a father ')
    
class B(A):
    def __init__(self):
        print('This is a clss B')
        super().__init__()
    def fun2(self):
        print('This is a cls B')
obj=B()
obj.fun1()
obj.fun2()