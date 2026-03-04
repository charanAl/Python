# def add(a,b):
#     print(a+b)
# add(20,5)

# def students(name,age):
#     print(name,age)
# students(age=22,name='charan')

# def greet(name='user'):
#     print('Hello','charan')
# greet
# print('charan')

# def wish(name='admin'):
#     print("welcome",name)
# wish()
# print("Charan")

# def total(*args):
#     print(sum(args))

# total(10,10,30)


# def add(a,b,/):
#     print(a+b)
# add(10,20)

# def add(a, b, /):
#     print(a + b)

# add(10, 20)
# add(a=10, b=20) ❌ Error



# def addition1(*args):
#     print(sum(args))
# addition1(10,20)

def login(*,username , password):
    print(username,password)
login(username='charan',password='1892374897')