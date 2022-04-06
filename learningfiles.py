#MICAH ROBINSON
#3/29
# LEARNING FILES      OPEN/CREATE FILE,WRITE FILE'w', APPEND'a', READ 'r' close

from mailbox import linesep
import pygame, os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name='Charles'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" " +name+" "+date.strftime('%m/%d/%Y'+'\n')
print(scoreLine)
myFile=open('ClassStuff\sce.txt','w')
myFile.close()


score=345
name='jay'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" " +name+" "+date.strftime('%m/%d/%Y'+'\n')
print(scoreLine)
myFile=open('ClassStuff\sce.txt','a')
myFile.write(scoreLine)
myFile.close()
myFile=open('ClassStuff\sce.txt','r')
lines=myFile.readline()
print(lines)
myFile.close()