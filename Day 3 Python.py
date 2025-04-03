""" Data Types """

""" Indexing """

str= "My name is Nandu"
print(type(str))
print(str[1])
print(str[-2])
print(str[4])

print(str[::-1]) # Negative Indexing



a=[1,2,"nandu",3,"reddy"]
print(a)


""" Access or retrive list using index value """

a=["nandi","vardhan","reddy"]
print(a[1])
print(a[-1])
print(a[-4])  # list index out of range

""" Tuple """

tuple1=(10,30,45,23)
print(tuple1[2])
print(tuple1[-1])

""" Boolean Type """

valid= True
Invalid=False
print(type(valid))
print(type(Invalid))
print(type(true))  #name true is not defined

""" Set """

s1=set("HelloWelcomeHello")
print(s1)

s2=set(["Hello","Welcome","Hello"])
print(s2)


#frozenset

fs=frozenset({1,2,3})
fs.add(4)   # Error

""" String Operation  slicing """
 
name="Revature"
print(name[0])
print(name[1:4])
print(name.upper())
print(name.lower())

""" Append  in list """

fruits=["apple","orange","banana"]
fruits.append("mango")
print(fruits)

""" Range """

numbers=range(1,10,2)
numbers1=range(3,29,5)
print(list(numbers))
print(list(numbers1))

""" Dictionary Data Type """

student={"name":"nandu","age":21,"city":"Tadipatri"}
print(student["name"])
print(student["age"])
print(student["city"])
print(student)

""" Binary Data Types """

b=[65,66,67]
print(b)

c=bytes([65,66,67,76])
print(c)

""" None Type """

x=None
print(type(x))

y
print(y)   # y is not defined
print(type(y))  # y is not defined

""" Flow control Statements """

# elif

a=200
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")
    

""" Nested if else """

i=0
if i!=0:
    if i>0:
        print("positive")
    if i<0:
        print("Negative")
else:
    print("zero")
    
""" while loop """

n=5
while n>0:
    n-=1
    print(n)
    
""" break """

n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
    
""" continue """

n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
    
""" for loop """

thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x)
    
""" inner for loop """

x=[1,2]
y=[4,5]
for i in x:
    for j in y:
        print(i,j)
        
""" key-value pairs """

states_tz_dict={
    'Florida': 'EST and CST',
    'Hawai': 'HST',
    'Arizona':'DST',
    'Colorado':'MST and PST'
}
for k in states_tz_dict.keys():
    print(k)
    
    
""" Defining and calling a Function """

def greet():
    print("Hello Welcome !")

greet()
    
# Function with Parameters

def greet(name):
    print("Hello",name)

greet("Nandu")

# Default  Parameter Value

def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Bob")

# Function with Multiple return values

def get_details():
    name="Nandu"
    age=21
    return name,age

n,a=get_details()
print("Name:",n,"Age:",a)

# Function with *args (Mulitple arguments)

def add_all(*numbers):
    return sum(numbers)   # sum is the predefined function
print(add_all(1,2,3,4,5))

# Function with **kwargs (keyword Arguments)

def info(**details):
    for key,value in details.items():
        print(key,":",value)
info(name="Nandu",age=21,city="Tadipatri")

""" Arrays """

import array
fruits=array.array('u',"applebananacherry")
print(fruits[0])
print(fruits[11])

# Example 2 in for loop

import array
fruits=array.array('u',"applebananacherry")
for fruit in fruits:
    print(fruit)
    
# Example

import array
fruits=array.array('u',"applebananacherry","mango") #Type error array can take only two arguments
for fruit in fruits:
    print(fruit)
    
# Example 3

import array
numbers=array.array('i',[1,2,3,4,5])
length =len(numbers)
print(length)

# Example 4

import array
numbers=array.array('i',[3,1,4,1,5,9])
numbers_sorted = sorted(numbers)
print(numbers_sorted)