import pygame , os
import sys
import random
os.system('cls')

# code from Code IO


def draw_btns(BUTTONS):    #Creates buttons
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


# Buttons /// spacing and placing of boxes
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
WordList1 = ['CLIPPERS','LAKERS','CELTICS','MAVERICKS',"SUNS",'SPURS',"WARRIORS","GRIZZLIES","WIZARDS","ROCKETS","HEAT","JAZZ","PELICANS","NUGGETS","MAGIC",'BUCKS',"NETS",'BULLS',"KNICKS","KINGS","THUNDER",
'COWBOYS','JETS','GIANTS',"RAMS","BEARS","VIKINGS","PACKERS","PANTHERS","JAGUARS","TITANS","BENGALS","EAGLES","STEELERS","CHEIFS","PATRIOTS",'BILLS',"BRONCOS",'RAVENS','LIONS']
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