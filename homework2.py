#Micah Robinson 1/22 homework
import os, random 
os.system('cls')




print("    Guess a number menu   ")


myNumber=random.randint(1,100)
GameOn=True
while(GameOn):
    userGuess=int(input("Guess a number from 1-100 :)" ))
if myNumber == userGuess: 
    print("You guessed it!")
    GameOn=False
else:
    print("good luck next time")
print("the number to guess was "+ str(myNumber))