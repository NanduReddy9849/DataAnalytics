a = "Nandu Reddy"
b=21
msg="My name is {0} and I am {1} yeras old".format(a,b)
print(msg)


a="Python"
print("This article is written in {}".format(a))

print("hi ! My name is {} and I am {} years old".format("Nandu",21))


# fstring

name="Nandu Reddy"
age=21
print(f"Hello, My Name is {name} amd I'm {age} years old.")


""" Inner Functions """

def fun1(msg):   # outer function
    def fun2():  # inner function
        print(msg)
    fun2()
fun1("hello")



""" Decorator """

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
# Applying the decorator to a function

@decorator  #greet = decorator(greet)

def greet():
    print("Hello World")
greet()



# Signature 

import inspect
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
# Applying the decorator to a function

@decorator  #greet = decorator(greet)

def greet():
    print("Hello World")
greet()
print(inspect.signature(decorator))


""" Example on iter """

numbers=[1,2,3,4,5]
iter_numbers=iter(numbers)
print(next(iter_numbers))
print(next(iter_numbers))