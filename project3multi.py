from vectfunctionsv5 import *
from math import pi
import pygame

#Version 3: works with vectfunc library v5 : has camera controls and axis lines 11/1/22

window = pygame.display.set_mode((1000,700))
pygame.init()
pygame.display.set_caption('Project Draft 3: N-Body System')
clock = pygame.time.Clock()

#camera offsets
camx = 0
camy = 0
camSpeed = 1

#axis lines
xaxis = 350
yaxis = 500

earth = body(500,350,50,50,(0,0,255),[0.02,-pi/2]) 
moon = body(600,350,17,1,(100,100,140),[1.2,pi/2])
red = body(300,350,10,0.0005,(244,100,90),[1,-pi/2])

bodies = [earth, moon, red]

def physics():
    G = 6
    for b1 in bodies:
        for b2 in bodies:
            if b2==b1:
                pass
            else:
                updatepos(b1)
                distvect = vectfrompoints(b1, b2)
                acc = [G*b2.mass/ distvect[0]**2 , distvect[1]]
                b1.v = resultant(acc, b1.v)


def pointrender(p):
    pygame.draw.circle(window, p.colour, (p.x + camx, p.y + camy), p.size) 

def draw():
     window.fill((0,0,0)) #clears screen
     pygame.draw.line(window,(100,0,0),(0,xaxis + camy),(1000,xaxis + camy))
     pygame.draw.line(window,(0,0,100),(yaxis + camx,0),(yaxis + camx, 700))
     for b in bodies:
        pointrender(b)
     pygame.display.update()
     
#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   keys = pygame.key.get_pressed()  #checking pressed keys
   if keys[pygame.K_RIGHT]:
        camx -= camSpeed
   if keys[pygame.K_LEFT]:
        camx += camSpeed
   if keys[pygame.K_UP]:
        camy += camSpeed
   if keys[pygame.K_DOWN]:
        camy -= camSpeed   


   #main game loop
   clock.tick(300)
   draw()
   physics()



