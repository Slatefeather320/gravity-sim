from vectfunctionsv5 import *
import pygame
from math import pi
#to test addition of vectors 
window = pygame.display.set_mode((400,400))
pygame.init()
pygame.display.set_caption('Vector Addition Test')
clock = pygame.time.Clock()

v1 = [100,pi/2]
v2 = [100,0]
op = body(200,200,5,1,(255,255,255),[0,0])

def pointrender(p):
    pygame.draw.circle(window, p.colour, (p.x, p.y), p.size)

def render():
    window.fill((0,0,0)) #clears screen
    pointrender(op)
    pointrender(np)
    pointrender(np1)
    pointrender(np2)
    pygame.display.update()

#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   keys = pygame.key.get_pressed()  #checking pressed keys
   if keys[pygame.K_q]:
        v1[1] += 0.06
   if keys[pygame.K_w]:
        v1[1] -= 0.06
   if keys[pygame.K_a]:
        v2[1] += 0.06
   if keys[pygame.K_s]:
        v2[1] -= 0.06
    

   #main game loop
   v = resultant(v1, v2)
   npPos = addvectpoint(op, v)
   npPos1 = addvectpoint(op, v1)
   npPos2 = addvectpoint(op, v2)
   np = body(npPos[0],npPos[1],10,1,(255,0,255),[0,0])
   np1 = body(npPos1[0],npPos1[1],8,1,(255,0,0),[0,0])
   np2 = body(npPos2[0],npPos2[1],8,1,(0,0,255),[0,0])
   clock.tick(60)
   render()
   print((v1[1]%pi)*180/pi,(v2[1]%pi)*180/pi,v[1]*180/pi)