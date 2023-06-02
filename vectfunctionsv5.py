import math
pi = math.pi
#library used in project Version 5 11/1/22
class body:
    def __init__(self,x,y,size,mass,colour,v):
        self.x = x
        self.y = y
        self.size = size
        self.mass = mass
        self.colour = colour
        self.v = v


def resultant(v1,v2): #works TESTED 
    v1x = (v1[0])*(math.cos(v1[1]))
    v1y = (v1[0])*(math.sin(v1[1]))
    v2x = (v2[0])*(math.cos(v2[1]))
    v2y = (v2[0])*(math.sin(v2[1]))

    rx = v1x + v2x
    ry = v1y + v2y

    rmag = ((rx**2) + (ry**2))**(1/2) #find magnitude of r
    rdir = math.atan(ry/rx)
    if rx<0:
        rdir += pi
    return rmag, rdir

def vectfrompoints(p1,p2):
    delx = p2.x - p1.x #finds delta x
    dely = p2.y - p1.y #finds delta y

    m = (delx**2 + dely**2)**(1/2)
    if delx == 0:
        if dely == 0:
            d = 0
        if dely<0:
            d = -pi/2
        if dely>0:
            d = pi/2
    else:
        d = (math.atan(dely/delx))
    if delx<0:
        d+=pi
    return m, d

def addvectpoint(p,v1): #works TESTED
    v1x = (v1[0])*(math.cos(v1[1]))
    v1y = (v1[0])*(math.sin(v1[1]))
    x = p.x+v1x
    y = p.y+v1y
    return [x,y]

def updatepos(p): #works TESTED
    newp = addvectpoint(p, p.v)
    p.x = newp[0]
    p.y = newp[1]
