#first let's import random since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building lists to build the deck
#NumberCards is the list to hold numbers plus face cards
numberCards = []
suits = ['h',"d", "c", "♠️"]
royals = ["J", "Q", "K", "A"]
tempPlayer1=[]
tempPlayer2=[]

def TheDeck():
    global counter
    global suits
    global royals
    global numberCards
    global deck
#using loops and append to add our content to numberCards :
for i in range(2,11):
    numberCards.append(str(i))
    #this adds numbers 2-10 and converts them to string data

for j in range(4):
    numberCards.append(royals[j])
    #this will add the card faces to the base list
#Create full deck
for k in range(4):   # four suits
    for l in range(13): #13 cards per suit
        card = (numberCards[l] + " " + suits[k])
        #this makes each card, cycling through suits, but first through faces
        deck.append(card)
        #this adds the information to the "full deck" we want to make
#you can print the deck here, if you want to see how it looks
print(deck)
#now let's see the deck!
counter=0
for row in range(4):
    for col in range(13):
        print(deck[counter], end=" ")
        counter +=1
    print()
#now let's shuffle our deck!
#Shuffle the deck cards
random.shuffle(deck)
player1=[]
player2=[]
# you could print it again here just to see how it shuffle
#loop to devide the cards to each player
for l in range(52):
    if l%2==0:
        player1.append(deck[l])
    else:
        player2.append(deck[l])


print("player1 ",player1)
print()
print("player2 ",player2)
halfDeck=int(len(deck)/2)
plyr1=0
plyr2=0


    #ask user to hit a key to release cards
   
for i in range (0,halfDeck):
    click=input("Press a any key to get cards")
    print("Player 1     Player 2")
    print("     "+player1[i]+"      "+player2[i])
    if player1[i]>player2[i]:
        tempPlayer1.extend(player1[i])
        tempPlayer1.extend(player2[i])
        

    elif player1[i]<player2[i]:
        tempPlayer2.extend(player2[i])
        tempPlayer2.extend(player2[i])
     

    print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))


if len(tempPlayer2==0):
    print("Player one won the game ")
    gameOn=False
elif len(tempPlayer1==0):
    print("Player two won the game ")
    gameOn=False
else:
    
    if len(tempPlayer1)<len(tempPlayer2):
        halfDeck=len(player1)
    elif len(player2)<len(player1):
        halfDeck=len(player2)
    other1=player1[halfDeck: ]
    other2=player2[halfDeck: ]
    print(other1)
    print(player1)
    print(other2)
    print(player2)

    if len(player1)>len(player2):
        tempPlayer1.extend(player1[halfDeck: ])
    elif len(player2)>len(player1):
        

    else:
        for j in range (0,halfDeck):
            player1.pop(0)
            player2.pop(0)
            player1.extend(tempPlayer1)
            player2.extend(tempPlayer2)
            tempPlayer1.clear()
            tempPlayer2.clear()
        
        if len(player1)<len(player2):
            halfDeck=len(player1)
        elif len(player2)<len(player1):
            halfDeck=len(player2)



