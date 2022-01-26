#Micah Robinson 1/22 homework
import os, random 
os.system('cls')

#key word def
def menu():
    print("##########################")
    print("#    Guess a number menu #")
    print("#                        #")
    print("#    1. Choices 1-10     #")
    print("#     2. Choices 1-50    #")
    print("#    3. Choices 1-100    #")
    print("#   Select Your CHoice   #")
    print('##########################')

#Checking for correct user input

menu()          #calling function menu
check=True
while check:
    try:
        choice=int(input("Choice: "))
        check = False
    except ValueError:
        print("Sorry, wrong choice, please insert 1 to 3 only")

if choice == 1:
       myNumber= random.randint(1,10)

elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
    myNumber= random.randint(1,100)
print(choice)
GameOn=True
while(GameOn):
    userGuess=int(input("give me a number "))
    if myNumber ==userGuess:
        print("You guessed it!")
        GameOn=False
    else:
        print("good luck next time", myNumber)
print("The number to guess was " + str(myNumber))

# os.system('cls')
# menu()