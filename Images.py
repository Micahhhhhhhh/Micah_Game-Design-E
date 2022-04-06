import mailbox
import os, time, random,math
import pygame
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE
#initialize pygame
pygame.init()

# clock = pygame.time.clock()
#variables, constants, and objects
WIDTH=700
HEIGHT=700
x=100
y=15
xc=random.randint(50, WIDTH-50)
yc=random.randint(50,HEIGHT-50)
hbox=20  #height if rect
wbox=20  #width of rect
rad=10    #radius of the circle

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

left = False
right = False
walkcount=0
win = pygame.display.set_mode((500,500))

def redrawGameWindow():
    global walkcount
    win.blit(bg, (0,0))
if walkcount + 1 >=27:
    walkCount = 0

if left:
    win.blit(walkLeft[walkcount//3, (x,y)])
    walkcount += 1
elif right:
    win.blit(walkRight[walkcount//3, (x,y)])
    walkcount += 1 
else:
    win.blit(char, (x,y))
pygame.display.update()


#inscribe square
ibox=rad*math.sqrt(2)
xi= xc-ibox/2
yi= yc-ibox/2
inscSq=pygame.Rect(xi,yi, ibox,ibox)
bg=pygame.image.load('bgSmaller.jpg')
man=pygame.image.load('standing.png')

manX=0
manY=HEIGHT-64
check=True
manSquare=pygame.Rect(manX,manY,64,64)
boulder = pygame.Rect(230,270,180,345) 
square=pygame.Rect(x,y,wbox,hbox)

JUMP=False
#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#define colors Dictionary dictio={key: values}
colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229]}
#calling values from a dictionaty get('key')
background=colors.get('white')
cr_color=colors.get('mag')
#Create a sqaure rand color 
#sq_color=colors.get('aqua')
blColor=colors.get('aqua')
randColor=''
def changeClr():
    print(background)
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        print("rand Clr = ", randColor)
        if colors.get(randColor)  == background:
            print("backgrnd = randclr")
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
sq_color=colors.get(randColor)    

pygame.display.set_caption("Circle eats Square")
jumpCount=7
COUNT=7
impact=False
while check:
    move=10
    crash=boulder.colliderect(manSquare)
    if crash:
        impact = True
    else:
        impact=False

    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() # this is a list
    print(impact)
    if case.type==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
    #Square Moves
    if keys[pygame.K_a] and manX>=move:
        square.x -= move
        left = True
        right = False
        # if not impact:
        manX -= move
        manSquare.x -= move
    elif keys[pygame.K_d] and manX<WIDTH-wbox:
        square.x += move
        right = True
        left =False
    else:
        right= False
        left = False
        walkcount = 0 
        if not impact:
            manX += move
            manSquare.x += move
    #JUMP CODE
    if not JUMP:
        # if keys[p.K_s]:
        #     square.y += move
        #     if not impact:
        #         manY += move
        #         manSquare.y += move
        # if keys[p.K_w]:
        #     square.y -= move
        #     if not impact:
        #         manY -= move
        #         manSquare.y -= move
        if keys[pygame.K_SPACE]:
            JUMP=True
            right = False
            left = False
            walkcount = 0
    else:
        if jumpCount >= -COUNT:
            square.y -= jumpCount*abs(jumpCount)/2
            manY -= jumpCount*abs(jumpCount)/2
            manSquare.y -= jumpCount*abs(jumpCount)/2
            jumpCount -=1
        else:
            jumpCount=COUNT
            JUMP=False
        redrawGameWindow()
    
    #circle moves
    if keys[pygame.K_LEFT] and xc > move:
        xc -= move
        inscSq.x -= move
    if keys[pygame.K_RIGHT] and xc <WIDTH-(rad+move):
        xc += move
        inscSq.x += move
    if keys[pygame.K_DOWN] and yc <HEIGHT-(rad+move):
        yc += move
        inscSq.y += move
    if keys[pygame.K_UP] and yc > move:
        yc -= move
        inscSq.y -= move

   # choque=square.collidepoint((xc,yc))
    choque=square.colliderect(inscSq )
    if choque:
        square.x=random.randint(50, WIDTH-50)
        square.y=random.randint(50,HEIGHT-50)
        changeClr()
        sq_color=colors.get(randColor)    

        rad +=move
        ibox=rad*math.sqrt(2)
        xi= xc-ibox/2
        yi= yc-ibox/2
        inscSq=pygame.Rect(xi,yi, ibox,ibox)
    #Check clide between the man and the bulder
    
    

    pygame.draw.rect(screen,1,manSquare)
    pygame.draw.rect(screen,blColor, boulder)
    screen.blit(bg,(0,0))
    screen.blit(man,(manX,manY))
    pygame.draw.rect(screen,sq_color, square)
    pygame.draw.rect(screen,cr_color,inscSq)
    pygame.draw.circle(screen,cr_color,(xc,yc), rad )
    pygame.display.update()
    pygame.time.delay(30)