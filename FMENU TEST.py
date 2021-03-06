import os, random, time, pygame, math, datetime, sys
from turtle import screensize
os.system('cls')

name=input("What is your name? ")
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size']
sizeList=['1000 x 1000','800 x 800','600 x 600']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HANGMAN')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    print("in instr")
    myFile=open('instructions.txt', 'r')
    yi=150
    stuff= myFile.readlines()


    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\sce.txt','a') #SCORE PATH
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        # temp[j]=stuff[i]
        #     j +=1
        # print(temp)
        # for i in range(N):
        #     text=INST_FNT.render(temp[i], 1, BLACK)
        #     screen.blit(text, (40,yi))
        #     pygame.display.update()
        #     pygame.time.delay(50)
        #     yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
    
def playGame(): # some code from Code IO


    def draw_btns(BUTTONS):
        for button,letter in BUTTONS:
            btn_text = btn_font.render(letter, True, BLACK)
            btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
            pygame.draw.rect(screen, BLACK, button, 2)
            screen.blit(btn_text, btn_text_rect)

        

    def display_guess():
        display_word = ''

        for letter in WORD:
            if letter in GUESSED:
                display_word += f"{letter} "
            else:
                display_word += "_ "

        text = letter_font.render(display_word, True, BLACK)
        screen.blit(text, (400, 200))


    pygame.init()
    WIDTH, HEIGHT = 800, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")

    game_over = False

    # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    # Images
    IMAGES = []
    hangman_satus = 0

    for i in range(7):
        image = pygame.image.load(f"FINAL PROJECT WORK\IMAGES\hangman{i}.png")
        IMAGES.append(image)


    # Buttons
    ROWS = 2
    COLS = 13
    GAP = 20
    SIZE = 40
    BOXES = []

    for row in range(ROWS):
        for col in range(COLS):
            x = ((GAP * col) + GAP) + (SIZE * col)
            y = ((GAP * row) + GAP) + (SIZE * row) + 330
            box = pygame.Rect(x,y,SIZE,SIZE)
            BOXES.append(box)

    A = 65
    BUTTONS = []

    for ind, box in enumerate(BOXES):
        letter = chr(A+ind)
        button = ([box, letter])
        BUTTONS.append(button)

    # Fonts
    btn_font = pygame.font.SysFont('arial', 30)
    letter_font = pygame.font.SysFont('arial', 50)
    game_font = pygame.font.SysFont('arial', 50)

    #WORD
    WordList1 = ["LEBRON","KYRIE","ZION","KAWHI","GIANNIS","NIKOLA","KOBE","SHAQUILLE","DAMIAN",
    "JOEL","LUKA","STEPHEN","KD","BAM"]

    WORD = random.choice(WordList1)

    GUESSED = []

    # Title
    title = "Hangman"
    title_text = game_font.render(title, True, BLACK)
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+10))
    check=True
    while check:   
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm= mouse_pos[0]
                ym= mouse_pos[1]

                for button, letter in BUTTONS:
                    if button.collidepoint(mouse_pos):
                        GUESSED.append(letter)

                        if letter not in WORD:
                            hangman_satus += 1

                        if hangman_satus == 6:
                            game_over = True

                        BUTTONS.remove([button, letter])

        screen.fill(WHITE)
        screen.blit(IMAGES[hangman_satus], (150,100))
        screen.blit(title_text, title_text_rect)
        draw_btns(BUTTONS)
        display_guess()

        # def PlayAgain():
        #     global gameOn
        #     answer=input("DO YOU WANT TO PLAY AGAIN? Y/N")
        #     if "Y" in answer:
        #        Mainmenu()    

        won = True

        for letter in WORD:
            if letter not in GUESSED:
                won = False

        if won:
            game_over = True
            display_text = 'CONGRATS :) PLAY AGAIN ? Y/N' 
            
        
        else:
            display_text = 'SORRY :( PLAY AGAIN ? Y/N'
        

        def PlayAgain():
            global gameOn
            answer=input("DO YOU WANT TO PLAY AGAIN? Y/N")
            if "Y" in answer:
                Mainmenu()    # WILL MAKE MENU FUNCTION

        pygame.display.update()

        if game_over:
            screen.fill(WHITE)
            game_over_text = game_font.render(display_text, True, BLACK)
            game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2))
            screen.blit(game_over_text, game_over_text_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()
    

   
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
    if SETT:
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        screen.fill(background)
        playGame()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
        MAIN=False
        LEV_III=True   
    if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
        MAIN=False
        SCORE=True 
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        c_first=False
        if keys[pygame.K_ESCAPE]:
            c_first=True
            set_first=True
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        keepScore(121)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False 
        pygame.time.delay(3000)
        check=False
    pygame.display.update()
    pygame.time.delay(10)

os.system('cls')
pygame.quit()