# Json tp Python 


import json
x='{"name":"Nandu Reddy","age":21}'
z=json.loads(x)
print(z["name"])
print(z["age"])


# Dictionary to JSON Format

x={
   "name":"Nandu Reddy",
   "Age":21
   }
y=json.dumps(x)
print(y)


# REGEX

import re
x="The rain in spain"
y=re.search("^The.* spain$",x)
if y:
    print("yes the match is correct")
else:
    print("Not matching with the pattern")
    

# Example

x="The rain in spain"
y=re.findall("ai",x)
print(y)


z=re.search("\s",x)
z=re.split("\s",x)  # splitted with the white space

# Replace all white spaces with $

re.sub("\s","$",x)

# patterns 

pattern=r"\d+"
text="These are 123 apples"
match=re.search(pattern,text)
if match:
    print("Match found",match.group())
    
# Example 2

pattern=r"\d+"   # Matches one or more digits
text="There are 123 apples and 456 oranges"
matches=re.findall(pattern,text)
print(matches)


# Example 3

pattern =r"(\d+)-(\d+)-(\d+)"
text="The Event is on 2025-03-26"
match=re.search(pattern,text)
if match:
    print("Year:",match.group(1))
    print("Month:",match.group(2))
    print("Day:",match.group(3))
    
    
# Example 4

email_pattern=r'[a-zA-Z0-9,%+-]+@[a-zA-Z0-9."]+[a-zA-Z]{2,}'
text="please contact us enandivardhan2002@gmail.com"
match=re.search(email_pattern,text)
if match:
    print("Email found:",match.group())
    
    
# Logging

import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("Hello, Debug !")
logging.info("Hello, Info !")
logging.warning("Hello, Warning !")
logging.error("hello, Error !")
logging.critical("Hello, Critical !")


# Example 2

import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'
)

logging.debug("Hello, Debug !")
logging.info("Hello, Info !")
logging.warning("Hello, Warning !")
logging.error("hello, Error !")
logging.critical("Hello, Critical !")

