""" Single Inheritance """

class A:
    #class data(a,b,c)
    a,b,c=10,20,30
    def __init__(self,p,q,r):
        #instance data(x,y,z)
        self.x=p
        self.y=q
        self.z=r
    def display1(self):
        print("this is display1 from class A")
class B(A):
    x1,y1,z1=100,200,300
#create the object for class B
b1=B(1000,2000,3000)
print(b1.a,b1.b,b1.c,b1.x,b1.y,b1.z)
print(b1.x1,b1.y1,b1.z1)
b1.display1()


""" Multiple Inheritance """

class A:
    a,b,c=100,200,300
class B:
    x,y,z=200,300,400
class C:
    p,q,r=500,600,700
class D(A,B,C):
    pass
#create the object for class D
d1=D()
print(d1.a,d1.b,d1.c,d1.x,d1.y,d1.z,d1.p,d1.q,d1.r)


""" Multi level inheritance """

class A:
    a,b,c,d=100,200,300,5000
class B(A): #B==>A+B
    x,y,z=200,300,400
class C(B): #C==>A+B+C
    p,q,r=500,600,700
class D(C): #D==>A+B+C+D
    pass
#create the object for class D
d1=D()
print(d1.a,d1.b,d1.c,d1.d,d1.x,d1.y,d1.z,d1.p,d1.q,d1.r)


""" Hierarchial Inheritance """

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

dog.sound()  # Inherited from Animal
dog.bark()

cat.sound()  # Inherited from Animal
cat.meow()