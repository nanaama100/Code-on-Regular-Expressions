#this code is used to check a password with 8 or more characters containing at least 1 Uppercase, 1 Lowercase, 1 Digit, 1 Special Symbol
# in order to check password, the user needs to enter the password to see if its accurate. 
import re

user_entry = input("enter your password: ")
pattern = re.compile("^[a-zA-Z0-9]+[@]{1}[a-z]+$")
result = pattern.search(user_entry)
print(result)





