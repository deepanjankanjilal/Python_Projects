# Formatting output in python with % and {}
# %d - int %s - string %f or %g - float
# lambda function in python -- number of arguments to the function
# *args and **kwargs -- number of keyword argument

name = "John"
age = 25
salary = 1.25

print(name,age,salary)
print("Name:%s Age:%d Salary:%g"%(name,age,salary))
print("Name:{} Age:{} Salary:{}".format(name,age,salary))
print("Name:{0} Age:{1} Salary:{2}".format(name,age,salary))

x = lambda a,b,c : a + b +c
print(x(5,6,7))

def summation(*args):
    s = 0
    for i in args:
        s+=1
    print("sum is ", s)
summation(1,2,3,4,5,6)

class Bank:
    def rateOfInterest(self):
        return 0

class ICICI(Bank):
    def rateOfInterest(self):
        return 10.5

obj = ICICI()
print(obj.rateOfInterest())

obj1 = Bank()
print(obj1.rateOfInterest())

class myClass:
    def __disp1(self):
        print("This is disp1")
    def disp2(self):
        print("This is disp2")
        self.__disp1()

ob = myClass()
ob.disp2()
ob.__disp1

