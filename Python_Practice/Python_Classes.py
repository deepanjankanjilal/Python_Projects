# Instance method and static method
# class myClass:
#     def m1(self):
#         print("instance method")
#
#     @staticmethod
#     def m2(self):
#         print("static method")
#
# mc = myClass()
# mc.m1()
# mc.m2("deep")

# # Variables inside the class
# class myClass:
#     a,b = 10,20
#
#     def out(self):
#         print(self.a+self.b)
#
# ob = myClass()
# ob.out()

# # Local, Global and Class variables
# i,j=30,40 # Global variables
# class myClass:
#     a, b = 10, 20 # Class variables
#
#     def add(self,x,y): # Local variables
#         print(x+y) # accessing local variables
#         print(self.a + self.b) # accessing class variables
#         print(i+j) # accessing Global variables
#
# ob = myClass()
# ob.add(100,200)

# variables with same name
# a,b=30,40 # Global variables
# class myClass:
#     a, b = 10, 20 # Class variables
#
#     def add(self,a,b): # Local variables
#         print(a+b) # accessing local variables
#         print(self.a + self.b) # accessing class variables
#         print(globals()['a'] + globals()['b']) # accessing Global variables
#
# ob = myClass()
# ob.add(100,200)
# print(id(a))
# print(id(b))

# class myClass:
#     def m1(self):
#         print("first method")
#
#     def __init__(self):
#         print("default constructor")
# c= myClass()
# c.m1()

# class myClass:
#     def values(self,val1,val2):
#         print(val1)
#         print(val2)
#         self.val1 = val1
#         self.val2 = val2
#     def add(self):
#         print(self.val1 + self.val2)
# ob = myClass()
# ob.values(10,20)
# ob.add()

# Calling current class method froma nother method
class myClass:
    def m1(self):
        print("this is m1 method")
        self.m2(100)
    def m2(self,a):
        print("this is m2 method", a)
ob = myClass()
ob.m1()