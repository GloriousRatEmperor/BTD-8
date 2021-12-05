import pyglet
import numpy as np
import random
import pygame
import math
import os
import time
from pyglet.window import key
from pyglet.window import Window
from pyglet.gl import *
from pygame.locals import *
from PodSixNet.Connection import connection, ConnectionListener

with open("ip.txt", "r") as ip:
    ipadress=ip.read()

connection.DoConnect((ipadress, 5071))
class MyNetworkListener(ConnectionListener):

    def Network(self, data):
        pass
    def Network_gitplayer(self,data):
        global me
        if data["id"]<3:
            me=player(data["id"])
        else:
            uu=1/0
    def Network_ugotbloonsmon(self,data):
        sendbloon(data["takedis"])
nwl = MyNetworkListener()



pygame.init()
class player(object):
    def __init__(self,ID):
        self.ID=ID
connection.Send({"action":"start","id":888690420})
# r = requests.post('http://' + ipadress + ':5000/AuctionPrice', headers=headers,
#                   data=j
# r = requests.get(f'http://{ipadress}:5000/start')
# me = jsonpickle.decode(r.text)
def loadify(imgname):
    return pygame.image.load(f"imagesboom/{imgname}.png").convert_alpha()
def loadanimation(foldername,imgname):
    return pygame.image.load(f"imagesboom/boom/{foldername}/{imgname}.png").convert_alpha()
font = pygame.font.Font('freesansbold.ttf',25)
fint = pygame.font.Font('freesansbold.ttf',150)
finter = pygame.font.Font('freesansbold.ttf',48)
flont = pygame.font.Font('freesansbold.ttf',80)
flint = pygame.font.Font('freesansbold.ttf',30)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("BTD Battles 8")
icon = loadify('drtmonk')
pygame.display.set_icon(icon)
running = True
XX = 0
PXSPD=0
PYSPD=0
YY = 0
growbloon=[]
money=50
pas=time.time()
bloons=[]
lvlup = []
monks = []
animations=[]
bomb=loadify('bomb')
gunners=[]
enginer=loadify('engineer')
gunI=loadify('guner')
wata=loadify('water')
blns=[]
mines=[]
murder=[]
sqares=[]
sqaresize=100
x=int(sqaresize/2)
y=int(sqaresize/2)
for e in range(400):
    sqares.append([])
    x+=sqaresize
    if x>w:
        x=sqaresize/2
        y+=sqaresize
maxsqare=19
sqaresa=[[g for g in e] for e in sqares]
sqaresb=[[g for g in e] for e in sqares]
sqares2=[[g for g in e] for e in sqares]

class drtmonkey(pygame.sprite.Sprite):
    def __init__(self,X,Y,I,f,F,DS,H,c,ID,LS,P,SPE,dmg=1):
        super(drtmonkey, self).__init__()
        if LS==-10:
            monks.append(self)
            self.price = 20
            #self.price = 31+int(DS / 3) - int(c / 10)
        else:
            if I==wata:
                self.rot=7
            else:
                self.rot=F*2+1
            #if F>0:
                #self.Q=0.5
            #else:
                #self.Q=1
        self.Q=1
        self.MID=1
        self.LS=LS
        self.dmg=dmg
        self.ID=ID
        self.H=H
        self.c=c
        self.DS=DS
        self.C=ti
        self.I=I
        self.f=f
        self.SPE=SPE
        self.F=F
        self.X=X
        self.Y=Y
        self.P=P
        
class gunner(pygame.sprite.Sprite):
    def __init__(self,X,Y,I,f,F,DS,c,ID,H,P,SPE):
        super(gunner, self).__init__()
        monks.append(self)
        self.c=c
        self.dmg=1
        self.MID=4
        self.price = 225
        self.H=H
        self.ID=ID
        self.DS=DS
        self.C=ti
        self.I=gunI
        self.IB=I
        self.f=f
        self.SPE=SPE
        self.F=F
        self.X=X
        self.Y=Y
        self.P=P
        self.EX=0
        self.EY=0


class factory(pygame.sprite.Sprite):
    def __init__(self,X,Y,I,f,F,H,c,ID,LS,P):
        self.spikeX=[]
        self.spikeY=[]
        self.X=X
        self.Y=Y
        self.price = 90
        self.SPE=[0,0]
        super(factory, self).__init__()
        monks.append(self)
        for i in range (len(tracX)):
            if distanceB(tracX[i], tracY[i],self.X+60,self.Y+60,100):
                self.spikeX.append(tracX[i])
                self.spikeY.append(tracY[i])
        gobl=10000
        for i in range (int((len(blntrac))/2)):
            if i>0:
                if distanceC(blntrac[i*2-2], blntrac[i*2-1],self.X+60,self.Y+60)<gobl:
                    numba=i*2-1
                    gobl=distanceC(blntrac[i*2-2], blntrac[i*2-1],self.X+60,self.Y+60)
        self.tracpos=numba
        self.MID=3
        self.ID=ID
        self.H=H
        self.LS=LS
        self.c=c
        self.G=100000000
        self.C=ti
        self.I=I
        self.f=f
        self.F=F
        self.P=P
class Image(pygame.sprite.Sprite):
    def __init__(self, I,X,Y):
        self.I=I
        self.x = X
        self.y = Y
class engin(pygame.sprite.Sprite):
    def __init__(self,X,Y,I,f,F,DS,H,c,MI,MC,ID,LS,P,SPE):
        super(engin, self).__init__()
        monks.append(self)
        self.SPE=SPE
        self.price = 69
        self.MID=2
        self.ID=ID
        self.MC=MC
        self.MI=MI        
        self.LS=LS
        self.ID=ID
        self.H=H
        self.c=c
        self.DS=DS
        self.C=ti
        self.I=I
        self.f=f
        self.F=F
        self.X=X
        self.Y=Y
        self.P=P
