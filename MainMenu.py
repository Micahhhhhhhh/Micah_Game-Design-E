#Micah Robinson 3/23/22
#Main menu for the game / creating functions for menu
import pygame,time
pygame.init()
#Variales
WIDTH=700
HEIGHT=700
wbox=30
hbox=30
xs=50
ys=250

#LIST FOR MESSAGES
MenuList='Instructions', 'ScreenSize', 'Color','Sound','Level','Level2','Level3'

#GET COLORS
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75],'neon green':[127,255,0]}
background= colors.get('pink')
randColosr=''
sq_color=colors.get('pink') 

#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

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

square=pygame.Rect(xs,ys,wbox,hbox)
txty=248
for i in range (7):
    message=MenuList[i]
    text=INST_FNT.render(message, 1,(0,255,0))
    wind.blit(text,(90,txty)) 
    pygame.draw.rect(wind,sq_color,square)
    square.y +=50
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