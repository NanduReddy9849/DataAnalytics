""" Access specifiers """

class Sample:
    #data
    a=10  # public data
    _b=20 # protected data
    __c=30 # private data
    # methods
    def display(self):
        print("This is public method")
    def _display1(self):
        print("this is protected method")
    def __display2(self):
        print("This is private method")
class Sample1(Sample):
    pass
#create object for Sample1
s1=Sample1()
print(s1.a)
print(s1._b)
print(s1.__c) # error (private data can't be accessed)
s1.display()
s1._display1()
s1.__display2()  # error