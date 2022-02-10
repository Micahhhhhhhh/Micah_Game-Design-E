#micah robinson
# 1/31
#strings=array of characters
# has many function

import os,random
os.system('cls')

myName= "Maria Suarez"
print (myName[6])
myStatement=""" My name is so nice because 
blah blah blajhhh

what ever
erte"""
for elem in myName:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words=["Radio", "Clues", "suite", "robot", "peter"]
word=random.choice(words)
print(word)
check=True
while check:
    letter=input("Dear user, please give us a nice letter")
    if len(letter)>1 or not letter.isalpha():
        print("BAD")
    else:
        check=False
print("ready to play the game")
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end=" ")
    else:
        print("_", end=" ")



# print(" My last name begins with " +myName[6])
# print(myStatement)
# if 'blah' in myStatement:
#     print('true')
# print('expert' not in myStatement) 
# Index= myName.find(" ")
# print(Index)
# #finding the length of word
# wordLen=len(myName)
# print(wordLen) #your last index is len-1
# print(myName[11])
# for i in range(wordLen-1):
#     if "a" in myName[i]:
#         print(i, end=", ")
# print("")
# print("done")
# myStatement=myStatement.upper()
# print(myStatement)

# check=True
# while check:
#     letter=input("Dear user, please give us a nice letter")
#     if len(letter)>1 or not letter.isalpha():
#         print("BAD")
#     else:
#         check=False
# print("ready to play the game")