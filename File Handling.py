""" File Handling """

file=open("Test.txt",'r')
content=file.read()
print(content)
content1=file.readline()
content2=file.readlines()
file.close()

# Example 2

file=open("Test.txt",'w')
file.write("Nandu Age is 21\n")
file.write("and he is From Anantapur\n")

# Example 3

file=open("Test.txt",'a')
file.write("New Content")
file.close()

# Existing or Not

import os
if os.path.exists("Test.txt"):
    with open('Test.txt','r') as file:
        content=file.read()
        print(content)
else:
    print("File doesn't Exist")
    
# Example 4

import os
try:
    with open("Test.txt",'r') as file:
        data=file.read()
    with open("Test1.txt",'w') as filewrite:
        filewrite.write(data)
    print("file copied succesfully")

except FileNotFoundError:
    print("input or output operation file")
except IOError as e:
    print(f"I/O Exception:{e}")
except Exception as e:
    print("An unexcepted Error")
    
# Remove the File

import os
os.remove('newtest.txt')
