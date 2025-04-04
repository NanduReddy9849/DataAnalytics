""" polymorphism """

# working with method overloading

class Sample:
    #method with default arguments
    def display(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)
# create the object for sample class
s1=Sample()
s1.display()
s1.display(100)
s1.display(100,200)