# len(array)-1 = Last Index
#Micah Robinson
#2/16/2022
#list and list methods
import os, random
os.system('cls')
fruits= ["bannana", "grapes", "watermelon", "papaya", "oranges","tomatoes",
    "mangos","bannana", "kiwis","strawberries","apples", "blackberries","blueberries"]

#length of your array
size= len(fruits)
print(size)
fruits.append("rambutan")
for I in range(13): #13 is not included
    print(fruits[I])
print(fruits[size-1])
print(fruits[-2])
print (fruits.count('bannana'))
list2=[3,6,8,9,10]
fruits.append(list2)
print("append \n", fruits)
fruits.extend(list2)
print("extend \n", fruits)


numberCards-[]
for i in range(2,11):
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[1-2])
print(numberCards)