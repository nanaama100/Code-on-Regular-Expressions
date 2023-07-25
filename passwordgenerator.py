#this code is used to generate a password which as has 8 or more characters containing at least 1 Uppercase, 1 Lowercase, 1 Digit, 1 Special Symbol 
import re
generated_password = "Am2@pass"
pattern = re.compile("^[a-zA-Z0-9]+[@]{1}[a-z]+$")
result = pattern.search(generated_password)
print(result)