ball=loadify("druidball")
druidart=[]
class Drt(pygame.sprite.Sprite):
    def __init__(self,X,Y,S,s,I,H,x,y,P,SPE,DMG=1,bounce=0):
        super(Drt, self).__init__()
        self.x=0
        self.dmg=DMG
        self.b=bounce
        self.y=0
        self.SPE=SPE
        self.IM=0
        self.I=I
        if xS==0:
            spdx=b.DS
            spdy=0
        else:
            spdx=b.DS/math.sqrt(yS**2/xS**2+1)
            if xS<0:
                spdx*=-1
            spdy=spdx*yS/xS
        if spdx==0:
            if spdy<0:
                self.a=pygame.transform.rotate(self.I,-90)
            else:
                 self.a=pygame.transform.rotate(self.I,90)
        elif spdx>0:
            self.a=pygame.transform.rotate(self.I,-math.atan(spdy/spdx)*180/math.pi)
        else:
            self.a=pygame.transform.rotate(self.I,180-math.atan(spdy/spdx)*180/math.pi)
        self.ss = pygame.Surface.get_size(self.a)
        self.I=self.a
        self.s=s
        self.S=S
        self.H=H
        self.X=X
        self.pierce=[1,1]
        self.Y=Y
        self.P=P
        self.siz=(self.ss[0]+self.ss[1])/5
        self.V=int(self.ss[0]/2)
        self.C=int(self.ss[1]/2)
    def special(self,loss):
        for c in range(len(self.SPE)//2):
            if self.SPE[c*2-2]==1:
                if loss.ID>-10:
                    loss.f-=self.SPE[c*2-1]*2
                    if loss.f<1:
                        loss.f=1
                    loss.SY=0
                else:
                    if loss.IM==0:
                        loss.SX/=self.SPE[c*2-1]+1
                        loss.SY/=self.SPE[c*2-1]+1
                        loss.IM=1
            elif self.SPE[c*2-2]==2:
                print(self.SPE[c*2-1],self.SPE[c*2-2])
                if self.pierce[0]<1:
                    if self.H>1:
                        xplosions.append(explode(self.X,self.Y,self.a,self.D[1]/7*30,10.73/self.D[1]*self.SPE[c*2-1],0))
                        if self.SPE[c*2-1]>1:
                            self.a=pygame.transform.smoothscale(self.I,(int(self.ss[0]*self.SPE[c*2-1]),int(self.ss[1]*self.SPE[c*2-1])))
                            self.ss=self.ss = pygame.Surface.get_size(self.a)
                            self.pierce[1]+=1
                            self.dmg+=2
                        self.pierce[0]=self.pierce[1]
                        drts.remove(self)
                        druidart.append(self)
                        self.D[0]=ti
                else:
                    self.pierce[0]-=1
                    self.H+=1
            elif self.SPE[c*2-2]==3:
                if loss not in thorned and loss.ID>-9:
                    thorned.append(loss)
                    loss.spawn=[]
                    loss.SY/=loss.S*10
                    loss.SX /=loss.S*10
                    loss.S = 0.1
            # if ti % 7 == 0:
            #     for e in xplosions:
            #         e.t += 30
            #         e.I = pygame.transform.scale(e.i, (int((e.t * 3 + e.Start) * e.S), int((e.t * 3 + e.Start) * e.S)))
            #         e.s = pygame.Surface.get_size(e.I)
            #         if e.t > e.T:
            #             xplosions.remove(e)
            #             e.kill()
            #             del e

minemine=loadify('supermine')
class mine(pygame.sprite.Sprite):
    def __init__(self,X,Y,S,s,H,x,y,P,LS,SPE,dmg):
        super(mine, self).__init__()
        global minemine
        mines.append(self)
        self.I=minemine
        self.dmg=dmg
        self.a=pygame.transform.rotate(self.I,random.randint(-180,180))
        self.x=0
        self.y=0
        self.s=s
        self.LS=LS
        self.S=S
        self.ss = pygame.Surface.get_size(self.I)
        self.H=H
        self.SPE=SPE
        self.X=X
        self.Y=Y
        self.P=P
        ss=pygame.Surface.get_size(self.a)
        self.siz=(ss[0]+ss[1])/5
        self.V=int(ss[0]/2)
        self.C=int(ss[1]/2)
    def special(self,loss):
        pass
class Drt2(pygame.sprite.Sprite):
    def __init__(self,X,Y,I,H,LS,PR,CR,f,P,dmg=1):
        super(Drt2, self).__init__()
        self.CR=CR
        self.PR=PR
        self.dmg=dmg
        self.f=f
        self.P=P
        self.I=I
        self.a=self.I
        self.LS=LS
        self.H=H
        self.ss=pygame.Surface.get_size(self.a)
        self.X=X
        self.Y=Y
        if self.PR<1:
            self.x=X
            self.y=Y
        else:
            self.x=X-35
            self.y=Y-35
        self.a=pygame.transform.rotate(self.I,random.randint(0,1800)/math.pi)
yeano=1
rndbloon=[]

class Bloon(pygame.sprite.Sprite):
    def __init__(self,X,Y,S,H,f,r,ID,h,HH,spawn=[],armr=0,EY=0,sent=0):
        super(Bloon, self).__init__()
        global power,POWER,yeano
        blns.append(self)
        self.n=blntrac
        self.armr=armr
        self.EX=0
        self.made=sent
        if sent==0:
            rndbloon.append(self)
        self.spawn=spawn
        self.EY=EY
        self.ID=ID
        self.H=H
        self.r=r
        # if self.ID==-8:
        #     #force.append(self)
        #     self.PO=[POWER,POWER]
        #     self.po=[power,0]
        #     self.I=spe[2]
        #     self.ID=-3
        #     self.r=0
        self.h = h
        self.HH = HH
        if self.r>0:
            growbloon.append(self)
            if self.ID>-1:
                self.i=B
                self.I=self.i[self.H-1]
            elif self.ID==-1:
                self.I=spe[1]
            elif -1>self.ID>-7:
                self.i = B
                self.I=B[-self.ID+3]
        elif self.ID>-1:
                self.i=[e for e in A]
                self.I=self.i[self.H-1]
        elif self.ID==-1:
            self.I=spe[0]
        elif self.ID==-10:
            self.I=bossI
            self.img=bossI
        elif -1>self.ID>-7:
            self.I=A[-self.ID+3]
        elif self.ID == -11:
            self.I=boss2
            self.img = boss2
        self.X=X
        self.Y=Y
        self.f=f
        ss=pygame.Surface.get_size(self.I)
        self.s = pygame.Surface.get_size(self.I)
        self.siz=(ss[0]+ss[1])/4
        self.T=(ss[0]/2)
        self.R=(ss[1]/2)
        self.f=f
        self.x=-50
        self.y=50
        self.SX=0
        self.SY=0
        self.S=S
        self.q=self.I
    def hploss(self,loss):
        global hploss,money,rel,POWER,power
        if self.ID==1:
            self.H-=loss
            self.HH-=loss
            if self.H<1:
                 murder.append(self)
                 rel=0
            else:
                self.SX/=self.S
                self.SY/=self.S
                self.S = speed(self.H)/5
                self.SX*=self.S
                self.SY*=self.S
                self.I = self.i[self.H-1]
        else:
            self.H-=loss
            if self.H<1:
                 if not self.spawn==[]:
                     for c in self.spawn:
                         for e in range(c[0]):
                             self.make(c[1],self.H)
                 murder.append(self)
                 rel=0
            # elif self.ID>0:
            #     self.SX/=self.S
            #     self.SY/=self.S
            #     self.S = speed(self.H)/5
            #     self.SX*=self.S
            #     self.SY*=self.S
            #     self.I = self.i[self.H-1]
    def make(self,which,overkill):
        if which+overkill>-1:
            bloonlistdingus = [[2, 1, 1, 1, []], [4, 2, 2, 1, []], [6, 3, 3, 1, []], [8, 4, 4, 1, []], [10, 5, 5, 1, []],
                       [0, 1, 6, -2, [[2, 4]]], [9, 4, 7, -3, [[1, 5], [1, 8]]], [10, 5, 8, -4, [[1, 5], [4, 2]]],
                       [15, int(6 + rn / 10), int(6 + rn / 10), -1, []],
                       [10, 20, 9, -5, [[5, 5]]],[7, int(20 + rn / 12), 10,-6,[[4,9]],2], [16, rn + 65, 0, -11, [[4, 9]]],
                       [3, rn * 3 + 120, 0, -10, [[4, 11]]] ]

            what=bloonlistdingus[which]
            if what[3] > -10:
                what[0] += min(rn, 60) / 5
            # what = [speed,health,HH(wierdhelf),ID,spawn,EX,EY]

            if len(what)>5:
                armour = what[5]
            else:
                armour = 0
            newbloon=Bloon(self.X +random.randint(-70,70), self.Y+random.randint(-70,70), (what[0])/5
                                , what[1], self.f
                                , self.r, what[3], self.h,what[2],what[4], armour, 0,self.made)
            bloons.append(newbloon)
            if overkill<0:
                newbloon.hploss(-overkill)
    def grow(e,howmuch=1):
        if e not in murder:
            if e.HH < e.h:
                e.HH += min(howmuch,e.h-e.HH)
                if e.HH>5 and not e.ID==-1:
                    forms = [[0, 1, -2, [[2,4]]], [9, 4, -3, [[1, 5], [1, 8]]], [10, 5, -4, [[1, 5], [4, 2]]],
                             [10, 20, -5, [[5, 5]]],[7, int(30 + rn / 8), -6,[[4,9]],1]]

                    if e.HH > 6:
                        e.HH = e.h
                    form = forms[e.HH-6]
                    e.ID=form[2]
                    e.spawn=form[3]
                    e.H= form[1]
                    e.SX /= e.S
                    e.SY /= e.S
                    e.S = (form[0]+rn/5)/5
                    e.SX *= e.S
                    e.SY *= e.S
                    e.I = B[e.HH-1]
                    if len(form)>4:
                        e.armr = form[4]
                            # if e.h == 13:
                            #     e.ID = -3
                            #     e.H = 4
                            #     e.spawn = [[1, 1], [4, 5]]
                            #     e.I = B[6]
                            # elif e.h < 15:
                            #     e.ID = -4
                            #     e.H = 5
                            #     e.spawn = [[1, 1], [1, 4]]
                            #     e.I = B[7]
                            # else:
                            #     e.ID = -5
                            #     e.H = 20
                            #     e.spawn = [[5, 1]]
                            #     e.I = B[8].S

                elif e.ID>0:
                    e.H=e.HH
                    e.I = e.i[e.H - 1]
                    e.SX /= e.S
                    e.SY /= e.S
                    e.S = speed(e.H) / 5
                    e.SX *= e.S
                    e.SY *= e.S
                else:
                    e.H = e.HH

class explode(pygame.sprite.Sprite):
    def __init__(self,X,Y,i,T,howfast=1,strt=60):
        super(explode, self).__init__()
        self.i = i
        for e in range(3):
            if e==i:
                self.i=explod[i][0]
                animations.append(self)
                self.ii=explod[i]
                self.faze=0

        self.X=X+30
        self.Start=strt
        self.Y=Y+30
        self.T=T
        self.S = howfast
        self.s=pygame.Surface.get_size(self.i)
        self.I=loadify('noth')
        self.t=0
druids=[]
class Druid(pygame.sprite.Sprite):
    def __init__(self,X,Y,I,f,F,DS,c,timebetweenhits,SPE):
        super(Druid, self).__init__()
        monks.append(self)
        self.MID=5
        self.c=c
        self.DS=DS
        self.C=ti
        self.bounce=0
        self.price = 45
        self.D=timebetweenhits
        self.I=I
        self.f=f
        self.price=40
        self.SPE=SPE
        self.F=F
        self.X=X
        self.Y=Y
        self.ID =loadify("druidball")
        self.H=1
        self.P = [0]
        self.dmg = 3


def drtM():
    rel=0
    for e in drts:
        e.X+=e.S
        e.Y+=e.s
        e.x=int(e.X)
        e.y=int(e.Y)

        sqares2[int((e.X + e.ss[0]) // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(e)
        if e not in sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)]:
            sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
        if e not in sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)]:
            sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
        if e not in sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)]:
            sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(e)
        if not 0<e.X<1800+e.ss[0]/2:
            if e.b<1:
                e.kill()
                drts.remove(e)
                del e
            else:
                e.b -= 1
                e.S*=-1
        elif not 0<e.Y<1200+e.ss[1]/2:
            if e.b < 1:
                e.kill()
                drts.remove(e)
                del e
            else:
                e.b-=1
                e.s*=-1
