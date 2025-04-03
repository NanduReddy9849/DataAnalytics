""" String Functions """

text="Nandi vardhan reddy"
print(len(text))
print(text.lower())
print(text.upper())
print(text.strip()) # Remove leading & Trailing spaces
print(text.replace("Reddy","Nandu"))
print(text.split())
print("-".join(text)) #list into string
print(text.find("Vardhan")) # find substring position
print(text.count("Vardhan"))
print(text.capitalize()) # capitalise first letter
print(text.title()) # capitalise Each word
print(text.isdigit())
print(text.isalpha())
print(text.swapcase())

""" list functions """

lst=[10,20,30,40]
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
lst.append(60)
print(lst)
lst.extend([50,70])
print(lst)
lst.insert(2,3)
print(lst)
lst.remove(50)
print(lst)
lst.pop()
print(lst)
print(lst.count(70))
print(lst.index(40))
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print(sorted(lst))
lst.reverse()
print(lst)
lst.clear()
print(lst)


""" tuple functions """

tup=(10,20,30,40,50,40)
print(len(tup))
print(max(tup))
print(min(tup))
print(sum(tup))
print(tup.count(40))
print(tup.index(20))
print(sorted(tup))


""" Grades """

marks=int(input("Enter the Marks:"))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<=80:
    print("Grade B")
elif marks>=60 and marks<=70:
    print("Grade C")
else:
    print("Fail")
    

""" Reverse a string and Check for Palindrome """

str=input("Enter a String:")
print(str[::-1])
if str==str[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")


""" Check for Prime Number """

number=int(input("Enter a Number:"))
for i in range(2,number):
    if number%i==0:
        print("not prime")
        break
else:
    print("prime")
    

""" Fibanocci Series """

number=int(input("Enter a Number:"))
n1,n2=0,1
for i in range(number):
    print(n1,end=" ")
    n1,n2=n2,n1+n2
    

""" Check the Given Number is Even Or Odd """

number=int(input("Enter a Number:"))
for i in range(1,number):
    if number%2==0:
        print("Even")
        break
    elif number%2!=0:
        print("Odd")
        break
else:
    print("Zero")
    
    
""" Print 1 to 100 and even number can change to '@'  """

for i in range(1,101):
    if i%2==0:
        print("@",end=" ")
    else:
        print(i,end=" ")
        

""" Collection iterate each element and square it """

numbers=[1,2,3,4,5]
for i in numbers:
    print(i*i,end=" ")
    

""" Program To Retrieve the keys from the dictionary and based on the key to display the value """

my_dict={"name":"Nandu","age":21,"city":"Tadipatri"}
print("keys in dictionary:",list(my_dict.keys()))
key=input("Enter a Key:")
if key in my_dict:
    print(f"Value for '{key}':{my_dict[key]}")
else:
    print("key not found in the dictionary")
    

""" Create get The user details from the user, next function in to display the value
whatever we got from the user """

def get_user_details():
    user_name =input("Enter your name: ")
    user_age = input("Enter your age: ")
    user_email = input("Enter your email: ")
    return user_name,user_age,user_email
n,a,email = get_user_details()

def display(name,age,email):
    print(name)
    print(age)
    print(email)
display(n,a,email)


