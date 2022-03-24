#MICAH ROBINSON
# 3/21/2022

import pygame,time
pygame.init()
wind=pygame.display.set_mode((700,700))
pygame.display.set_caption('testing')

TITLE_FNT=pygame.font.SysFont('comicsans', 20)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('times new roman', 25)
text=TITLE_FNT.render('CIRCLE EATS SQUARE', 1, (255,0,0))
wind.fill((255,255,255))
wind.blit(text,(50,50))
text=INST_FNT.render("Write your instructions", 1,(0,255,0))
text=INST_FNT.render('Use keys A,W,S,D to move the square, and the arrow keys to move the circle.', 1, (255,0,0))
text=INST_FNT.render('Chase the square around, and try to cover the square', 1, (255,0,0))
text=INST_FNT.render('If the square is covered, the circle will then recieve a point, and grow bigger', 1, (255,0,0))
text=INST_FNT.render('The game will continute until the circle covers the whole screen', 1, (255,0,0))
wind.blit(text,(220,220))
pygame.display.update()


pygame.time.delay(10000)