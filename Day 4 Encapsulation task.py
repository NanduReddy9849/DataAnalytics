""" Encapsulation """

class Sample:
    #define the data using constructor
    def __init__(self,x,y,z):
        #here x,y,z are data
        self.x=x
        self.y=y
        self.z=z
    def display(self):
        print(self.x)
        print(self.y)
        print(self.z)
        
#create the object for Sample Class

s1=Sample(10,20,30)  #x=10,y=20,z=30
s1.display()
s1=Sample(100,200,300)
s1.display()