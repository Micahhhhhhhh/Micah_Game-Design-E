#micah robinson
# 2/8
#Word game with 3 levels:
#               1.Fruits  
#               2. Animals 
#               3.Computer Parts
#  Choice:


import os, random
os.system('cls')
choice=0
def menu():
    global choice
    
    print("###############################################")
    print("#                                             #")
    print("#                                             #")
    print("#                                             #")
    print("#                                             #")
    print("#                  WORD                       #")
    print("#              GUESS                          #")
    print("#                    GAME                     #")
    print("#                                             #")
    print("#                                             #")
    print("#     1. fruits                               #")
    print("#     2. Animals                              #")
    print("#     3. Computer Parts                       #")
    print("#              SELECT YOUR CHOICE             #")
    print("###############################################")
    
    check=True
    while check:
        try:
            choice=int(input("Choice: "))
            check = False
        except ValueError:
            print("Sorry, wrong choice, please insert 1 to 3 only")

    

words=""
guess=""
def selectWord():
    global words
    fruits= ["bannana", "grapes", "watermelon", "papaya", "oranges","tomatoes",
    "mangos", "kiwis","strawberries","apples", "blackberries","blueberries"]
    animals= ["lions", "tigers", "dogs", "zebras", "dolphins","sharks","monkeys","gorillas"]
    computer_parts=["keyboard","mouse","screen","chord","charger", "monitor", "printer","usb"]
    if choice == 1:
        words= random.choice(fruits)

    elif choice == 2:
        wordsr= random.choice(animals)
    elif choice == 3:
        words= random.choice(computer_parts)
    for letter in words:
        print("_",end=" ")
    print()

def playAgain():
    global gameOn
    answer=input("do you want to play again? Y/N")
    if "Y" in answer:
        menu()
        tries=0
        letterGuessed=""
        selectWord()
    else:
        gameOn=False
        print("good job, your score is",score)

def guessfunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\neneter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else: 
                print("only one letter please")
        except ValueError:
            print("only one letter please")
            
gameOn=True
menu()
tries=0
letterGuessed=""
selectWord()
score=0
while gameOn:
   
   
    guessfunction()
    letterGuessed += guess
    if guess not in words:
        tries +=1 
        print(tries)
    countLetter=0
    for letter in words:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries > 6:
        print ("\nsorry run out of tries")
        playAgain()
    if countLetter == len(words):
        print("\nYou guess it! ")
        score= (len(words) * 5 - tries*2)
        playAgain()

