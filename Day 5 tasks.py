""" Validate Url """

import re
url = input("Enter a URL: ")
pattern = r'(https?:\/\/)?(www\.)?([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(\/\S*)?'
match = re.match(pattern, url)
if match:
    print("Valid URL")
else:
    print("Invalid URL")


""" Validate Password """

import re
password = input("Enter a password: ")
pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}'
match = re.match(pattern, password)
if match:
    print("Valid password")
else:
    print("Invalid password")




