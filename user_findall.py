import re

f = open ("Sec.Info.txt", "r")
text = f.read()

user_input = input("enter the word to find all: ")
pattern = user_input
x = re.findall(pattern,text)
print(x)