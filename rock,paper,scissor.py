#Micah Robinson
import os, random 
os.system('cls')

# rock=1
# paper=2
# scissor=3
#rock vs paper-> paper wins
#rock vs scissor-> rock wins
#paper vs scissor-> scissor wins
#ask if want to play again


print("###############################################")
print("#                                             #")
print("#                                             #")
print("#                                             #")
print("#           ROCK PAPER SCISSORS GAME          #")
print("#     rock=1  paper=2   scissor=3             #")
print("#                                             #")
print("#           SELECT YOUR CHOICE                #")
print("#                                             #")
print("###############################################")
choice=int(input("Choice: "))

if choice == "rock":
       myNumber= random.randint(2,3)

elif choice == "paper":
    myNumber= random.randint(1,3)
elif choice == "scissor":
    myNumber= random.randint(1,2)
print(choice)



# user='paper'
# computer = 1
# user='rock'
# computer = 2
# user='scissor'
# computer = 3



if 'p' in user:
    user =int(1)
    print("paper"+str(user))
elif 'ro' in user:
    user =int(2)
    print("rock"+str(user))
elif 's' in user:
    user = int(3)
    print("scissor"+str(user))