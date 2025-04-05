""" Exception Handling """

try:
    x=10/0
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("Completed execution")
    
    
# Example 2

try:
    num=int(input("Enter a number:"))
    result=10/num
except ValueError as e:
    print(f"Invalid input:{e}")
except ZeroDivisionError as e:
    print("cannot divided by zero")
except Exception as e:
    print("An Unexcepted")
else:
    print(f"Result:{result}")
finally:
    print("Code executed succesfully")
    
# Example 3

class NotEligible(Exception):
    pass

def checkage(age):
    if age<18:
        raise NotEligible("Age must be 18")
    else:
        print("You are Eligible")
        
try:
    checkage(16)
except NotEligible as e:
    print("Error")