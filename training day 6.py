'''#INHERITANCE IN PYTHON 
#single inheritance 
class A:
    def f1(self):
        print('class A')
class B(A):
    def f2(self):
        print('class B')
ob = B()
ob.f1()
ob.f2()
#multilevel inheritance
class A:
    def f1(self):
        print('class A')
class B(A):
    def f2(self):
        print('class B')
class C(B):
    def f3(self):
        print('class C')
ob = C()
ob.f1()
ob.f2()
ob.f3()
#multiple inheritance
class A:
    def f1(self):
        print('class A')
class B():
    def f2(self):
        print('class B')
class C(A,B):
    def f3(self):
        print('class C')
ob = C()
ob.f1()
ob.f2()
ob.f3()
#hierarical inheritance
class A:
    def f1(self):
        print('class A')
class B(A):
    def f2(self):
        print('class B')
class C(A):
    def f3(self):
        print('class C')
ob = C()
ob.f1()
ob.f3()
#hybrid inheritance
from pickle import OBJ


class School:
    def f1(self):
        print("This function is in school.")
class Student1(School):
    def f2(self):
        print("This function is in student 1. ")
class Student2(School):
    def f3(self):
        print("This function is in student 2.")
class Student3(Student1, School):
    def f4(self):
        print("This function is in student 3.")
object = Student3()
object.f1()
object.f4()

#POLYMORPHISM 
# overriding
class A:
    def __init__ (self):
        print('a')
    def m1(self):
        print('m1')
class B(A):
    def m1(self):
        print('B class')
object=B()
object.m1()'''
# MODULES
import math
print(math.sqrt(40))        

#current date time
from datetime import date
today = date.today()
print("today's date =",today)