import re
f = open ("Sec.Info.txt", "r")
text = f.read()

user_input = input("enter the word you will like to search for: ")
pattern = user_input 
x = re.search(pattern, text)
if user_input in text:
    print("Word found in text")
else:
    print("the word you are looking for is not in the text file")

