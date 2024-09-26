# Password Fenerator
# Input two numbers and an operation choice.
# 15 May 2024

import random

print("\n======== Password Generator ========\n")

length = int(input("Enter desired length : "))

ListOfChars =[]

for count in range(length):
    ASCII_index = random.randint(33, 126)
    ListOfChars.append(chr(ASCII_index))

print("\n====================================")
print("Password :",''.join(ListOfChars))
print("====================================")