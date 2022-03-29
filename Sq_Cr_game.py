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
#Variales
WIDTH=700
HEIGHT=700
wbox=30 
hbox=30
xMs=50
yMs=250

#LIST FOR MESSAGES
MenuList='Instructions', 'ScreenSize', 'Color','Sound','Level','Level2','Level3'
SettingList=['Screen Size','Font size','Color', 'Sound','BC']
#GET COLORS
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75],'neon green':[127,255,0], 'tan':[255,255,224]}
background= colors.get('aqua')
randColosr=''
sqM_color=colors.get('pink') 

#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

def TitleMenu(Message):
    TITLE_FNT=pygame.font.SysFont('comicsans', 80)
    MENU_FNT=pygame.font.SysFont('comicsans', 40)
    INST_FNT=pygame.font.SysFont('times new roman', 30)
    #CREATE TITLE
    text=TITLE_FNT.render('MENU', 1, (255,0,0))
    wind.fill((255,255,255))
    #get width of text
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2 - text.get_width()/2
    wind.blit(text,(xt,50))

#CREATE FIRST BUTTON


#CREATE SQUARE FOR  MENU

squareM=pygame.Rect(xMs,yMs,wbox,hbox)
#this function uses a parameter
def Mainmenu(Mlist):
    txty=248
    squareM.y=250
    for i in range (len(Mlist)):
        message=MenuList[i]
        text=INST_FNT.render(message, 1,(0,255,0))
        wind.blit(text,(90,txty)) 
        pygame.draw.rect(wind,sqM_color,squareM)
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(1000)

# text=INST_FNT.render('Use keys A,W,S,D to move the square, and the arrow keys to move the circle.', 1, (255,0,0))
# text=INST_FNT.render('Chase the square around, and try to cover the square', 1, (255,0,0))
# text=INST_FNT.render('If the square is covered, the circle will then recieve a point, and grow bigger', 1, (255,0,0))
# text=INST_FNT.render('The game will continute until the circle covers the whole screen', 1, (255,0,0))
# wind.blit(text,(220,220))
pygame.display.update()


pygame.time.delay(10000)

























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
background= colors.get('navy') #background color
# sq_color=colors.get('aqua') #square color
#Making random color for square

randColosr=''
cr_color=colors.get('white') #circle color
def changeColor():
    global randColors
    colorCheck=True
    while colorCheck:
        randColors=random.choice(list(colors))
        if colors.get==background:
           print(randColors)
           print(background)
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
    TitleMenu('MENU')
    Mainmenu(MenuList)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    

    keys=pygame.key.get_pressed() #this returns a list
    m
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move #substract 5 from the x value
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move
    if keys[pygame.K_w] and square.y >=move:
            square.y -= move
    if keys[pygame.K_s] and square.y <HEIGHT-hbox:
            square.y += move 
    #     # if keys[pygame.K_space]:    
    #         JUMP=True  
    # else:
    #     if JumpCount >= -MAX:
    #         square.y -= JumpCount*abs(JumpCount)/2
    #         JumpCount-=1
    #     else:
    #         JumpCount=MAX
    #         JUMP=False

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





