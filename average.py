import os 
#Micah J Robinson
# Jan 14, 2022
# Declare variables, print variables, print type of data, learn some operators


# This symbol is for comments, means compueter will ignore*
# i want to clear my terminal
os.system('cls')

#Declare and assign valuesgit config --global user.name "Your Name"
test1=89
test2=78.5
test3=86
Flag=False
#to display things on the screen, we use the function print
print(type(test1), type(test2), type(Flag))


Sum = test1 + test2 + test3


print(Sum)
Average = Sum/3
print(Average)
print("The average of 3 test is", Average)
print("test 1 =", test1, end=" ")
print("test2", test2)