
#Micah Robinson 1/27
# choices = rock, paper, scissors

# if rock vs paper-> paper wins
# if rock vs scissor-> rock wins
# if paper vs scissor-> scissor wins
# if user and computer choice =, then it's a tie
#ask if want to play again

import random, os
os.system('cls')

print("###############################################")
print("#                                             #")
print("#                                             #")
print("#                                             #")
print("#           ROCK PAPER SCISSORS GAME          #")
print("#                                             #")
print("#       Choices: rock  paper  scissor         #")
print("#           SELECT YOUR CHOICE                #")
print("#                                             #")
print("###############################################")




user = input("Select Choice: ")
choices = ["rock", "paper", "scissors"]
computer= random.choice(choices)
print("\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print("Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
print( "Do you want to play again? Y or N")
user = input ("Select Choice: ")
choices= ( "Y", "N")
if user == "Y":
    os.system('cls')
    user = input("Select Choice: ")
choices = ["rock", "paper", "scissors"]
computer= random.choice(choices)
print("\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print("Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")



