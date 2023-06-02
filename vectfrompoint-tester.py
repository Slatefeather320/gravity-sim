from vectfunctionsv5 import *
import pygame
from math import pi
#to test finding of vector between points
window = pygame.display.set_mode((400,400))
pygame.init()
pygame.display.set_caption('Finding Vector Test')
clock = pygame.time.Clock()



o = body(200,200,10,1,(255,255,255),[0,0])
m = body(0,0,10,1,(255,0,255),[0,0])

def pointrender(p):
    pygame.draw.circle(window, p.colour, (p.x, p.y), p.size)

def render():
    window.fill((0,0,0)) #clears screen
    pointrender(o)
    pointrender(m)
    pygame.display.update()

#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    

   #main game loop
   clock.tick(60)
   render()
   mousepos = pygame.mouse.get_pos()
   m.x=mousepos[0]
   m.y=mousepos[1]
   om = vectfrompoints(o,m)
   degrees = om[1]*180/pi
   print(om[0],degrees)