#Micah
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
#initialize pygame
import os, random, time, pygame
from sre_constants import JUMP
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
check=True #for the while loop
move=10 #pixels
#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75],'neon green':[127,255,0]}
#Get colors
background= colors.get('pink') #background color
# sq_color=colors.get('aqua') #square color
#Making random color for square

randColosr=''
cr_color=colors.get('white') #circle color
def changeColor():
    global randColors
    colorCheck=True
    while colorCheck:
        randColors=random.choice(list(colors))
        if randColors==background:
            randColors=random.choice(list(colors))
        else:
            colorCheck=False

changeColor()
sq_color=colors.get(randColors)

MAX=10
JumpCount=MAX
JUMP=False
while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    

    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move #substract 5 from the x value
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move
    #Jumping part
    if not JUMP:
        if keys[pygame.K_w] and square.y >=move:
            square.y -= move
        if keys[pygame.K_s] and square.y <HEIGHT-hbox:
            square.y += move 
        # if keys[pygame.K_space]:    
            JUMP=True  
    else:
        if JumpCount >= -MAX:
            square.y -= JumpCount*abs(JumpCount)/2
            JumpCount-=1
        else:
            JumpCount=MAX
            JUMP=False

    if keys[pygame.K_LEFT]  and xc >=rad:
        xc -= move 
    if keys[pygame.K_RIGHT] and xc <WIDTH-rad:
        xc += move
    if keys[pygame.K_UP] and yc >=rad:
        yc -= move
    if keys[pygame.K_DOWN] and yc <HEIGHT-rad:
        yc += move
         
    checkCollide=square.collidepoint((xc,yc))
    if checkCollide:
        square.x=random.randint(wbox, WIDTH-rad)
        square.y=random.randint(hbox, HEIGHT-rad)
        changeColor()
        sq_color=colors.get(randColors)
        rad += move
    
   
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)

    pygame.display.update()
    pygame.time.delay(10)

#move for Square
#Square.x - move = move to left
#Square.x + move = move to right
#Square.y - move = Up 
#Square.y + move = down

#move for circle
#xc - move = left
#xc + move = right
#yc - move = Up
#yc + move= Down 

# x * abs(x)





