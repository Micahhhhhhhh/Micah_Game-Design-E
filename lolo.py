#Micah Robinson
#learning how to draw circles and squares and rectangles
#use keys to move object
#using dictionaries


#objective of the game is for the rect to run away from the circle, if they collide the circle eats the saquare
#circle will get larger and a new rectangle should appear somewhere on the screen

import os, random, time, pygame
#initialize pygame
pygame.init()

#declare constants, variables, list, dictiornaries, any object

WIDTH=700
HEIGHT=700
xs=20
ys=20
wbox=30
hbox=30
rad=15
xc=random.randint(rad,WIDTH-rad)
yc=random.randint(rad,HEIGHT-rad)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153,255], 'orange':[255,85,0], 'purple':[48,25,52],
'navy':[5,31,64], 'pink':[200,3,75]}

#Get colors
background= colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')

screen.fill(background)
pygame.draw.rect(screen, sq_color, square)
pygame.draw.circle(screen, cr_color, (xc,yc), rad)

pygame.display.update()
pygame.time.delay(1000)