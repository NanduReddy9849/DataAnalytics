""" Class """

class Dog:
    sound="Bark"
dog1=Dog()  # create an object from the class
print(dog1.sound)  # access the class attribute


""" Constructor """

class Dog:
    species="Canine"  # Class Attribute
    
    def __init__(self,name,age):  # When You create the object
        self.name=name  # Instance Attribute
        self.age=age    # Instance Attribute
        
    def __str__(self):   # print the object ie like toString()
        return f"{self.name} is {self.age} years old."  # Returning a string
        
# Creating an object of the dog class
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)

print(dog1.name)
print(dog1.species)
print(dog1)
print(dog2)



# Example 


class Dog:
    # Class Variables
    species="Canine" 
    
    def __init__(self,name,age):  # When You create the object
        # instance variables
        self.name=name 
        self.age=age   
        
    def __str__(self):   # print the object ie like toString()
        return f"{self.name} is {self.age} years old."  # Returning a string
        
# Creating an object of the dog class

dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)

#Access class and instance variables

print(dog1.species)  # class variable
print(dog1.name)     # instance variable
print(dog2.name)     # instance variable

# Modify instance Variable

dog1.name="Max"
print(dog1.name) # Updated instance variable

# Modify Class variable

dog1.species="Lab"
print(dog1.species)


""" Inheritance """

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):  # Create the child class
    def sound(self):
        return "Woof !"
    
a=Animal("Generic Animal")  # init method

d=Dog("Buddy")

# Accessing attributes and methods
print(a.name)
print(d.name)
print(d.sound())


# Example

class Color:
    def __init__(self):
        self.name="Green"
        self.lg=self.Lightgreen()
    def show(self):
        print('Name:',self.name)
        
    class Lightgreen:
        def __init__(self):
            self.name="Light Green"
            self.code='024avc'
        def display(self):
            print("name:",self.name)
            print("code:",self.code)
            
outer=Color()  # outer class object creation
outer.show()   # outer class method innvocation

g=outer.lg     # inner class object creation
g.display()    # inner class method calling


""" Overridden method using super() """

class Parent():
    def show(self):
        print("Inside Parent")
class Child(Parent):
    def show(self):
        super().show()
        print("Inside Child")

obj=Child
obj.show()


""" Encapsulation """

# Private 

class Private:
    def __init__(self):
        self.__salary=5000
    def salary(self):
        return self.__salary
obj=Private()
print(obj.salary())