def moida():
    global money,income,rn,locked
    for b in range (len(murder)):
         e=murder[0]
         murder.remove(e)
         if e in blns:
             blns.remove(e)
             bloons.remove(e)
             if e in rndbloon:
                rndbloon.remove(e)
                if rndbloon == []:
                    money+=income
                    rn+=1
                    locked+=1
                    ready()
             if e in thorned:
                 thorned.remove(e)
             if e in force:
                 force.remove(e)
             if e in growbloon:
                 growbloon.remove(e)
         e.kill()
nspd=0
nespd=0
newspd=0
spe=[loadify('purple'),loadify('regpur'),loadify('blnSHA'),loadify('blnSH')]
health=100
ss=0
SS=0
def blnM():
    global health,bloon,blns,drts2, sqares,Bloondamage
    for e in blns:
        if e.SY==0:
            e.IM=0
            e.SY=0
            e.SX=0
            xS= e.n[e.f-1]-e.X
            yS=e.n[e.f]-e.Y
            if xS==0:
                e.SX=e.S
                e.SY=0
            else:
                e.SX=e.S/math.sqrt(yS**2/xS**2+1)
                if xS<0:
                    e.SX*=-1
                e.SY=e.SX*yS/xS
            if e.ID<-9:
                if e.SX==0:
                    if e.SY<0:
                        e.I=pygame.transform.rotate(e.img,-90)
                    else:
                         e.I=pygame.transform.rotate(e.img,90)
                elif e.SX>0:
                    e.I=pygame.transform.rotate(e.img,-math.atan(e.SY/e.SX)*180/math.pi)
                else:
                    e.I=pygame.transform.rotate(e.img,180-math.atan(e.SY/e.SX)*180/math.pi)
                ss=pygame.Surface.get_size(e.I)
                e.EX=int(ss[0]/2)
                e.EY=int(ss[1]/2)
                e.T=0
                e.R=0

        e.X+=e.SX
        e.Y+=e.SY
        e.x=int(e.X)
        e.y=int(e.Y)
        if e not in drts2:
            if e.X>0:
                sqares[int((e.X + e.s[0]) // sqaresize + (e.Y + e.s[1]) // sqaresize * maxsqare)].append(e)
                if e not in sqares[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)]:
                    sqares[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
                if e not in sqares[int((e.X + e.s[0]) // sqaresize + e.Y // sqaresize * maxsqare)]:
                    sqares[int((e.X + e.s[0]) // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
                if e not in sqares[int(e.X // sqaresize + (e.Y + e.s[1]) // sqaresize * maxsqare)]:
                    sqares[int(e.X // sqaresize + (e.Y + e.s[1]) // sqaresize * maxsqare)].append(e)
        else:
            sqares2[
                int((e.X + e.ss[0]) // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(
                e)
            if e not in sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)]:
                sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
            if e not in sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)]:
                sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
            if e not in sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)]:
                sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(e)
        if distanceB(e.X, e.Y, e.n[e.f-1], e.n[e.f],-90):
            e.SY=0
            if e.ID==99:
                e.f-=2
                if e.f<1:
                    blns.remove(e)
                    for b in sqaresa:
                        if e in b:
                            b.remove(e)
                    drts2.remove(e)
                    e.kill()
                    del e
            else:
                e.f+=2
                if e.f>21:
                    health-=e.H
                    murder.append(e)
                    e.f=0
                    if health<0:
                        death(100,h//2-200)
power=0             
POWER=0
xplosions=[]           
ti=0
xS=0
spc=15
yS=0

blntrac=[370,150,370,85,1200,95,1520,300,1520,600,990,600
         ,990,340,820,340,820,500,350,500,350,1050]
spdx=0
elo=0   
spdy=0
A = [loadify('bloon'),loadify('blnB'),loadify('blngreen')
     ,loadify('blnyellow'),loadify('blnpink'),loadify('blnblac')
     ,loadify('tigerP'),loadify('tigerG'),loadify('blackrockbloon'),loadify('platebloon')]
B = [loadify('regred'),loadify('regblu'),loadify('reggrn')
     ,loadify('regyel'),loadify('regpin'),loadify('regbla')
     ,loadify('regpu2'),loadify('reggr2'),loadify('regblackrockbloon'),loadify('regplate')]
force=[]
drtmonks = []
drts=[]
enginers=[]
bossH=0
bossX=0
bossY=0
def sendbloon(stuff):
    global bloons,money,income
    #what is speed,health,ID,spawn,EX,EY
    bloonlistcomplete = [[2, 1, 1, 1, []], [4, 2, 2, 1, []], [6, 3, 3, 1, []], [8, 4, 4, 1, []], [10, 5, 5, 1, []],
                       [0, 1, 6, -2, [[2, 4]]], [9, 4, 7, -3, [[1, 5], [1, 8]]], [10, 5, 8, -4, [[1, 5], [4, 2]]],
                       [15, int(6 + rn / 10), int(6 + rn / 10), -1, []],
                       [10, 20, 9, -5, [[5, 5]]],[7, int(20 + rn / 12), 10,-6,[[4,9]],1], [16, rn + 50, 0, -11, [[4, 9]]],
                       [3, rn * 3 + 100, 0, -10, [[4, 11]]] ]
    what = bloonlistcomplete[stuff[1]]
    if len(stuff)>3:
        sent=0
        spc=stuff[3]
    else:
        spc=5
        sent=1
    if len(what) > 5:
        armour = what[5]
    else:
        armour = 0
    if what[3]>-10:
        what[0]+=min(rn,60)/5
    for e in range (stuff[0]):
        bloons.append(Bloon(-50 - e * spc,150, (what[0])/5
                            , what[1], 1
                            ,stuff[2], what[3], what[2], what[2],what[4],armour,0,sent))
income=25
def roundshow(x,y,l):
    dead = fint.render("round" + str(l), True, (0, 255, 0))
    screen.blit(dead, (x, y))
def hpshow(x,y):
    hhp = font.render("health:" + str(health), True, (0, 255, 0))
    screen.blit(hhp, (x, y))
    kii = font.render("money:" + str(int(money)), True, (0, 255, 0))
    screen.blit(kii, (x, y+25))
    kii = font.render("income:" + str("{:.1f}".format(income)), True, (0, 255, 0))
    screen.blit(kii, (x, y+50))
rn=5
speeed=0
hippo=0
heredy=0
headers = {'Content-type': 'application/json'}
def ready():
    global heredy,thorned,growbloon
    thorned=[]
    growbloon=[]
    roundshow(100, 500, rn - 3)
    pygame.display.update()
    connection.Send(
        {"action": "ready"})
    # r = requests.post('http://' + ipadress + ':5000/sendready', headers=headers,
    #                   data=jsonpickle.encode([me.ID,1]))

cl=1
def upgrade():
    global cl,price,lvlup,drtmonks,money,druids
    cl=1
    menu()
    for e in lvlup:
        menuAB(e.MID,e.F,e.f)
        sell(e.price)

    pygame.display.update()
    while cl==1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                XX = pygame.mouse.get_pos()
                if 450>XX[0]>200:
                    if 350>XX[1]:
                        cl=0
                
                if XX[0]>1100:
                    if 450>XX[1]:
                        if e.MID==1:
                            if e.F==0:
                                if money>29:
                                    for e in lvlup:
                                        e.c=e.c/2
                                        e.DS=e.DS*2
                                        e.F=1
                                        money-=30
                                        if e.f<2:
                                            e.I=loadify('drtmonkS')
                                            e.ID=loadify('drtS')
                                        cl=0
                            elif e.F==1:
                                if money>99:
                                    for e in lvlup:
                                        e.F=2
                                        money-=100
                                        e.Q=0.5
                                        cl=0
                            elif e.F==2 and e.f<3:
                                if money>109:
                                    for e in lvlup:
                                        e.DS+=10
                                        e.F=3
                                        money-=110
                                        e.ID=loadify('drtex')
                                        e.I=loadify('cyborg')
                                        e.P=[80,1,1]
                                        cl=0

                        elif e.MID==2:
                            if e.F==0:
                                if money>49:
                                    for e in lvlup:
                                        e.F=1
                                        if e.I==enginer:
                                            e.I=loadify('engineer2')
                                            e.MI=loadify('turret2b')
                                        money-=50
                                        e.Q=0.5
                                        cl=0
                            elif e.F==1:
                                if money>169:
                                    for e in lvlup:
                                        e.F=2
                                        e.I=loadify('grmn')
                                        e.MI=loadify('tureetb')
                                        e.ID=loadify('explodrt')
                                        e.P=[50,1,1]
                                        money-=170
                                        cl=0

                        elif e.MID==3:
                            if e.F==0:
                                if money>69:
                                    for e in lvlup:
                                        e.F=1
                                        e.c/=2
                                        money-=70
                                        cl=0
                            elif e.F==1:
                                if money>74:
                                    for e in lvlup:
                                        e.F=2
                                        money-=75
                                        cl=0
                        elif e.MID==4:
                            if e.F==0:
                                if money>199:
                                    for e in lvlup:
                                        e.I=loadify('double')
                                        e.F=1
                                        money-=200
                                        cl=0
                            elif e.F==1:
                                if money>199:
                                    for e in lvlup:
                                        e.I=loadify('triple')
                                        e.F=2
                                        money-=200
                                        cl=0
                            elif e.F==2:
                                if money>4499:
                                    for e in lvlup:
                                        e.I=loadify('tank')
                                        e.H+=6
                                        e.dmg += 1
                                        e.ID=loadify('blcdrt')
                                        e.DS*=3
                                        e.F=3
                                        e.c/=1.5
                                        money-=4500
                                        cl=0
                        elif e.MID==5:
                            if e.F==0:
                                if money > 39:
                                    for e in lvlup:
                                        e.H=9
                                        money-=40
                                        e.SPE.append(2)
                                        e.SPE.append(1)
                                        if e.f==0:
                                            e.I = loadify('druid2')
                                        elif e.f==1:
                                            e.I = loadify('druid3')
                                        e.F=1
                                        cl = 0
                            elif e.F==1:
                                if money > 379:
                                    for e in lvlup:
                                        money-=380
                                        e.DS+=1
                                        e.D/=1.2
                                        e.c/=3
                                        for y in range(len(e.SPE)):
                                            if e.SPE[y-1]==2:
                                                e.SPE[y] += 0.2
                                        if e.f==0:
                                            e.I = loadify('druid5')
                                        else:
                                            e.I = loadify('druid6')
                                        e.F=2
                                        cl=0
                    elif 900>XX[1]:
                        if e.MID==1:
                            if e.f==0 and e.dmg==1:
                                if money>39:
                                    e.f = 1
                                    money-=40
                                    e.dmg+=1
                                    cl = 0
                            elif e.f==1:
                                if money>39:
                                    for e in lvlup:
                                        e.c=e.c+2
                                        e.DS=e.DS-5
                                        if e.F>0:
                                            e.DS -= 5
                                        if e.DS<2:
                                            e.c=10000000
                                        e.H+=+2
                                        e.f=2
                                        money-=40
                                        e.I=loadify('beefdrtmonk')
                                        e.ID=loadify('beefdrt')
                                        cl=0
                            elif e.f==2 and e.F<3:
                                if money>99:
                                    for r in range(3):
                                        if e.F>0:
                                            r/=2
                                        if r*9.5<e.DS:
                                            e.H+=3
                                    e.DS += 2
                                    e.H += +2
                                    e.f = 3
                                    money -= 100
                                    e.ID = loadify('beefyerdrt')
                                    e.I = loadify('gorrila')
                                    cl = 0

                        elif e.MID==2:
                            if e.f==0:
                                if money>49:
                                    for e in lvlup:
                                        e.f=1
                                        money-=50
                                        e.c-=e.c/2.5
                                        e.c=int(e.c)
                                        if e.I==enginer:
                                            e.I=loadify('engineer2')
                                        cl=0
                            elif e.f==1:
                                if money>79:
                                    for e in lvlup:
                                        e.f=2
                                        money-=80
                                        e.I=loadify('time')
                                        e.MI=wata
                                        e.SPE=[1,1]
                                        cl=0

                        elif e.MID==3:
                            if e.f==0:
                                if money>249:
                                    for e in lvlup:
                                        e.f=1
                                        money-=250
                                        e.P=[35,1,1]
                                        e.ID=loadify('mineS')
                                        cl=0
                            elif e.f==1:
                                if money>999:
                                    for e in lvlup:
                                        e.f=2
                                        money-=1000
                                        cl=0
                                        e.G=0
                        elif e.MID==5:
                            if e.f==0:
                                if money > 49:
                                    for e in lvlup:
                                        e.f = 1
                                        money -= 50
                                        e.SPE.append(3)
                                        e.SPE.append(0)
                                        if e.F==0:
                                            e.I=loadify('druid02')
                                        elif e.F==1:
                                            e.I = loadify('druid3')
                                        elif e.f==1:
                                            e.I = loadify('druid6')
                                        e.dmg+=3
                                        cl = 0
                            elif e.f==1:
                                if money > 89:
                                    for e in lvlup:
                                        e.f = 2
                                        money -= 90
                                        e.bounce+=2
                                        cl = 0

                    else:
                        for e in lvlup:
                            money+=price
                            if e.MID==1:
                                drtmonks.remove(e)
                            elif e.MID==2:
                                enginers.remove(e)
                            elif e.MID==3:
                                factories.remove(e)
                            elif e.MID==4:
                                gunners.remove(e)
                            if e.MID==5:
                                druids.remove(e)
                            e.kill()
                            monks.remove(e)
                            del e
                            cl=0


    lvlup = []
price=0
def sell(insta):
    global price
    price = insta
    sold = flont.render("sell for " + str(price), True, (0, 0, 0))
    screen.blit(sold, (1150, 945))
def menu():
    screen.blit(loadify('menu'),(0,0))
def menuAB(MT,UPGNUM,PGNUM):
    if MT == 1:
        if UPGNUM==0:
            screen.blit(loadify('menuspd'),(1100,0))
        elif UPGNUM==1:
            screen.blit(loadify('doubleshot'),(1100,0))
        elif PGNUM>2:
            screen.blit(loadify('nope'),(1100,0))
        elif UPGNUM==2:
            screen.blit(loadify('explodedrt'),(1100,0))
    if MT == 2:
        if UPGNUM==0:
            screen.blit(loadify('turretmenu'),(1100,0))
        elif UPGNUM==1:
            screen.blit(loadify('gears'),(1100,0))
    if MT == 3:
        if UPGNUM==0:
            screen.blit(loadify('menFspikes'),(1100,0))
        elif UPGNUM==1:
            screen.blit(loadify('crawls'),(1100,0))
    if MT == 4:
        if UPGNUM==0:
            screen.blit(loadify('barrel'),(1100,0))
        elif UPGNUM==1:
            screen.blit(loadify('barells'),(1100,0))
        elif UPGNUM==1:
            screen.blit(loadify('barells'),(1100,0))
        elif UPGNUM==2:
            screen.blit(loadify('tankmen'),(1100,0))
    if MT == 5:
        if UPGNUM==0:
            screen.blit(loadify('regrowth'),(1100,0))
        elif UPGNUM==1:
            screen.blit(loadify('druidbook'),(1100,0))
    if MT == 1:
        if PGNUM==0:
            screen.blit(loadify('sharper'),(1100,450))
        elif PGNUM==1:
            screen.blit(loadify('beefmen'),(1100,450))
        elif UPGNUM>2:
            screen.blit(loadify('nope'),(1100,450))
        elif PGNUM==2:
            screen.blit(loadify('beefyermenu'),(1100,450))

    if MT == 2:
        if PGNUM==0:
            screen.blit(loadify('spannermen'),(1100,450))
        if PGNUM==1:
            screen.blit(loadify('timemen'),(1100,450))

    if MT == 3:
        if PGNUM==0:
            screen.blit(loadify('menmne'),(1100,450))
        elif PGNUM==1:
            screen.blit(loadify('minemen'),(1100,450))
    if MT == 5:
        if PGNUM==0:
            screen.blit(loadify('brambles'), (1100, 450))
        if PGNUM==1:
            screen.blit(loadify('bouncy'), (1100, 450))
branch=loadify("thorns")
thorned=[]
def bloon():
    for e in bloons:
        screen.blit(e.I,(e.x-e.EX,e.y-e.EY))
    for b in thorned:
        screen.blit(pygame.transform.smoothscale(branch,(b.s[0],b.s[1])), (b.x - b.EX, b.y - b.EY))
def drtmonk():
    for e in drtmonks:
        screen.blit(e.I,(e.X,e.Y))
    for e in druids:
        screen.blit(e.I,(e.X,e.Y))


def engeneer():
    for e in enginers:
        screen.blit(e.I,(e.X,e.Y))
def Factory():
    for e in factories:
        screen.blit(e.I,(e.X,e.Y))
def drt():
    for e in drts:
        screen.blit(e.a,(e.x-e.V,e.y-e.C))
    for e in drts2:
        screen.blit(e.a,(e.x,e.y))
    for e in gunners:
        screen.blit(e.IB,(e.X-e.EX,e.Y-e.EY))
    for e in xplosions:
        screen.blit(e.I,(int(e.X-e.s[0]/2),int(e.Y-e.s[1]/2)))
choecko=loadify('spikes')
gold=loadify('gold')
bossI=loadify('blnboss')
boss2=loadify('capsule')
rel=1
def distanceB(eneX, eneY, bulX, bulY,o):
    distance= math.sqrt((math.pow(eneX-bulX,2))+ (math.pow(eneY-bulY,2)))
    if distance<100+o:
        return True
def distanceC(eneX, eneY, bulX, bulY):
    distance= math.sqrt((math.pow(eneX-bulX,2))+ (math.pow(eneY-bulY,2)))
    return distance

def distanceM(eneX, eneY, bulX, bulY,o):
    if ti %lo == 0:
        distance= math.sqrt((math.pow(eneX-bulX,2))+ (math.pow(eneY-bulY,2)))
        if distance<100+o:
            return True
bl=10
bloons.append(Bloon(50,150,1,1,1,0,1,1,0))
def paused(x,y):
    paus = font.render("paused, press any key to resume", True, (0, 255, 0))
    screen.blit(paus, (x, y))
paus=1
def pause():
    global paus
    paus=1
    while paus==1:
        global pas
        if (time.time()-pas)> 1:
            paused(10,10)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                paus=0
monksel=[loadify('drtmonk'),loadify('engineer')
         ,loadify('spikefac'),loadify('gunner'),loadify('smoldruid')]
def death(x,y):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
        dead = fint.render("U died on round:" + str(rn-4), True, (255, 0, 0))
        screen.blit(dead, (x, y))
        pygame.display.update()
io=0

            
def speed(ch):
    if ch==10+rn/10:
        speeeed=rn/5+15
    else:
        if ch==6:
            ch=0
        speeeed=rn/5+ch*2
    return speeeed
TL=[loadify('turret'),loadify('turretb'),loadify('turret2b'),loadify('turret2')
    ,loadify('tureetb'),loadify('tureet'),loadify('waterb'),loadify('water')]
 
pliesX = 0
spikX=0
cf=0
explod1=[]
explod2=[]
explod3=[]
for e in range(25):
    explod1.append(loadanimation("boombiatch",'t'+str(e)))
for e in range(104):
    explod3.append(loadanimation("explosion2",'t'+str(e)))
for e in range(98):
    explod2.append(loadanimation("explosion",'tt'+str(e)))
explod=[explod1,explod2,explod3]

spikY=0
pliesY = 0
lo = 1
moar=[pygame.transform.smoothscale(loadify('btd map'),(w,h)).get_size(),loadify('btd map').get_size()]
tracY=[170, 170, 170, 170, 170, 170, 131, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 120, 147, 173, 200, 226, 252, 279, 305, 347, 397, 447, 497, 547, 597, 611, 612, 613, 613, 614, 615, 616, 617, 618, 619, 602, 552, 502, 452, 402, 368, 365, 362, 365, 415, 465, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 170, 170, 170]
tracX=[110, 160, 210, 260, 310, 360, 376, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1210, 1252, 1294, 1337, 1379, 1422, 1464, 1507, 1522, 1523, 1525, 1526, 1528, 1529, 1492, 1442, 1392, 1342, 1292, 1242, 1192, 1142, 1092, 1042, 1009, 1007, 1005, 1003, 1001, 984, 934, 884, 839, 836, 833, 825, 775, 725, 675, 625, 575, 525, 475, 425, 375, 368, 368, 367, 366, 365, 364, 363, 362, 361, 360, -36, -84, -133]
for e in tracY:
    e*=moar[0][1]/moar[1][1]
for e in tracX:
    e*=moar[0][0]/moar[1][0]
select=0
spoikX=[]
boss=0
spoikY=[]
drts2=[]
locked=-1
lock=loadify("locked")
targetedB=[]
targetedF=[]
factories=[]
images=[]
scroll=0
ploi=0
CheaterPowers=0
board=loadify("board")
panelloon=loadify("bloonyroad")
panelsize = pygame.Surface.get_size(panelloon)
panelsize=panelsize[1]
back=pygame.transform.smoothscale(loadify('btd map'),(w,h))
bloonamount=loadify("killerrock")
drts3=[]
bloonumba=1
bloonprices=[ [[1,0.1],[2,0.23]], [[2,0.2],[4,0.5]], [[3,0.3],[6,0.77]], [[4,0.4],[7,0.9]], [[5,0.5],[10,1.3]],
             [[10,1],[24,2]], [[14,1.2],[30,2.2]], [[14,1.2],[30,2.2]], [[10,0.9],[24,2]], [[90,0.25],[200,0.5]], [[300,0],[500,0]], [[800,1]],[[1800,-50]] ]
while running:
    XX = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if XX[0]>w-200:
                if XX[1]<h-200:
                    clickpos=XX[1]-scroll
                    if 118*len(bloonprices)+13>clickpos>12:
                        if int((clickpos-13)/118)<locked:
                            if bloonprices[int((clickpos-13)/118)][growmaybe][0]*bloonumba<=money:
                                growmaybe=0
                                if XX[0]>w-100:
                                    if int((clickpos-13)/118)<10:
                                        growmaybe=1
                                connection.Send({"action": "send", "what": [bloonumba, int((clickpos-13)/118),growmaybe*random.randint(100,400)]})
                                money-=bloonprices[int((clickpos-13)/118)][growmaybe][0]*bloonumba
                                income+=bloonprices[int((clickpos-13)/118)][growmaybe][1]*bloonumba
                elif XX[0]>w-100:
                    if XX[1] < h - 100:
                        bloonumba+=1
                    elif bloonumba>1:
                        bloonumba -= 1
            else:
                pliesY =0
                for e in monks:
                    if distanceB(XX[0]-60, XX[1]-80, e.X, e.Y,0):
                        pliesY = 1
                if pliesY == 0:
                    if select==0:
                        if money>24:
                            money-=25
                            drtmonks.append(drtmonkey(XX[0]-60,XX[1]-80,loadify('drtmonk')
                                                  ,0,0,10+random.randint(-9,10),1
                                                  ,200+random.randint(-120,120),loadify('drtn'),-10,[0,0],[0,0]))
                    elif select==1:
                        if money>74:
                            money-=75
                            enginers.append(engin(XX[0]-60,XX[1]-80,enginer
                                                      ,0,0,15+random.randint(-10,15),1
                                                      ,1000+random.randint(-600,600)
                                                      ,loadify('turret'),200+random.randint(-120,120)
                                                      ,loadify('nail'),1000,[0,0],[0,0]))
                    elif select==2:
                        if money>99:
                            money-=100
                            factories.append(factory(XX[0]-60,XX[1]-80,loadify('spikefac')
                                                     ,0,0,5,200+random.randint(-120,120)
                                                     ,loadify('spikes'),2000+random.randint(-900,900)
                                                     ,[0,0]))
                    elif select==3:
                        if money>249:
                            money-=250
                            gunners.append(gunner(XX[0]-60,XX[1]-80,loadify('guner')
                                                     ,0,0,5+random.randint(-2,2),20+random.randint(-12,12)
                                                  ,loadify('drtn'),1,[0,0],[0,0]))
                    elif select==4:
                        if money>49:
                            money-=50
                            druids.append(Druid(XX[0]-60,XX[1]-80,loadify('druid'),0,0,4+random.randint(-3,0),650+random.randint(-250,250),200+random.randint(-50,250),[]))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
             XX = pygame.mouse.get_pos()
             if distanceB(XX[0], XX[1], 410, 403,-50):
                 xplosions.append(explode(380,400,gold,400))
                 
             for e in monks:
                 if distanceB(XX[0]-60, XX[1]-80, e.X, e.Y,-50):
                     lvlup.append(e)
                     upgrade()
                     break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                scroll-=min(scroll+panelsize-h,25)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                scroll+=min(-scroll,25)
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_p:
                 pause()
             if event.key == pygame.K_SPACE:
                 for e in drts2:
                     if e.CR>1:
                         if e.LS>ti:
                             e.LS=ti+1
             if event.key == pygame.K_s:
                 lo+=1
             if event.key == pygame.K_d:
                 if lo>2:
                     lo-=1
             if event.key == pygame.K_g:
                for b in factories:
                    if b.f>1:
                        if b.G<ti:
                            b.G=ti+10000
                            XX = pygame.mouse.get_pos()
                            xS= (XX[0])-(b.X+10)
                            yS=(XX[1])-(b.Y+60)
                            if xS==0:
                                spdx=5
                                spdy=0
                            else:
                                spdx=5/math.sqrt(yS**2/xS**2+1)
                                if xS<0:
                                    spdx*=-1
                                spdy=spdx*yS/xS
         
                            drts.append(mine(b.X+10,b.Y+60,spdx,spdy,150+rn,0,0,[1000,10,0],XX,[0,0],3))
                            break

             if event.key == pygame.K_LEFT:
                 if select>0:
                     select-=1
                 else:
                     select=len(monksel)-1
             if event.key == pygame.K_RIGHT:
                 select+=1
                 if len(monksel)-1<select:
                     select=0
             if event.mod & pygame.KMOD_RSHIFT:
                 if event.key == pygame.K_q:
                     money+=1000
                 elif event.key == pygame.K_BACKSLASH:
                     CheaterPowers=1
        if event.type == pygame.QUIT:
           pygame. quit()
    connection.Pump()
    nwl.Pump()
    #if ti%1 == 0:
    for b in animations:
        if b.faze<int(b.t/b.T*len(b.ii)):
            b.faze=int(b.t/b.T*len(b.ii))
            b.i=b.ii[b.faze-1]
    for e in xplosions:
        e.t+=4
        if e.t>e.T:
            xplosions.remove(e)
            if e in animations:
                animations.remove(e)
            e.kill()
            del e
        else:
            e.I=pygame.transform.smoothscale(e.i,(int((e.t*3+e.Start)*e.S),int((e.t*3+e.Start)*e.S)))
            e.s = pygame.Surface.get_size(e.I)
    if CheaterPowers==1:
        for e in bloons:
            e.hploss(100)
    # r = requests.post('http://' + ipadress + ':5000/anynew', headers=headers,
    #                   data=jsonpickle.encode(me.ID))
    # thing = jsonpickle.decode(r.text)
    # for e in thing:
    #     updatelist[e[0]](e[1])

    # for b in force:
    #     #PO:amount of charges, max charges po:for shield recharge cooldown, second is time of shield expiration, first is cooldonw neccessary
    #     if b.PO[0]>0:
    #         for e in drts2:
    #             if distanceM(b.X+b.EX, b.Y+b.EY, e.X+5, e.Y+50,42):
    #                 b.PO[0] -= 1
    #                 if b.PO[0] < 1:
    #                     b.I=spe[3]
    #                     b.EX=0
    #                     b.EY=0
    #                     b.T=32
    #                     b.R=40
    #                     b.po[1]=ti
    #                     rel=0
    #                 e.H -= 10
    #                 if e.H < 1:
    #                     for b in sqaresa:
    #                         if e in b:
    #                             b.remove(e)
    #                     if e in blns:
    #                         blns.remove(e)
    #                     drts2.remove(e)
    #                     e.kill()
    #                     del e
    #                     rel=0
    #                 if rel ==0:
    #                     rel=1
    #                     break
    #         for e in drts:
    #             if distanceM(b.X+b.EX, b.Y+b.EY, e.X+5, e.Y+50,32):
    #                 b.PO[0] -= 1
    #                 if b.PO[0] < 1:
    #                     b.I=spe[3]
    #                     b.EX=0
    #                     b.EY=0
    #                     b.T=32
    #                     b.R=40
    #                     b.po[1]=ti
    #                     rel=0
    #                 e.H -= 3
    #                 if e.H < 1:
    #                     drts.remove(e)
    #                     e.kill()
    #                     del e
    #                 if rel ==0:
    #                     rel=1
    #                     break
    #
    #     elif ti-b.po[1]> b.po[0]:
    #         b.PO[0]=b.PO[1]
    #         b.I=spe[2]
    #         b.EX=20
    #         b.EY=35
    #         b.T=20
    #         b.R=35

    for z in range(400):
        for b in sqares[z]:
            for d in sqares2[z]:
                if d in drts:
                    if b not in murder:
                        if distanceM(b.X+b.T, b.Y+b.R-10, d.X+5, d.Y+5,-80+b.siz+d.siz):
                            d.special(b)
                            if d.dmg>b.armr:
                                b.hploss(d.dmg-b.armr)
                            d.H -= 1
                            if d.H < 1:
                                if d.P[0]>0:
                                    xplosions.append(explode(d.x,d.y,d.P[2],d.P[0]))
                                    for c in bloons:
                                        if d.P[1]>c.armr:
                                            if distanceB(c.X+c.T,c.Y+c.R, d.X+5, d.Y+50,d.P[0]+c.siz):
                                                c.hploss(d.P[1]-c.armr)

                                d.kill()
                                drts.remove(d)
                                del d
                                rel=0
                elif d in drts2:
                    if b not in murder:
                        if distanceM(b.X+b.T, b.Y+b.R, d.X, d.Y,-75+b.siz):
                            d.H -= 1
                            if b.armr<d.dmg:
                                b.hploss(d.dmg-b.armr)
                            if d.H < 1:
                                if d.P[0]>0:
                                    xplosions.append(explode(d.x,d.y,d.P[2],d.P[0]))
                                    for c in bloons:
                                        if c.armr<d.P[1]:
                                            if distanceB(c.X+c.T,c.Y+c.R, d.X+5, d.Y+50,d.P[0]+c.siz):
                                                c.hploss(d.P[1]-c.armr)
                                if d in blns:
                                    blns.remove(d)
                                for i in sqaresa:
                                    if d in i:
                                        i.remove(d)
                                drts2.remove(d)
                                d.kill()
                                del d

    for e in factories:
        if (ti-e.C)> e.c:
            if not len(e.spikeX)<4:                
                e.C = ti
                elo=random.randint(0,len(e.spikeX)-2)
                cl=random.uniform(0,1)
                spikX=(1-cl)*e.spikeX[elo]+e.spikeX[elo+1]*cl
                spikY=(1-cl)*e.spikeY[elo]+e.spikeY[elo+1]*cl
                drtnew=Drt2(int(spikX),int(spikY),e.ID,e.H,e.LS+ti,e.f,e.F,e.tracpos,e.P)
                sqaresa[int((drtnew.X + drtnew.ss[0]) // sqaresize + (drtnew.Y + drtnew.ss[1]) // sqaresize * maxsqare)].append(drtnew)
                if drtnew not in sqaresa[int(drtnew.X // sqaresize + drtnew.Y // sqaresize * maxsqare)]:
                    sqaresa[int(drtnew.X // sqaresize + drtnew.Y // sqaresize * maxsqare)].append(drtnew)
                if drtnew not in sqaresa[int((drtnew.X + drtnew.ss[0]) // sqaresize + drtnew.Y // sqaresize * maxsqare)]:
                    sqaresa[int((drtnew.X + drtnew.ss[0]) // sqaresize + drtnew.Y // sqaresize * maxsqare)].append(drtnew)
                if drtnew not in sqaresa[int(drtnew.X // sqaresize + (drtnew.Y + drtnew.ss[1]) // sqaresize * maxsqare)]:
                    sqaresa[int(drtnew.X // sqaresize + (drtnew.Y + drtnew.ss[1]) // sqaresize * maxsqare)].append(drtnew)
                drts2.append(drtnew)
    for e in druidart:
        if e.D[0]+e.D[1]<ti:
            drts.append(e)
            druidart.remove(e)
    for b in druids:
        if (ti - b.C) > b.c:
            for e in bloons:
                if distanceM(e.X + e.T, e.Y + e.R, b.X + 67, b.Y + 60, 350 + e.siz):
                    pliesX = 15
                    pliesY = 20
                    b.C = ti
                    xS = (e.X + e.T) - (b.X + pliesX)
                    yS = (e.Y + e.R) - (b.Y + pliesY)
                    if xS == 0:
                        spdx = b.DS
                        spdy = 0
                    else:
                        spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                        if xS < 0:
                            spdx *= -1
                        spdy = spdx * yS / xS
                    druiddart=Drt(b.X + pliesX, b.Y + pliesY, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE, b.dmg,b.bounce)
                    druiddart.D=[ti,b.D]
                    drts.append(druiddart)
                    break

    for b in drtmonks:
        if (ti-b.C)> b.c:
            rel=0
            for e in bloons:
                if distanceM(e.X+e.T, e.Y+e.R, b.X+67, b.Y+60,350+e.siz):
                    if b.LS == -10:                        
                        pliesX = 10
                        pliesY = 70
                    else:
                        pliesX = 15
                        pliesY = 20
                        if e.X>b.X:
                            if b.rot > 0:
                                b.I=TL[b.rot]
                                b.rot*=-1

                        elif b.rot < 0:
                            b.rot*=-1
                            b.I=TL[b.rot-1]
                    b.C = ti
                    xS= (e.X+e.T)-(b.X+pliesX)
                    yS=(e.Y+e.R)-(b.Y+pliesY)
                    if xS==0:
                        spdx=b.DS
                        spdy=0
                    else:
                        spdx=b.DS/math.sqrt(yS**2/xS**2+1)
                        if xS<0:
                            spdx*=-1
                        spdy=spdx*yS/xS
 
                    drts.append(Drt(b.X+pliesX,b.Y+pliesY,spdx,spdy,b.ID,b.H,0,0,b.P,b.SPE,b.dmg))
                    if b.LS>0:
                        if b.F>0:
                            drts.append(Drt(b.X+pliesX-spdx,b.Y+pliesY-spdy,spdx,spdy,b.ID,b.H,0,0,b.P,b.SPE,b.dmg))
                    rel+=b.Q
                    if rel==1:
                        break
    for b in gunners:
        if (ti-b.C)> b.c:
            XX = pygame.mouse.get_pos()
            pliesX = -12 
            pliesY = 0
            b.C = ti
            xS= (XX[0])-(b.X+pliesX)
            yS=(XX[1])-(b.Y+pliesY)
            if xS==0:
                spdx=b.DS
                spdy=0
            else:
                spdx=b.DS/math.sqrt(yS**2/xS**2+1)
                if xS<0:
                    spdx*=-1
                spdy=spdx*yS/xS
            
            if spdx==0:
                if spdy<0:
                    b.IB=pygame.transform.rotate(b.I,-90)
                else:
                     b.IB=pygame.transform.rotate(b.I,90)
            elif spdx>0:
                b.IB=pygame.transform.rotate(b.I,-math.atan(spdy/spdx)*180/math.pi)
            else:
                b.IB=pygame.transform.rotate(b.I,180-math.atan(spdy/spdx)*180/math.pi)
            ss=pygame.Surface.get_size(b.IB)
            b.EX=int(ss[0]/2)
            b.EY=int(ss[1]/2)

            if b.F>0:
                nspd=b.DS/10
                nespd=spdx/-nspd
                newspd=spdy/nspd
                pliesX=5
                pliesY=5
                pliesX*=newspd
                pliesY*=nespd
                drts.append(Drt(b.X+pliesX,b.Y+pliesY,spdx,spdy,b.ID,b.H,0,0,b.P,b.SPE,b.dmg))
                if b.F>1:
                    drts.append(Drt(b.X-pliesX,b.Y-pliesY,spdx,spdy,b.ID,b.H,0,0,b.P,b.SPE,b.dmg))
                    if b.F>2:
                        pliesX/=2
                        pliesY/=2
                        newspd=random.randint(1,10)
                        if newspd>9:
                            newspd=150
                            nespd=bomb
                        else:
                            newspd=0
                            nespd=b.ID
                        drts.append(Drt(b.X+pliesX,b.Y+pliesY,spdx,spdy,nespd,b.H,0,0,[b.P[0]+newspd,b.P[1]+3,1],b.SPE,b.dmg))
                        drts.append(Drt(b.X-pliesX,b.Y-pliesY,spdx,spdy,nespd,b.H,0,0,[b.P[0]+newspd,b.P[1]+1,1],b.SPE,b.dmg))
                        drts.append(Drt(b.X,b.Y,spdx,spdy,nespd,b.H,0,0,[b.P[0]+newspd,b.P[1]+1,1],b.SPE,b.dmg))
                       
            drts.append(Drt(b.X,b.Y,spdx,spdy,b.ID,b.H,0,0,b.P,b.SPE,b.dmg))
    sqares=[[g for g in e] for e in sqaresb]
    sqares2 = [[g for g in e] for e in sqaresa]
    for b in enginers:
        if (ti-b.C)> b.c:
            b.C = ti
            drtmonks.append(drtmonkey(b.X+random.randint(-150,200),b.Y+random.randint(-150,200),b.MI,b.f,b.F
                                      ,b.DS,b.H,b.MC,b.ID,b.LS*2+ti,b.P,b.SPE))
        elif b.f>0:
           if random.randint(1,2)==2:
               pass
           elif (ti-b.C)== int(b.c/2):
                for e in bloons:
                    xS= (e.X+e.T)-(b.X+10)
                    yS=(e.Y+e.R)-(b.Y+60)
                    if xS==0:
                        spdx=b.DS
                        spdy=0
                    else:
                        spdx=b.DS/math.sqrt(yS**2/xS**2+1)
                        if xS<0:
                            spdx*=-1
                        spdy=spdx*yS/xS
 
                    drts.append(Drt(b.X+10,b.Y+60,spdx,spdy,loadify('spanner'),10,0,0,[0,0],b.SPE))
                    break
           
    screen.blit(back,(0,0))
    blnM()
    drtM()
    drtmonk()
    engeneer()
    Factory()
    bloon()
    drt()
    hpshow(10,10)
    screen.blit(loadify('select'),(40,780)) 
    screen.blit(monksel[select],(50,800))    
    screen.blit(panelloon,(w-240,scroll))
    for b in range(len(bloonprices)):
        v=len(bloonprices)-b
        if int((121*v)/118)>locked:
            screen.blit(lock, (w-240, int((118*(v-1)+scroll+13))))
        else:
            break
    for e in images:
        screen.blit(e.I,(x,y))
    screen.blit(bloonamount, (w - 240, h-200))
    bwee = finter.render(str(bloonumba), True, (0, 0, 0))
    screen.blit(bwee, (w - 180, h - 150))
    if XX[0]>w-200:
        if XX[1] < h - 200:
            clickpos = XX[1] - scroll
            if 118 * len(bloonprices) + 13 > clickpos > 12:
                growmaybe=0
                if XX[0]>w-100:
                    if int((clickpos - 13) / 118)<10:
                        growmaybe=1
                screen.blit(board, (XX[0] - 300, XX[1]))
                bwee = flint.render(str(bloonprices[int((clickpos - 13) / 118)][growmaybe][0]*bloonumba), True, (0, 0, 0))
                screen.blit(bwee, (XX[0]-198, XX[1]+25))
                bwee = flint.render(str(bloonprices[int((clickpos - 13) / 118)][growmaybe][1]*bloonumba), True, (0, 0, 0))
                screen.blit(bwee, (XX[0]-162, XX[1]+62))
    pygame.display.update()

    ti+=1
    for e in drtmonks:
        if e.LS == ti:
            e.kill()
            drtmonks.remove(e)
            del e
    for e in drts2:
        if e.LS == ti:
            if e.CR>1:
                blns.append(e)
                e.n=blntrac
                e.SX=0
                e.SY=0
                e.S=3
                e.ID=99
            else:
                for b in sqaresa:
                    if e in b:
                        b.remove(e)
                drts2.remove(e)
                e.kill()
                del e
                

    for e in growbloon:
        if ti %(e.r*3) == 0:
            e.grow()

    for e in mines:
        if distanceB(e.X,e.Y, e.LS[0], e.LS[1],-90):
            e.S=0
            e.s=0
            mines.remove(e)
    moida()




        
