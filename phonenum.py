# this code is used to check phone numbers with 1st digit being 0, next three digits between 2-5 and the rest 0-9
import re
phone_number =  input("enter your phone number: ")
pattern = re.compile("^[0]{1}[2-5]{3}[0-9]+$")
result = pattern.search(phone_number)
print(result)