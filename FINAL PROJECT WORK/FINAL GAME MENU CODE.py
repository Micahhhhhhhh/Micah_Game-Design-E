#Micah Robinson 4/14/2022
# Sports Hangman game
#Create Menu that will have PlayGame, and Settings button
# Setting button will allow User to change screen size and Background image
#Playgame button will then lead user to screen where they will select the level they wish to play
# Level 1 = NBA Players
# Level 2 = NFL Players
# Level 3 = NFL/NBA Teams
# File or List with 3, 6, and 12 letter words
# Need 9 different background images... 3 options per level
# User will select level and silhuoette of word will appear
# user will then start guessing thw word
# user will have toltal 5 guesses for every level.... Head, Arm, Arm, Leg, Leg
# for Level 3, User will have 8 guesses ... Head, Arm, Arm, Leg, Leg, Eye, Eye, Smile
# lenWord * 5 - Guesses for scoring 
#after user either fails, or guesses the word, they will have the option to either leave (ESC) back to menu, or play again



import os , pygame , random , time
os.system('cls')

#LIST FOR WORDS
WordList1 = ["lebron james","james harden","kyrie irving",'giannis antetokounmpo','luka doncic','kevin durant','trae young','jayson tatum','bradley beal','anthony davis',
'carmelo anthony','stephen curry','damien lillard','darius garland','tyrese maxey','joel embiid','demar derozan','brandon ingram']
WordList2 = ['lamar jackson','patrick mahomes','cam newton','justin jefferson','stephon diggs','dak prescott','ceedee lamb','micah parsons','tom brady','mike evans'
'derrick henry','julio jones','jamarr chase','aaron donald','cooper cupp','odell beckam jr','saquon barkley','trevon diggs','jalen ramsey','kyler murray','deandre hopkins','myles garret','deshaun watson']
WordList3 = ["la lakers",'la clippers','boston celtics','golden state warriors','brooklyn nets','ny knicks','portland trailbrazers','dallas mavericks','utah jazz','miami heat','washington wizards',
'dallas cowboys','ny giants','carolina panthers','baltimore ravens','arizona cardinals','ne patirots','lv raiders','la rams','gb packers','kc cheifs','denver broncos',' chicago bears','buffalo bills',' seattle seahawks','miami dolphins','detroit lions'
'pittsburgh steelers']
#LISTS FOR MENU
MList = 'Instructions','Settings','Level 1 (NBA)','Level 2(NFL)','Level 3 (NBA/NFL)'
SettingsList='Screen Size','Background Image'
sizeList=['1000 x 1000','800 x 800','600 x 600']

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
sqM_color=colors.get('pink')



name=input("What is your name? ")
pygame.init()


#VARIABLES FOR SCREEN
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30


#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HANGMAN GAME')


#FNT FOR MENU
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#CREATE TITLE
text=TITLE_FNT.render('HANGMAN GAME', 1, (255,0,0))
wind.fill((255,255,255))
#WIDTH OF TEXT
xt=WIDTH/2 - text.get_width()/2
wind.blit(text,(xt,50))

squareM=pygame.Rect(xMs,yMs,wb,hb)
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(255,0,0))
        wind.blit(text,(90,txty))
        pygame.draw.rect(wind,sqM_color, squareM)
        squareM.y +=50
        txty+=50
pygame.display.update()
pygame.time.delay(100000)





