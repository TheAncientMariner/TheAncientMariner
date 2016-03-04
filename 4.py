
import random
import time
import turtle
t = turtle.Pen()



from turtle import * 
from Tkinter import *

"""BACKGROUND EIKONA"""
screen = turtle.Screen()

#I eikona pano stin opoia sxediazonte oi kikloi prepei einai 1024x1024 opos zitaei i ekfonisi
screen.setup(1024, 1024)

screen.bgpic("BATMAN.GIF")

def empty(value):
    try:
        value = float(value)
    except ValueError:
        pass
    return bool(value)


"""Kikloi pou temnonte"""	
def TemKikloi(centerX1, centerY1, radius1, centerX2, centerY2, radius2,tk):
	
		distanceSquared=(centerX1-centerX2)**2+(centerY1-centerY2)**2
		distance=pow(distanceSquared, 0.5)
		if distance<radius1+radius2:
			tk = tk + 1
			return tk
			

	
circlecor= None
my_x = [0]*20
my_y = [0]*20
x = [0]*20


count = 0
"""SXEDIASMOS TON 20 TIXAION KIKLON"""
for i in range(0, 20):
	my_x[i] = t.xcor()
	my_y[i] = t.ycor()
	
	t.color("white")
	x[i] = random.randint(10,500)  #Aktina me tixaia timi apo 10-500
	t.circle(x[i]) 
	
	
	t.up()
	
	y = random.randint(0,360)
	t.seth(y) 
	
	if t.xcor() < -300 or t.xcor() > 300:
		t.goto(0, 0) # this is the center 
	elif t.ycor() < -300 or t.ycor() > 300:
		t.goto(0, 0) # this is the center 
	z = random.randint(0,100)
	

	t.forward(z) 
	t.down() 

	
	
	
	circleinfo={my_x[i],my_y[i],x[i]}
	
	if  circlecor==None:
		circlescor = circleinfo
	else:
		circlescor.append(circleinfo)
		
	count = TemKikloi(my_x[i-1],my_y[i-1],x[i-1],my_x[i],my_y[i],x[i],count)
	
	
time.sleep(1)

print "TEMNONTE %d KIKLOI" %count

time.sleep(1)

"""EMFANISI EIKONAS"""
import pygame 
from pygame.locals import *


pygame.init()

size = [1280 , 720]

screen = pygame.display.set_mode((1600,1200),0,32)

background = pygame.image.load("BATMAN.GIF")

while True:
	screen.blit(background, (0,0))
	
	pygame.display.update()






