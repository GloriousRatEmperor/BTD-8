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
btdmap=0
with open("ip.txt", "r") as ip:
    ipadress = ip.read()

connection.DoConnect((ipadress, 5071))
blntrac=[]
class MyNetworkListener(ConnectionListener):

    def Network(self, data):
        pass

    def Network_gitplayer(self, data):
        global me
        if data["id"] < 3:
            me = player(data["id"])
        else:
            uu = 1 / 0

    def Network_ugotbloonsmon(self, data):
        sendbloon(data["takedis"])

    def Network_mapchosen(self, data):
        global btdmap,maps,chosen,blntrac,mapspecial
        btdmap=maps[(data["info"])[0]-1]
        chosen=100
        blntrac=blntracks[(data["info"])[0]-1]
        mapspecial=mapspecials[(data["info"])[0]-1]



nwl = MyNetworkListener()

pygame.init()


class player(object):
    def __init__(self, ID):
        self.ID = ID


connection.Send({"action": "start", "id": 888690420})


# r = requests.post('http://' + ipadress + ':5000/AuctionPrice', headers=headers,
#                   data=j
# r = requests.get(f'http://{ipadress}:5000/start')
# me = jsonpickle.decode(r.text)
def loadify(imgname):
    return pygame.image.load(f"imagesboom/{imgname}.png").convert_alpha()


def loadanimation(foldername, imgname):
    return pygame.image.load(f"imagesboom/boom/{foldername}/{imgname}.png").convert_alpha()


font = pygame.font.Font('freesansbold.ttf', 25)
fint = pygame.font.Font('freesansbold.ttf', 150)
finter = pygame.font.Font('freesansbold.ttf', 48)
flont = pygame.font.Font('freesansbold.ttf', 80)
flint = pygame.font.Font('freesansbold.ttf', 30)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, h = pygame.display.get_surface().get_size()
w =W-240
pygame.display.set_caption("BTD Battles 8")
icon = loadify('drtmonk')
pygame.display.set_icon(icon)
running = True
XX = 0
PXSPD = 0
PYSPD = 0
YY = 0
growbloon = []
money = 101
pas = time.time()
bloons = []
lvlup = []
monks = []
animations = []
bomb = loadify('bomb')
gunners = []
enginer = loadify('engineer')
gunI = loadify('guner')
wata = loadify('water')
blns = []
mines = []
murder = []
sqares = []
sqaresize = 100
for e in range(204):
    sqares.append([])
maxsqare = 17
sqaresa = [[g for g in e] for e in sqares]
sqaresb = [[g for g in e] for e in sqares]
sqares2 = [[g for g in e] for e in sqares]

drtmunks=[]
class drtmonkey(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, f, F, DS, H, c, ID, LS, P, SPE, dmg=1,range=250):
        super(drtmonkey, self).__init__()
        self.SPX = []
        drtmunks.append(self)
        if LS == -10:
            monks.append(self)
            self.price = 20
            # self.price = 31+int(DS / 3) - int(c / 10)
        else:
            if I == wata:
                self.rot = 7
            else:
                self.rot = F * 2 + 1
            # if F>0:
            # self.Q=0.5
            # else:
            # self.Q=1
        self.rang=range
        self.Q = 1
        self.MID = 1
        self.LS = LS
        self.dmg = dmg
        self.ID = ID
        self.H = H
        self.c = c
        self.DS = DS

        self.C = ti
        self.I = I
        self.f = f
        self.SPE = SPE
        self.F = F
        self.X = X
        self.Y = Y
        self.XX = X
        self.YY = Y
        self.P = P
        self.ss = pygame.Surface.get_size(self.I)

class leafblower(drtmonkey):
    def __init__(self,X, Y, I, f, F, DS, H, c, ID, LS, P, SPE,blow,range):
        super().__init__( X, Y, I, f, F, DS, H, c, ID, LS, P, SPE)
        self.MID = 6
        self.i=I
        self.rang=range
        drtmunks.remove(self)
        self.price = 10
        self.Slow = 0.1
        self.blow=blow
        self.power=0
        self.XX = self.X-self.ss[0]//2
        self.YY = self.Y-self.ss[1]//2

class gunner(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, f, F, DS, c, ID, H, P, SPE):
        super(gunner, self).__init__()
        monks.append(self)
        self.c = c
        self.dmg = 1
        self.MID = 4
        self.price = 225
        self.H = H
        self.ID = ID
        self.DS = DS
        self.C = ti
        self.I = gunI
        self.IB = I
        self.f = f
        self.SPE = SPE
        self.F = F
        self.X = X
        self.Y = Y
        self.XX = X
        self.YY = Y
        self.P = P
        self.EX = 0
        self.EY = 0


class factory(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, f, F, H, c, ID, LS, P):
        self.spikeX = []
        self.spikeY = []
        self.X = X
        self.Y = Y
        self.XX = X
        self.YY = Y
        self.price = 90
        self.SPE = [0, 0]
        super(factory, self).__init__()
        monks.append(self)
        for i in range(len(tracX)):
            if distanceB(tracX[i], tracY[i], self.X + 60, self.Y + 60, 200):
                self.spikeX.append(tracX[i])
                self.spikeY.append(tracY[i])
        gobl = 10000
        for i in range(int((len(blntrac)) / 2)):
            if i > 0:
                if distanceC(blntrac[i * 2 - 2], blntrac[i * 2 - 1], self.X + 60, self.Y + 60) < gobl:
                    numba = i * 2 - 1
                    gobl = distanceC(blntrac[i * 2 - 2], blntrac[i * 2 - 1], self.X + 60, self.Y + 60)
        self.tracpos = numba

        self.MID = 3
        self.ID = ID
        self.H = H
        self.LS = LS
        self.c = c
        self.G = 100000000
        self.C = ti
        self.I = I
        self.Dmg = 1
        self.f = f
        self.F = F
        self.P = P


class Image(pygame.sprite.Sprite):
    def __init__(self, I, X, Y):
        self.I = I
        self.x = X
        self.y = Y


class engin(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, f, F, DS, H, c, MI, MC, ID, LS, P, SPE):
        super(engin, self).__init__()
        monks.append(self)
        self.SPE = SPE
        self.price = 69
        self.MID = 2
        self.ID = ID
        self.MC = MC
        self.MI = MI
        self.LS = LS
        self.ID = ID
        self.H = H
        self.c = c
        self.DS = DS
        self.C = ti
        self.I = I
        self.f = f
        self.F = F
        self.X = X
        self.Y = Y
        self.XX = X
        self.YY = Y
        self.P = P


ball = loadify("druidball")
druidart = []


class Drt(pygame.sprite.Sprite):
    def __init__(self, X, Y, S, s, I, H, x, y, P, SPE, DMG=1, bounce=0, Specialonexplosion=[]):
        super(Drt, self).__init__()
        self.x = 0
        self.dmg = DMG
        self.b = bounce
        self.y = 0
        self.SPE = SPE
        self.SPX = Specialonexplosion
        self.IM = 0
        self.I = I
        if xS == 0:
            spdx = b.DS
            spdy = 0
        else:
            spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
            if xS < 0:
                spdx *= -1
            spdy = spdx * yS / xS
        if spdx == 0:
            if spdy < 0:
                self.a = pygame.transform.rotate(self.I, -90)
            else:
                self.a = pygame.transform.rotate(self.I, 90)
        elif spdx > 0:
            self.a = pygame.transform.rotate(self.I, -math.atan(spdy / spdx) * 180 / math.pi)
        else:
            self.a = pygame.transform.rotate(self.I, 180 - math.atan(spdy / spdx) * 180 / math.pi)
        self.ss = pygame.Surface.get_size(self.a)
        self.I = self.a
        self.s = s
        self.S = S
        self.H = H
        self.X = X
        self.Y = Y
        self.P = P
        self.siz = (self.ss[0] + self.ss[1]) / 5
        self.V = int(self.ss[0] / 2)
        self.C = int(self.ss[1] / 2)

    def special(self, loss):
        for c in range(len(self.SPE) // 2):
            if self.SPE[c * 2 - 2] == 1:
                if loss.ID > -10:
                    loss.f -= self.SPE[c * 2 - 1] * 2
                    if loss.f < 1:
                        loss.f = 1
                    loss.SY = 0
                else:
                    if loss.IM == 0:
                        loss.SX /= self.SPE[c * 2 - 1] + 1
                        loss.SY /= self.SPE[c * 2 - 1] + 1
                        loss.IM = 1

    def xplod(d):
        xplosions.append(explode(d.x+d.V, d.y+d.C, d.P[2], d.P[0]))
                     #X, Y, i, T, howfast=1, strt=60
        for c in bloons:
            if c not in murder:
                if distanceB(c.X, c.Y, d.X, d.Y, d.P[0] + c.siz):
                    for r in range(len(d.SPX) // 2):
                        if d.SPX[r * 2 - 2] == 4:
                            if c not in burning and c.ID > -9:
                                burning.append(c)
                                c.lists.append(burning)
                                c.firetick = [0, d.SPX[r * 2 - 1][0]]
                                c.firedmg = d.SPX[r * 2 - 1][1]
                    if c.armr < d.P[1]:
                        if int(d.P[1]) > 0:
                            c.hploss(int(d.P[1]) - c.armr)


class druidball(Drt):
    def __init__(self, X, Y, S, s, I, H, x, y, P, SPE, DMG=1, bounce=0, pierce=[0, 0]):
        super().__init__(X, Y, S, s, I, H, x, y, P, SPE, DMG, bounce)
        self.pierce = pierce

    def special(self, loss):
        for c in range(len(self.SPE) // 2):
            if self.SPE[c * 2 - 2] == 2:
                if self.pierce[0] < 1:
                    if self.H > 1:
                        if self.SPE[c * 2 - 1] > 1:
                            self.a = pygame.transform.smoothscale(self.I, (
                            int(self.ss[0] * self.SPE[c * 2 - 1]), int(self.ss[1] * self.SPE[c * 2 - 1])))
                            self.ss = self.ss = pygame.Surface.get_size(self.a)
                            self.pierce[1] += 1
                            self.dmg += 2
                        xplosions.append(
                            explode(self.X, self.Y, self.a, self.D[1] / 7 * 30,
                                    10.73 / self.D[1] * self.SPE[c * 2 - 1] * 4 / 7,
                                    0))
                        self.pierce[0] = self.pierce[1]
                        drts.remove(self)
                        druidart.append(self)
                        self.D[0] = ti
                else:
                    self.pierce[0] -= 1
                    self.H += 1
            elif self.SPE[c * 2 - 2] == 3:
                if loss not in thorned and loss.ID > -9:
                    thorned.append(loss)
                    loss.lists.append(thorned)
                    loss.spawn = []
                    loss.SY /= loss.S * 10
                    loss.SX /= loss.S * 10
                    loss.S = 0.1


minemine = loadify('supermine')


class mine(pygame.sprite.Sprite):
    def __init__(self, X, Y, S, s, H, x, y, P, LS, SPE, dmg):
        super(mine, self).__init__()
        global minemine
        mines.append(self)
        self.I = minemine
        self.dmg = dmg
        self.a = pygame.transform.rotate(self.I, random.randint(-180, 180))
        self.x = 0
        self.y = 0
        self.s = s
        self.LS = LS
        self.S = S
        self.ss = pygame.Surface.get_size(self.I)
        self.H = H
        self.SPE = SPE
        self.X = X
        self.Y = Y
        self.P = P
        ss = pygame.Surface.get_size(self.a)
        self.siz = (ss[0] + ss[1]) / 5
        self.V = int(ss[0] / 2)
        self.C = int(ss[1] / 2)

    def special(self, loss):
        pass

    def xplod(d):
        xplosions.append(explode(d.x+d.V, d.y+50+d.C, d.P[2], d.P[0]))
        for c in bloons:
            if c not in murder:
                if distanceB(c.X, c.Y, d.X, d.Y+50, d.P[0] + c.siz):
                    if c.armr < d.P[1]:
                        if int(d.P[1]) > 0:
                            c.hploss(int(d.P[1]) - c.armr)


class Drt2(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, H, LS, PR, CR, f, P, dmg=1):
        super(Drt2, self).__init__()
        self.CR = CR
        self.PR = PR
        self.dmg = dmg
        self.f = f
        self.P = P
        self.I = I
        self.a = self.I
        self.LS = LS
        self.H = H
        self.ss = pygame.Surface.get_size(self.a)
        self.X = X
        self.Y = Y
        self.a = pygame.transform.rotate(self.I, random.randint(0, 1800) / math.pi)
        self.V = int(self.ss[0] / 2)
        self.C = int(self.ss[1] / 2)

yeano = 1
rndbloon = []
cart=loadify('blooncart')
lightning=loadify('lightining')

class Bloon(pygame.sprite.Sprite):
    def __init__(self, X, Y, S, H, f, r, ID, h, HH, spawn=[], armr=0, EY=0, sent=0,deathrattle=0):
        super(Bloon, self).__init__()
        global power, POWER, yeano
        blns.append(self)
        self.lists=[]
        self.lists.append(blns)
        self.n = [e for e in blntrac]
        self.armr = armr
        if deathrattle==0:
            self.ondeath = []
        else:
            self.ondeath =deathrattle
        self.EX = 0
        self.made = sent
        if sent == 0:
            rndbloon.append(self)
            self.lists.append(rndbloon)
        self.spawn = spawn
        self.EY = EY
        self.ID = ID
        self.H = H
        self.r = r
        # if self.ID==-8:
        #     #force.append(self)
        #     self.PO=[POWER,POWER]
        #     self.po=[power,0]
        #     self.I=spe[2]
        #     self.ID=-3
        #     self.r=0
        self.h = h
        self.HH = HH
        if self.r > 0:
            growbloon.append(self)
            self.lists.append(growbloon)
            if self.ID > -1:
                self.i = B
                self.I = self.i[self.H - 1]
            elif self.ID == -1:
                self.I = spe[1]
            elif -1 > self.ID > -7:
                self.i = B
                self.I = B[-self.ID + 3]
        elif self.ID > -1:
            self.i = [e for e in A]
            self.I = self.i[self.H - 1]
        elif self.ID == -1:
            self.I = spe[0]
        elif self.ID == -10:
            self.I = bossI
            self.img = bossI
        elif -1 > self.ID > -7:
            self.I = A[-self.ID + 3]
        elif self.ID == -9:
            self.I = cart
        elif self.ID == -11:
            self.I = boss2
            self.img = boss2
        self.X = X
        self.Y = Y
        self.f = f
        ss = pygame.Surface.get_size(self.I)
        self.s = pygame.Surface.get_size(self.I)
        self.siz = (ss[0] + ss[1]) / 4
        self.T = (ss[0] / 2)
        self.R = (ss[1] / 2)
        self.f = f
        self.x = -50
        self.y = 50
        self.SX = 0
        self.SY = 0
        self.S = S
        self.q = self.I

    def hploss(self, loss):
        global hploss, money, rel, POWER, power
        if self not in murder:
            if self.ID == 1:
                self.H -= int(loss)
                self.HH -= int(loss)
                if self.H < 1:
                    murder.append(self)
                    self.lists.append(murder)
                    rel = 0
                else:
                    self.SX /= self.S
                    self.SY /= self.S
                    self.S = speed(self.H) / 5
                    self.SX *= self.S
                    self.SY *= self.S
                    self.I = self.i[self.H - 1]
            else:
                self.H -= loss
                if self.H < 1:
                    if not self.spawn == []:
                        for c in self.spawn:
                            for e in range(c[0]):
                                self.make(c[1], self.H)
                    murder.append(self)
                    self.lists.append(murder)
                    rel = 0
                # elif self.ID>0:
                #     self.SX/=self.S
                #     self.SY/=self.S
                #     self.S = speed(self.H)/5
                #     self.SX*=self.S
                #     self.SY*=self.S
                #     self.I = self.i[self.H-1]

    def make(self, which, overkill):
        bloonlistdingus = [[2, 1, 1, 1, []], [4, 2, 2, 1, []], [6, 3, 3, 1, []], [8, 4, 4, 1, []],
                           [10, 5, 5, 1, []],
                           [0, 1, 6, -2, [[2, 4]]], [9, 4, 7, -3, [[1, 5], [1, 8]]],
                           [10, 5, 8, -4, [[1, 5], [4, 2]]],
                           [15, int(6 + rn / 10), int(6 + rn / 10), -1, []],
                           [10, 20, 9, -5, [[5, 5]]], [7, int(20 + rn / 12), 10, -6, [[4, 5]], 1],
                           [16, rn + 65, 0, -11, [[4, 9]]],
                           [3, rn * 3 + 120, 0, -10, [[4, 11]]]]
        what = bloonlistdingus[which]

        if int(what[2] + overkill) > 0:
            if what[3] > -10:
                what[0] += min(rn, 60) / 5
            # what = [speed,health,HH(wierdhelf),ID,spawn,EX,EY]

            if len(what) > 5:
                armour = what[5]
            else:
                armour = 0
            newbloon = Bloon(self.X + random.randint(-70, 70), self.Y + random.randint(-70, 70), (what[0]) / 5
                             , what[1], self.f
                             , self.r, what[3], self.h, what[2], what[4], armour, 0, self.made)
            bloons.append(newbloon)
            newbloon.lists.append(bloons)
            if self in burning:
                burning.append(newbloon)
                newbloon.lists.append(burning)
                newbloon.firetick = self.firetick
                newbloon.firedmg = self.firedmg
            if overkill < 0:
                newbloon.hploss(-overkill)

    def die(e):
        global lightning
        for b in range(len(e.ondeath)):
            if e.ondeath[b][1] == 0:
                xplosions.append(explode(e.x, e.y,lightning, e.ondeath[b][0][1],2,5))
                for c in bloons:
                    if distanceB(c.X, c.Y, e.x, e.y,e.ondeath[b][0][1]*2 + c.siz):
                        if c.armr < e.ondeath[b][0][0]:
                            if int(e.ondeath[b][0][0]) > 0:
                                c.hploss(int(e.ondeath[b][0][0]) - c.armr)
        for g in e.lists:
            g.remove(e)

    def grow(e, howmuch=1):
        if e not in murder:
            if e.HH < e.h:
                e.HH += min(howmuch, e.h - e.HH)
                if e.HH > 5 and not e.ID == -1:
                    forms = [[0, 1, -2, [[2, 4]]], [9, 4, -3, [[1, 5], [1, 8]]], [10, 5, -4, [[1, 5], [4, 2]]],
                             [10, 20, -5, [[5, 5]]], [7, int(20 + rn / 12), -6, [[4, 5]], 1]]

                    if e.HH > 6:
                        e.HH = e.h
                    form = forms[e.HH - 6]
                    e.ID = form[2]
                    e.spawn = form[3]
                    e.H = form[1]
                    e.SX /= e.S
                    e.SY /= e.S
                    e.S = (form[0] + rn / 5) / 5
                    e.SX *= e.S
                    e.SY *= e.S
                    e.I = B[e.HH - 1]
                    if len(form) > 4:
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

                elif e.ID > 0:
                    e.H = e.HH
                    e.I = e.i[e.H - 1]
                    e.SX /= e.S
                    e.SY /= e.S
                    e.S = speed(e.H) / 5
                    e.SX *= e.S
                    e.SY *= e.S
                else:
                    e.H = e.HH


class explode(pygame.sprite.Sprite):
    def __init__(self, X, Y, i, T, howfast=1, strt=60):
        super(explode, self).__init__()
        self.i = i
        for e in range(3):
            if e == i:
                self.i = explod[i][0]
                animations.append(self)
                self.ii = explod[i]
                self.faze = 0

        self.X = X
        self.Start = strt
        self.Y = Y
        self.T = T
        self.S = howfast
        self.s = pygame.Surface.get_size(self.i)
        self.I = loadify('noth')
        self.t = 0


druids = []


class Druid(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, f, F, DS, c, SPE):
        super(Druid, self).__init__()
        monks.append(self)
        self.MID = 5
        self.c = c
        self.DS = DS
        self.C = ti
        self.bounce = 0
        self.price = 45
        self.D = DS * 100
        self.I = I
        self.f = f
        self.price = 40
        self.SPE = SPE
        self.F = F
        self.X = X
        self.Y = Y
        self.XX = X
        self.YY = Y
        self.ID = loadify("druidball")
        self.H = 2
        self.pierce = [0, 0]
        self.P = [0]
        self.dmg = 3


def drtM():
    for e in drts:
        e.X += e.S
        e.Y += e.s
        e.x = int(e.X)
        e.y = int(e.Y)

        if not 0 < e.X < 1800 + e.ss[0] / 2:
            if e.b < 1:
                e.kill()
                drts.remove(e)
                del e
            else:
                e.b -= 1
                e.S *= -1
        elif not 0 < e.Y < 1200 + e.ss[1] / 2:
            if e.b < 1:
                e.kill()
                drts.remove(e)
                del e
            else:
                e.b -= 1
                e.s *= -1

        else:
            for d in range(int(1 + (min((int((e.X + e.ss[0]) // sqaresize), maxsqare)) - int(e.X // sqaresize)))):
                for i in range(int(1 + (min(int(e.Y + e.ss[1] // sqaresize), 11) - int(e.Y // sqaresize)))):
                    sqares2[min(len(sqares2)-1,int((e.X + d * sqaresize) // sqaresize + (
                                min(e.Y, h) + i * sqaresize) // sqaresize * maxsqare) - 1)].append(e)

        # sqares2[int((e.X + e.ss[0]) // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(e)
        #
        # if e not in sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)]:
        #     sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
        #
        # if e not in sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)]:
        #     sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
        #
        # if e not in sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)]:
        #     sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(e)

stopround=0
def moida():
    global money, income, rn, locked,stopround
    for b in range(len(murder)):
        e = murder[0]
        e.die()
        # e = murder[0]
        # murder.remove(e)
        # if e in blns:
        #     blns.remove(e)
        #     bloons.remove(e)
        #     if e in rndbloon:
        #         rndbloon.remove(e)
    if stopround==0:
        if rndbloon == []:
            stopround=1
            money += income
            rn += 1
            locked += 1
            ready()
        #     if e in thorned:
        #         thorned.remove(e)
        #     if e in burning:
        #         burning.remove(e)
        #     if e in force:
        #         force.remove(e)
        #     if e in growbloon:
        #         growbloon.remove(e)
        # e.kill()


nspd = 0
nespd = 0
newspd = 0
spe = [loadify('purple'), loadify('regpur'), loadify('blnSHA'), loadify('blnSH'), loadify('blooncart')]
health = 100
ss = 0
SS = 0


def blnM():
    global health, bloon, blns, drts2, sqares, Bloondamage
    for e in blns:
        if e not in murder:
            if e.SY == 0:
                e.IM = 0
                e.SX = 0
                xS = e.n[e.f - 1] - e.X
                yS = e.n[e.f] - e.Y
                if xS == 0:
                    e.SX = e.S
                    e.SY = 0.0001
                else:
                    e.SX = e.S / math.sqrt(yS ** 2 / xS ** 2 + 1)
                    if xS < 0:
                        e.SX *= -1
                    e.SY = e.SX * yS / xS
                if e.ID < -9:
                    if e.SX == 0:
                        if e.SY < 0:
                            e.I = pygame.transform.rotate(e.img, -90)
                        else:
                            e.I = pygame.transform.rotate(e.img, 90)
                    elif e.SX > 0:
                        e.I = pygame.transform.rotate(e.img, -math.atan(e.SY / e.SX) * 180 / math.pi)
                    else:
                        e.I = pygame.transform.rotate(e.img, 180 - math.atan(e.SY / e.SX) * 180 / math.pi)
                    ss = pygame.Surface.get_size(e.I)
                    e.EX = int(ss[0] / 2)
                    e.EY = int(ss[1] / 2)
                    e.T = 0
                    e.R = 0

            e.X += e.SX
            e.Y += e.SY
            e.x = int(e.X)
            e.y = int(e.Y)
            if e not in drts2:
                if e.X > 0:
                    for d in range(int(1 + (min((int((e.X + e.s[0]) // sqaresize), maxsqare)) - int(e.X // sqaresize)))):
                        for i in range(int(1 + (min(int(e.Y + e.s[1] // sqaresize), 11) - int(e.Y // sqaresize)))):
                            sqares[int((e.X + d * sqaresize) // sqaresize + (
                                    e.Y + i * sqaresize) // sqaresize * maxsqare) - 1].append(e)
                    # for d in range(min(int(1 + (int((e.X + e.s[0]) // sqaresize - int(e.X // sqaresize)))), maxsqare)):
                    #     for i in range(min(int(1 + (int((e.Y + e.s[1]) // sqaresize - int(e.Y // sqaresize)))), 11)):
                    #         sqares[int((e.X + d * sqaresize) // sqaresize + (e.Y + i * sqaresize) // sqaresize * maxsqare)-1].append(e)
                    # sqares[int((e.X + e.s[0]) // sqaresize + (e.Y + e.s[1]) // sqaresize * maxsqare)].append(e)
                    # if e not in sqares[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)]:
                    #     sqares[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
                    # if e not in sqares[int((e.X + e.s[0]) // sqaresize + e.Y // sqaresize * maxsqare)]:
                    #     sqares[int((e.X + e.s[0]) // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
                    # if e not in sqares[int(e.X // sqaresize + (e.Y + e.s[1]) // sqaresize * maxsqare)]:
                    #     sqares[int(e.X // sqaresize + (e.Y + e.s[1]) // sqaresize * maxsqare)].append(e)
            else:
                for d in range(int(1 + (min((int((e.X + e.ss[0]) // sqaresize), maxsqare)) - int(e.X // sqaresize)))):
                    for i in range(int(1 + (min(int(e.Y + e.ss[1] // sqaresize), 11) - int(e.Y // sqaresize)))):
                        sqares2[int((e.X + d * sqaresize) // sqaresize + (
                                    e.Y + i * sqaresize) // sqaresize * maxsqare) - 1].append(e)
                # for d in range(min(int(1 + (int((e.X + e.ss[0]) // sqaresize - int(e.X // sqaresize)))), maxsqare)):
                #     for i in range(min(int(1 + (int((e.Y + e.ss[1]) // sqaresize - int(e.Y // sqaresize)))), 11)):
                #         sqares2[
                #             int((e.X + d * sqaresize) // sqaresize + (e.Y + i * sqaresize) // sqaresize * maxsqare)-1].append(
                #             e)
                # sqares2[
                #     int((e.X + e.ss[0]) // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(
                #     e)
                # if e not in sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)]:
                #     sqares2[int(e.X // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
                # if e not in sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)]:
                #     sqares2[int((e.X + e.ss[0]) // sqaresize + e.Y // sqaresize * maxsqare)].append(e)
                # if e not in sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)]:
                #     sqares2[int(e.X // sqaresize + (e.Y + e.ss[1]) // sqaresize * maxsqare)].append(e)
            if distanceB(e.X, e.Y, e.n[e.f - 1], e.n[e.f], 10):
                e.SY = 0
                if e.ID == 99:
                    e.f -= 2
                    if e.f < 1:
                        blns.remove(e)
                        for b in sqaresa:
                            if e in b:
                                b.remove(e)
                        drts2.remove(e)
                        e.kill()
                        del e
                else:
                    e.f += 2
                    if e.f > len(e.n)-1:
                        health -= e.H
                        murder.append(e)
                        e.lists.append(murder)

                        e.f = 0
                        if health < 0:
                            death(100, h // 2 - 200)


power = 0
POWER = 0
xplosions = []
ti = 0
xS = 0
spc = 15
yS = 0
blntrac2=[]
blntrac1 = [152, 215,385, 215, 385, 110, 1245, 120, 1565, 325, 1565, 620, 1035, 620, 1035, 365, 860, 365, 860, 525, 395, 525, 395, 1075]
spdx = 0
elo = 0
spdy = 0
A = [loadify('bloon'), loadify('blnB'), loadify('blngreen')
    , loadify('blnyellow'), loadify('blnpink'), loadify('blnblac')
    , loadify('tigerP'), loadify('tigerG'), loadify('blackrockbloon'), loadify('platebloon')]
B = [loadify('regred'), loadify('regblu'), loadify('reggrn')
    , loadify('regyel'), loadify('regpin'), loadify('regbla')
    , loadify('regpu2'), loadify('reggr2'), loadify('regblackrockbloon'), loadify('regplate')]
force = []
drtmonks = []
drts = []
enginers = []
bossH = 0
bossX = 0
bossY = 0
bloondelay=[]

def arrivetime(thing):
    return thing.X
def sendbloon(stuff):
    global bloons, money, income,stopround,CheaterPowers,bloondelay
    if CheaterPowers==0:
        # what is speed,health,HH,ID,spawn,armour,deathrattle
        bloonlistcomplete = [[2, 1, 1, 1, []], [4, 2, 2, 1, []], [6, 3, 3, 1, []], [8, 4, 4, 1, []], [10, 5, 5, 1, []],
                             [0, 1, 6, -2, [[2, 4]]], [9, 4, 7, -3, [[1, 5], [1, 8]]], [10, 5, 8, -4, [[1, 5], [4, 2]]],
                             [15, int(6 + rn / 10), int(6 + rn / 10), -1, []]
                             ,[7, int(25+rn//12), 0, -9, [],0.4,[[[int(25+rn//12)/3,50],0]]],[10, 20+ rn / 6, 9, -5, [[5, 5]]],
                             [7, int(20 + rn / 12), 10, -6, [[4, 5]], 1],
                             [16, rn + 50, 0, -11, [[4, 9]]],
                             [3, rn * 3 + 100, 0, -10, [[4, 11]]]]
        what = bloonlistcomplete[stuff[1]]
        if what[3] > -10:
            what[0] += min(rn, 60) / 5
        if len(stuff) > 3:
            sent = 0
            stopround = 0
            spc = stuff[3]
        else:
            spc = 5
            sent = 1
        if len(what) > 5:
            armour = what[5]
        else:
            armour = 0
        if len(what) > 6:
            deathrattle=what[6]
        else:
            deathrattle=[]
        if what[3]<-8:
            regrow=0
        else:
            regrow=stuff[2]
        for e in range(stuff[0]):
            bloondelay.append(Bloon(e * spc+ti, blntrac[1], (what[0]) / 5
                                , what[1], 1
                                , regrow, what[3], what[2], what[2], what[4], armour, 0, sent,deathrattle))
        bloondelay=sorted(bloondelay,key=arrivetime)
    else:
        stopround = 0
        bloonmade=Bloon(50, 150, 1, 1, 1, 0, 1, 1, 0)
        bloonmade.lists.append(bloons)
        bloons.append(bloonmade)


income = 50


def roundshow(x, y, l):
    dead = fint.render("round" + str(l), True, (0, 255, 0))
    screen.blit(dead, (x, y))


def hpshow(x, y):
    hhp = font.render("health:" + str(health), True, (0, 255, 0))
    screen.blit(hhp, (x, y))
    kii = font.render("money:" + str(int(money)), True, (0, 255, 0))
    screen.blit(kii, (x, y + 25))
    kii = font.render("income:" + str("{:.1f}".format(income)), True, (0, 255, 0))
    screen.blit(kii, (x, y + 50))


rn = 5
speeed = 0
hippo = 0
heredy = 0
headers = {'Content-type': 'application/json'}


def ready():
    global heredy, thorned, growbloon, burning
    mapspecial()
    roundshow(100, 500, rn - 3)
    pygame.display.update()
    connection.Send(
        {"action": "ready"})
    # r = requests.post('http://' + ipadress + ':5000/sendready', headers=headers,
    #                   data=jsonpickle.encode([me.ID,1]))


cl = 1
blow=loadify('leafblowah')

def upgrade():
    global cl, price, lvlup, drtmonks, money, druids,blow
    cl = 1
    menu()
    for e in lvlup:
        menuAB(e.MID, e.F, e.f)
        sell(e.price)

    pygame.display.update()
    while cl == 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                XX = pygame.mouse.get_pos()
                if 450 > XX[0] > 200:
                    if 350 > XX[1]:
                        cl = 0

                if XX[0] > 1100:
                    if 450 > XX[1]:
                        if e.MID == 1:
                            if e.F == 0:
                                if money > 29:
                                    for e in lvlup:
                                        e.c = e.c / 2
                                        e.DS = e.DS * 2
                                        e.F = 1
                                        money -= 30
                                        if e.f < 2:
                                            e.I = loadify('drtmonkS')
                                            e.ID = loadify('drtS')
                                        cl = 0
                            elif e.F == 1:
                                if money > 99:
                                    for e in lvlup:
                                        e.F = 2
                                        money -= 100
                                        e.Q = 0.5
                                        cl = 0
                            elif e.F == 2 and e.f < 3:
                                if money > 109:
                                    for e in lvlup:
                                        e.DS += 10
                                        e.F = 3
                                        money -= 110
                                        e.ID = loadify('drtex')
                                        e.I = loadify('cyborg')
                                        e.P = [80, 1, 1]
                                        cl = 0
                            elif e.F == 3 and e.f < 3:
                                if money > 399:
                                    for e in lvlup:
                                        e.F = 4
                                        money -= 400
                                        e.ID = loadify('drtbomb')
                                        e.I = loadify('bombsuit')
                                        e.P = [160, 1, 1]
                                        e.SPX.append(4)
                                        e.SPX.append([e.c, 1])
                                        cl = 0

                        elif e.MID == 2:
                            if e.F == 0:
                                if money > 49:
                                    for e in lvlup:
                                        e.F = 1
                                        if e.I == enginer:
                                            e.I = loadify('engineer2')
                                            e.MI = loadify('turret2b')
                                        money -= 50
                                        e.Q = 0.5
                                        cl = 0
                            elif e.F == 1:
                                if money > 169:
                                    for e in lvlup:
                                        e.F = 2
                                        e.I = loadify('grmn')
                                        e.MI = loadify('tureetb')
                                        e.ID = loadify('explodrt')
                                        e.P = [50, 1, 1]
                                        money -= 170
                                        cl = 0

                        elif e.MID == 3:
                            if e.F == 0:
                                if money > 69:
                                    for e in lvlup:
                                        e.F = 1
                                        e.c /= 2
                                        money -= 70
                                        cl = 0
                            elif e.F == 1:
                                if money > 74:
                                    for e in lvlup:
                                        e.F = 2
                                        money -= 75
                                        cl = 0
                        elif e.MID == 4:
                            if e.F == 0:
                                if money > 199:
                                    for e in lvlup:
                                        if e.f < 2:
                                            e.I = loadify('double')
                                        else:
                                            e.I = loadify('doublewide')
                                        e.F = 1
                                        money -= 200
                                        cl = 0
                            elif e.F == 1:
                                if money > 199:
                                    for e in lvlup:
                                        if e.f < 2:
                                            e.I = loadify("triple")
                                        else:
                                            e.I = loadify('triplewide')

                                        e.F = 2
                                        money -= 200
                                        cl = 0
                            elif e.F == 2:
                                if money > 4499:
                                    for e in lvlup:
                                        if e.f < 2:
                                            e.I = loadify('tank')
                                        else:
                                            e.I = loadify('tankwide')
                                        e.H += 6
                                        e.dmg += 1
                                        g = pygame.Surface.get_size(e.ID)
                                        e.ID = pygame.transform.smoothscale(loadify('blcdrt'), (g[0], g[1]))
                                        e.DS *= 3
                                        e.F = 3
                                        e.c /= 1.5
                                        money -= 4500
                                        cl = 0
                        elif e.MID == 5:
                            if e.F == 0:
                                if money > 39:
                                    for e in lvlup:
                                        e.H += 10
                                        money -= 40
                                        if e.f == 0:
                                            e.I = loadify('druid2')
                                        elif e.f == 1:
                                            e.I = loadify('druid3')
                                        e.F = 1
                                        cl = 0
                            elif e.F == 1:
                                if money > 379:
                                    for e in lvlup:
                                        money -= 380
                                        e.DS += 1
                                        e.D /= 1.2
                                        e.c /= 1.75
                                        for y in range(len(e.SPE)):
                                            if e.SPE[y - 1] == 2:
                                                e.SPE[y] += 0.2
                                        if e.f == 0:
                                            e.I = loadify('druid5')
                                        else:
                                            e.I = loadify('druid6')
                                        e.F = 2
                                        cl = 0
                        elif e.MID == 6:
                            if e.F == 0:
                                if money > 59:
                                    for e in lvlup:
                                        e.Q = 0.2
                                        e.power=1
                                        e.blow*=1.5
                                        money -= 60
                                        e.i = blow
                                        e.I = blow
                                        e.F = 1
                                        cl = 0
                    elif 900 > XX[1]:
                        if e.MID == 1:
                            if e.f == 0 and e.dmg == 1:
                                if money > 39:
                                    e.f = 1
                                    money -= 40
                                    e.dmg += 1
                                    cl = 0
                            elif e.f == 1:
                                if money > 39:
                                    for e in lvlup:
                                        e.c = e.c + 2
                                        e.DS = e.DS - 5
                                        if e.F > 0:
                                            e.DS -= 5
                                        if e.DS < 2:
                                            e.c = 10000000
                                        e.H += +2
                                        e.f = 2
                                        money -= 40
                                        if e.F < 3:
                                            e.I = loadify('beefdrtmonk')
                                            e.ID = loadify('beefdrt')
                                        cl = 0
                            elif e.f == 2 and e.F < 3:
                                if money > 99:
                                    for r in range(9):
                                        r += 1
                                        if e.F > 0:
                                            r *= 2
                                        if r * 1.5 < e.DS:
                                            e.H += 1
                                        else:
                                            break
                                    if e.F > 0:
                                        e.DS += 4
                                    else:
                                        e.DS += 2
                                    e.H += 3
                                    e.f = 3
                                    money -= 100
                                    e.ID = loadify('beefyerdrt')
                                    e.I = loadify('gorrila')
                                    cl = 0

                        elif e.MID == 2:
                            if e.f == 0:
                                if money > 49:
                                    for e in lvlup:
                                        e.f = 1
                                        money -= 50
                                        e.c -= e.c / 2.5
                                        e.c = int(e.c)
                                        if e.I == enginer:
                                            e.I = loadify('engineer2')
                                        cl = 0
                            elif e.f == 1:
                                if money > 79:
                                    for e in lvlup:
                                        e.f = 2
                                        money -= 80
                                        e.I = loadify('time')
                                        e.MI = wata
                                        e.SPE = [1, 1]
                                        cl = 0

                        elif e.MID == 3:
                            if e.f == 0:
                                if money > 249:
                                    for e in lvlup:
                                        e.f = 1
                                        money -= 250
                                        e.P = [35, 1, 1]
                                        e.ID = loadify('mineS')
                                        e.Dmg += 1
                                        cl = 0
                            elif e.f == 1:
                                if money > 999:
                                    for e in lvlup:
                                        e.f = 2
                                        money -= 1000
                                        cl = 0
                                        e.G = 0

                        elif e.MID == 4:
                            if e.f == 0:
                                if money > 299:
                                    g = pygame.Surface.get_size(e.ID)
                                    e.ID = pygame.transform.smoothscale(e.ID, (int(g[0] * 1.2), int(g[1] * 1.2)))
                                    money -= 300
                                    e.f += 1
                                    e.H += 1
                                    e.c *= 1.2
                                    if e.DS > 7:
                                        e.dmg += 1
                                    e.DS /= 1.2
                                    cl = 0
                            elif e.f == 1:
                                if money > 399:
                                    if e.F == 0:
                                        e.I = loadify("gunnerwide")
                                    elif e.F == 1:
                                        e.I = loadify("doublewide")
                                    elif e.F == 2:
                                        e.I = loadify("triplewide")
                                    elif e.F == 3:

                                        e.I = loadify("tankwide")
                                    money -= 400
                                    e.f += 1
                                    e.DS *= 1.2
                                    e.c /= 1.4
                                    cl = 0


                        elif e.MID == 5:
                            if e.f == 0:
                                if money > 49:
                                    for e in lvlup:
                                        e.f = 1
                                        money -= 50
                                        e.SPE.append(3)
                                        e.SPE.append(0)
                                        if e.F == 0:
                                            e.I = loadify('druid02')
                                        elif e.F == 1:
                                            e.I = loadify('druid3')
                                        elif e.f == 1:
                                            e.I = loadify('druid6')
                                        e.dmg += 3
                                        e.pierce = [1, 1]
                                        e.H += 1
                                        cl = 0
                            elif e.f == 1:
                                if money > 89:
                                    for e in lvlup:
                                        e.f = 2
                                        money -= 90
                                        e.bounce += 4
                                        cl = 0
                            elif e.f == 1:
                                if money > 89:
                                    for e in lvlup:
                                        e.SPE.append(3)
                                        e.SPE.append(0)
                                        e.f = 2
                                        money -= 90
                                        e.bounce += 2
                                        cl = 0
                        elif e.MID == 6:
                            if e.f == 0:
                                if money > 49:
                                    for e in lvlup:
                                        e.f = 1
                                        money -= 50
                                        drtmonks.append(e)
                                        e.c=((e.rang)**2)/470
                                        e.price+=40
                                        if e.F == 0:
                                            e.I = loadify('druid02')
                                        elif e.F == 1:
                                            e.I = loadify('druid3')
                                        elif e.f == 1:
                                            e.I = loadify('druid6')
                                        cl = 0
                    else:
                        for e in lvlup:
                            money += price
                            if e.MID == 1:
                                drtmonks.remove(e)
                                drtmunks.remove(e)
                            elif e.MID == 2:
                                enginers.remove(e)
                            elif e.MID == 3:
                                factories.remove(e)
                            elif e.MID == 4:
                                gunners.remove(e)
                            if e.MID == 5:
                                druids.remove(e)
                            if e.MID == 6:
                                if e in drtmonks:
                                    drtmonks.remove(e)
                                leafs.remove(e)
                            e.kill()
                            monks.remove(e)
                            del e
                            cl = 0

    lvlup = []


price = 0


def sell(insta):
    global price
    price = insta
    sold = flont.render("sell for " + str(price), True, (0, 0, 0))
    screen.blit(sold, (1150, 945))


def menu():
    screen.blit(loadify('menu'), (0, 0))


def menuAB(MT, UPGNUM, PGNUM):
    if MT == 1:
        if UPGNUM == 0:
            screen.blit(loadify('menuspd'), (1100, 0))
        elif UPGNUM == 1:
            screen.blit(loadify('doubleshot'), (1100, 0))
        elif PGNUM > 2:
            screen.blit(loadify('nope'), (1100, 0))
        elif UPGNUM == 2:
            screen.blit(loadify('explodedrt'), (1100, 0))
        elif UPGNUM == 3:
            screen.blit(loadify('incendiary'), (1100, 0))
    if MT == 2:
        if UPGNUM == 0:
            screen.blit(loadify('turretmenu'), (1100, 0))
        elif UPGNUM == 1:
            screen.blit(loadify('gears'), (1100, 0))
    if MT == 3:
        if UPGNUM == 0:
            screen.blit(loadify('menFspikes'), (1100, 0))
        elif UPGNUM == 1:
            screen.blit(loadify('crawls'), (1100, 0))
    if MT == 4:
        if UPGNUM == 0:
            screen.blit(loadify('barrel'), (1100, 0))
        elif UPGNUM == 1:
            screen.blit(loadify('barells'), (1100, 0))
        elif UPGNUM == 1:
            screen.blit(loadify('barells'), (1100, 0))
        elif UPGNUM == 2:
            screen.blit(loadify('tankmen'), (1100, 0))
    if MT == 5:
        if UPGNUM == 0:
            screen.blit(loadify('regrowth'), (1100, 0))
        elif UPGNUM == 1:
            screen.blit(loadify('druidbook'), (1100, 0))
    if MT == 6:
        if UPGNUM == 0:
            screen.blit(loadify('powah'), (1100, 0))

    if MT == 1:
        if PGNUM == 0:
            screen.blit(loadify('sharper'), (1100, 450))
        elif PGNUM == 1:
            screen.blit(loadify('beefmen'), (1100, 450))
        elif UPGNUM > 2:
            screen.blit(loadify('nope'), (1100, 450))
        elif PGNUM == 2:
            screen.blit(loadify('beefyermenu'), (1100, 450))

    if MT == 2:
        if PGNUM == 0:
            screen.blit(loadify('spannermen'), (1100, 450))
        if PGNUM == 1:
            screen.blit(loadify('timemen'), (1100, 450))

    if MT == 3:
        if PGNUM == 0:
            screen.blit(loadify('menmne'), (1100, 450))
        elif PGNUM == 1:
            screen.blit(loadify('minemen'), (1100, 450))
    if MT == 4:
        if PGNUM == 0:
            screen.blit(loadify('larger'), (1100, 450))
        elif PGNUM == 1:
            screen.blit(loadify('greatbarrel'), (1100, 450))
    if MT == 5:
        if PGNUM == 0:
            screen.blit(loadify('brambles'), (1100, 450))
        if PGNUM == 1:
            screen.blit(loadify('bouncy'), (1100, 450))
    if MT == 6:
        if PGNUM == 0:
            screen.blit(loadify('nailing'), (1100, 450))
branch = loadify("thorns")
thorned = []
burning = []


def bloon():
    for e in bloons:
        screen.blit(e.I, (e.x - e.EX-e.T, e.y - e.EY-e.R))
    for b in thorned:
        screen.blit(pygame.transform.smoothscale(branch, (b.s[0], b.s[1])), (b.x - b.EX, b.y - b.EY))
    for c in burning:
        c.firetick[0] += 1
        if c.firetick[0] > c.firetick[1]:
            c.firetick[0] = 0
            c.hploss(c.firedmg + c.armr)
        screen.blit(
            pygame.transform.scale(fire[int(c.firetick[0] / c.firetick[1] * (len(fire) - 1))], (c.s[0], c.s[1])),
            (c.x, c.y))


def drtmonk():
    for e in drtmunks:
        screen.blit(e.I, (e.X, e.Y))
    for e in leafs:
        screen.blit(e.I, (e.X-e.ss[0]//2, e.Y-e.ss[1]//2))
    for e in druids:
        screen.blit(e.I, (e.X, e.Y))


def engeneer():
    for e in enginers:
        screen.blit(e.I, (e.X, e.Y))


def Factory():
    for e in factories:
        screen.blit(e.I, (e.X, e.Y))


def drt():
    for e in drts:
        screen.blit(e.a, (e.x - e.V, e.y - e.C))
    for e in drts2:
        screen.blit(e.a, (e.X- e.V, e.Y- e.C+50))
    for e in gunners:
        screen.blit(e.IB, (e.X - e.EX, e.Y - e.EY))
    for e in xplosions:
        screen.blit(e.I, (int(e.X - e.s[0] / 2), int(e.Y - e.s[1] / 2)))


choecko = loadify('spikes')
gold = loadify('gold')
bossI = loadify('blnboss')
boss2 = loadify('capsule')
rel = 1


def distanceB(eneX, eneY, bulX, bulY, o):
    distance = math.sqrt((math.pow(eneX - bulX, 2)) + (math.pow(eneY - bulY, 2)))
    if distance < o:
        return True


def distanceC(eneX, eneY, bulX, bulY):
    distance = math.sqrt((math.pow(eneX - bulX, 2)) + (math.pow(eneY - bulY, 2)))
    return distance




bl = 10


def paused(x, y):
    paus = font.render("paused, press any key to resume", True, (0, 255, 0))
    screen.blit(paus, (x, y))


paus = 1


def pause():
    global paus
    paus = 1
    while paus == 1:
        global pas
        if (time.time() - pas) > 1:
            paused(10, 10)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                paus = 0


monksel = [loadify('drtmonk'), loadify('engineer')
    , loadify('spikefac'), loadify('gunner'), loadify('smoldruid'),loadify('leafblower')]


def death(x, y):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        dead = fint.render("U died on round:" + str(rn - 4), True, (255, 0, 0))
        screen.blit(dead, (x, y))
        pygame.display.update()


io = 0


def speed(ch):
    if ch == 10 + rn / 10:
        speeeed = rn / 5 + 15
    else:
        if ch == 6:
            ch = 0
        speeeed = rn / 5 + ch * 2
    return speeeed


TL = [loadify('turret'), loadify('turretb'), loadify('turret2b'), loadify('turret2')
    , loadify('tureetb'), loadify('tureet'), loadify('waterb'), loadify('water')]

pliesX = 0
spikX = 0
cf = 0
explod1 = []
explod2 = []
explod3 = []
fire = []
for e in range(74):
    fire.append(loadanimation("feuer", 't' + str(e)))
for e in range(25):
    explod1.append(loadanimation("boombiatch", 't' + str(e)))
for e in range(104):
    explod3.append(loadanimation("explosion2", 't' + str(e)))
for e in range(98):
    explod2.append(loadanimation("explosion", 'tt' + str(e)))
explod = [explod1, explod2, explod3]

spikY = 0
pliesY = 0
leafs=[]
lo = 1
moar = [pygame.transform.smoothscale(loadify('btd map'), (w - 240, h)).get_size(), loadify('btd map').get_size()]
tracY = [170, 170, 170, 170, 170, 170, 131, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114, 114,
         114, 120, 147, 173, 200, 226, 252, 279, 305, 347, 397, 447, 497, 547, 597, 611, 612, 613, 613, 614, 615, 616,
         617, 618, 619, 602, 552, 502, 452, 402, 368, 365, 362, 365, 415, 465, 510, 511, 512, 513, 514, 515, 516, 517,
         518, 519, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 170, 170, 170]
tracX = [110, 160, 210, 260, 310, 360, 376, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 961, 1011, 1061,
         1111, 1161, 1210, 1252, 1294, 1337, 1379, 1422, 1464, 1507, 1522, 1523, 1525, 1526, 1528, 1529, 1492, 1442,
         1392, 1342, 1292, 1242, 1192, 1142, 1092, 1042, 1009, 1007, 1005, 1003, 1001, 984, 934, 884, 839, 836, 833,
         825, 775, 725, 675, 625, 575, 525, 475, 425, 375, 368, 368, 367, 366, 365, 364, 363, 362, 361, 360, -36, -84,
         -133]
print(moar[0][0])
for e in tracY:
    e *= moar[0][1] / moar[1][1]
for e in tracX:
    e *= moar[0][0] / moar[1][0]
select = 0
spoikX = []
boss = 0
spoikY = []
drts2 = []
locked = 100
lock = loadify("locked")
targetedB = []
targetedF = []
factories = []
images = []
scroll = 0
ploi = 0
CheaterPowers = 0
board = loadify("board")
panelloon = loadify("bloonyroad")
panelsize = pygame.Surface.get_size(panelloon)
panelsize = panelsize[1]
back = pygame.transform.smoothscale(loadify('btd map'), (W, h))
bloonamount = loadify("killerrock")
drts3 = []
bloonumba = 1
bloonprices = [[[1, 0.1], [2, 0.23]], [[2, 0.2], [4, 0.5]], [[3, 0.3], [6, 0.77]], [[4, 0.4], [7, 0.9]],
               [[5, 0.5], [10, 1.3]],
               [[10, 1], [24, 2]], [[14, 1.2], [30, 2.2]], [[14, 1.2], [30, 2.2]], [[10, 0.9], [24, 2]],
               [[80, 2]],[[90, 0.25], [150, 0.5]], [[300, 0], [500, 0]], [[800, 1]], [[1800, -50]]]
chosen=0
yard=pygame.transform.smoothscale(loadify("backyard"), (w, h))
maps=[back,yard]
stopper=loadify("pathstopper")
blntrac2=[215, 434, 1455, 700]
def mapspecial1():
    pass
blunpath=loadify("path")

def mapspecial2():
    global blntrac,images
    images=[]
    blntrac=[blntrac[0],blntrac[1]]
    for e in range(min(len(monks),6)):
        theone=monks[random.randint(0,len(monks)-1)]
        if not blntrac[len(blntrac)-2]==theone.XX:
            blntrac.append(theone.XX)
            blntrac.append(theone.YY)
            xS = (blntrac[len(blntrac) - 2]) - (blntrac[len(blntrac) - 4])
            yS = (blntrac[len(blntrac) - 1]) - (blntrac[len(blntrac) - 3])
            if xS == 0:
                spdx = 100
                spdy = 0
            else:
                spdx = 100 / math.sqrt(yS ** 2 / xS ** 2 + 1)
                if xS < 0:
                    spdx *= -1
                spdy = spdx * yS / xS
            newpathh = pygame.transform.smoothscale(blunpath, (
                int(distanceC(blntrac[len(blntrac) - 2], blntrac[len(blntrac) - 1], blntrac[len(blntrac) - 4],
                              blntrac[len(blntrac) - 3])), 140))

            if spdx == 0:
                if spdy < 0:
                    newpath = pygame.transform.rotate(newpathh, -90)
                else:
                    newpath = pygame.transform.rotate(newpathh, 90)
                extray = 1
            elif spdx > 0:
                newpath = pygame.transform.rotate(newpathh, -math.atan(spdy / spdx) * 180 / math.pi)
            else:
                newpath = pygame.transform.rotate(newpathh, 180 - math.atan(spdy / spdx) * 180 / math.pi)

            if spdx > 0 and spdy > 0:
                extray = math.sin(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
                extrax = math.cos(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
            elif spdx > 0 and spdy < 0:
                extray = math.cos(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
                extrax = math.sin(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
            elif spdx < 0 and spdy < 0:
                extray = math.sin(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
                extrax = math.cos(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
            else:
                extray = math.cos(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
                extrax = math.sin(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
            if xS < 0:
                ximg = blntrac[len(blntrac) - 2]
            else:
                ximg = blntrac[len(blntrac) - 4]
            if yS < 0:
                yimg = blntrac[len(blntrac) - 1]
            else:
                yimg = blntrac[len(blntrac) - 3]
            images.append(Image(newpath, ximg - extrax, yimg - extray))



    blntrac.append(1)
    blntrac.append(1000)
    xS = (blntrac[len(blntrac) - 2]) - (blntrac[len(blntrac) - 4])
    yS = (blntrac[len(blntrac) - 1]) - (blntrac[len(blntrac) - 3])
    if xS == 0:
        spdx = 100
        spdy = 0
    else:
        spdx = 100 / math.sqrt(yS ** 2 / xS ** 2 + 1)
        if xS < 0:
            spdx *= -1
        spdy = spdx * yS / xS
    newpathh = pygame.transform.smoothscale(blunpath, (
        int(distanceC(blntrac[len(blntrac) - 2], blntrac[len(blntrac) - 1], blntrac[len(blntrac) - 4],
                      blntrac[len(blntrac) - 3])), 140))

    if spdx == 0:
        if spdy < 0:
            newpath = pygame.transform.rotate(newpathh, -90)
        else:
            newpath = pygame.transform.rotate(newpathh, 90)
        extray = 1
    elif spdx > 0:
        newpath = pygame.transform.rotate(newpathh, -math.atan(spdy / spdx) * 180 / math.pi)
    else:
        newpath = pygame.transform.rotate(newpathh, 180 - math.atan(spdy / spdx) * 180 / math.pi)

    if spdx>0 and spdy>0:
        extray = math.sin(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
        extrax = math.cos(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
    elif spdx>0 and spdy<0:
        extray = math.cos(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
        extrax = math.sin(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
    elif spdx < 0 and spdy < 0:
        extray = math.sin(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
        extrax = math.cos(math.radians(90 - math.atan(spdy / spdx) * 180 / math.pi)) * 70
    else:
        extray = math.cos(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
        extrax = math.sin(math.radians(- math.atan(spdy / spdx) * 180 / math.pi)) * 70
    if xS < 0:
        ximg = blntrac[len(blntrac) - 2]
    else:
        ximg = blntrac[len(blntrac) - 4]
    if yS < 0:
        yimg = blntrac[len(blntrac) - 1]
    else:
        yimg = blntrac[len(blntrac) - 3]
    images.append(Image(newpath , ximg- extrax, yimg - extray))

    for b in range(len(blntrac)//2):
        images.append(Image(stopper, blntrac[b*2-2]-70, blntrac[b*2-1]-70))


mapspecials=[mapspecial1,mapspecial2]
blntracks=[blntrac1,blntrac2]
mapsel=1
option=loadify("settingspannel")
while chosen==0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                connection.Send({"action": "mapchoose", "what": [mapsel]})
            if event.mod & pygame.KMOD_ALT:
                if event.key == pygame.K_F4:
                    chosen=1/0
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            XX = pygame.mouse.get_pos()
            if XX[0] > W//2:
                mapsel=min(mapsel+1,len(maps))
            else:
                mapsel = max(mapsel -1, 1)
    screen.blit(maps[mapsel-1], (0, 0))
    screen.blit(option, (w, 0))
    pygame.display.update()
    connection.Pump()
    nwl.Pump()
yoggstoth=Bloon(50, 150, 1, 1, 1, 0, 1, 1, 0)
yoggstoth.lists.append(bloons)
bloons.append(yoggstoth)
while running:
    XX = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if XX[0] > w + 40:
                if XX[1] < h - 200:
                    clickpos = XX[1] - scroll
                    if 118 * len(bloonprices) + 13 > clickpos > 12:
                        if int((clickpos - 13) / 118) < locked:
                            if bloonprices[int((clickpos - 13) / 118)][growmaybe][0] * bloonumba <= money:
                                growmaybe = 0
                                if XX[0] > w + 140:
                                    if int((clickpos - 13) / 118) < 11 and not int((clickpos - 13) / 118) ==9:
                                        growmaybe = 1
                                connection.Send({"action": "send", "what": [bloonumba, int((clickpos - 13) / 118),
                                                                            growmaybe * random.randint(150, 250)]})
                                money -= bloonprices[int((clickpos - 13) / 118)][growmaybe][0] * bloonumba
                                income += bloonprices[int((clickpos - 13) / 118)][growmaybe][1] * bloonumba
                elif XX[0] > w + 140:
                    if XX[1] < h - 100:
                        bloonumba += 1
                    elif bloonumba > 1:
                        bloonumba -= 1
            else:
                pliesY = 0
                for e in monks:
                    if distanceB(XX[0] - 60, XX[1] - 80, e.XX, e.YY, 100):
                        pliesY = 1
                if pliesY == 0:
                    if select == 0:
                        if money > 24:
                            money -= 25
                            drtmonks.append(drtmonkey(XX[0] - 60, XX[1] - 80, loadify('drtmonk')
                                                      , 0, 0, 10 + random.randint(-9, 10), 1  # 10+random.randint(-9,10)
                                                      , 200 + random.randint(-120, 120), loadify('drtn'), -10, [0, 0],
                                                      [0, 0]))
                    elif select == 1:
                        if money > 74:
                            money -= 75
                            enginers.append(engin(XX[0] - 60, XX[1] - 80, enginer
                                                  , 0, 0, 15 + random.randint(-10, 15), 1
                                                  , 1000 + random.randint(-680, 600)
                                                  , loadify('turret'), 200 + random.randint(-120, 120)
                                                  , loadify('nail'), 1000, [0, 0], [0, 0]))
                    elif select == 2:
                        if money > 99:
                            money -= 100
                            factories.append(factory(XX[0] - 60, XX[1] - 80, loadify('spikefac')
                                                     , 0, 0, 5, 200 + random.randint(-120, 120)
                                                     , loadify('spikes'), 2000 + random.randint(-900, 900)
                                                     , [0, 0]))
                    elif select == 3:
                        if money > 249:
                            money -= 250
                            gunners.append(gunner(XX[0] - 60, XX[1] - 80, loadify('guner')
                                                  , 0, 0, 6 + random.randint(-4, 4), 20 + random.randint(-12, 12)
                                                  , loadify('drtn'), 1, [0, 0], [0, 0]))
                    elif select == 4:
                        if money > 49:
                            money -= 50
                            druids.append(Druid(XX[0] - 60, XX[1] - 80, loadify('druid'), 0, 0,
                                                (40 + random.randint(-30, 0)) // 10, 550 + random.randint(-350, 350),
                                                [2, 1]))
                    elif select == 5:
                        if money > 14:
                            money -= 15
                            leafs.append(leafblower(XX[0], XX[1], loadify('leafblower')
                                                      , 0, 0, 10 + random.randint(-9, 10), 1  # 10+random.randint(-9,10)
                                                      , 200 + random.randint(-120, 120), loadify('drtn'), -10, [0, 0],
                                                      [0, 0],random.randint(50, 250)/1000,random.randint(110, 500) ) )

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            XX = pygame.mouse.get_pos()
            if distanceB(XX[0], XX[1], 410, 403, 50):
                xplosions.append(explode(380, 400, gold, 400))

            for e in monks:
                if distanceB(XX[0] - 60, XX[1] - 80, e.XX, e.YY, 50):
                    lvlup.append(e)
                    upgrade()
                    break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            scroll -= min(scroll + panelsize - h, 25)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            scroll += min(-scroll, 25)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_SPACE:
                for e in drts2:
                    if e.CR > 1:
                        if e.LS > ti:
                            e.LS = ti + 1
            if event.key == pygame.K_s:
                lo += 1
            if event.key == pygame.K_d:
                if lo > 2:
                    lo -= 1
            if event.key == pygame.K_g:
                for b in factories:
                    if b.f > 1:
                        if b.G < ti:
                            b.G = ti + 10000
                            XX = pygame.mouse.get_pos()
                            xS = (XX[0]) - (b.X + 10)
                            yS = (XX[1]) - (b.Y + 60)
                            if xS == 0:
                                spdx = 5
                                spdy = 0
                            else:
                                spdx = 5 / math.sqrt(yS ** 2 / xS ** 2 + 1)
                                if xS < 0:
                                    spdx *= -1
                                spdy = spdx * yS / xS

                            drts.append(
                                mine(b.X + 10, b.Y + 60, spdx, spdy, 150 + rn, 0, 0, [1000, 10, 0], XX, [0, 0], 3))
                            break

            if event.key == pygame.K_LEFT:
                if select > 0:
                    select -= 1
                else:
                    select = len(monksel) - 1
            if event.key == pygame.K_RIGHT:
                select += 1
                if len(monksel) - 1 < select:
                    select = 0
            if event.mod & pygame.KMOD_RSHIFT:
                if event.key == pygame.K_q:
                    money += 1000
                elif event.key == pygame.K_BACKSLASH:
                    CheaterPowers -= 1
                    CheaterPowers *= -1
        if event.type == pygame.QUIT:
            pygame.quit()
    connection.Pump()
    nwl.Pump()
    # if ti%1 == 0:
    for b in animations:
        if b.faze < int(b.t / b.T * len(b.ii)):
            b.faze = int(b.t / b.T * len(b.ii))
            b.i = b.ii[b.faze - 1]

    for e in xplosions:
        e.t += 4
        if e.t > e.T:
            xplosions.remove(e)
            if e in animations:
                animations.remove(e)
            e.kill()
            del e
        else:
            e.I = pygame.transform.smoothscale(e.i, (int((e.t * 3 + e.Start) * e.S), int((e.t * 3 + e.Start) * e.S)))
            e.s = pygame.Surface.get_size(e.I)

    if CheaterPowers == 1:
        for e in bloons:
            e.hploss(100)


    for z in range(204):
        for b in sqares[z]:
            for d in sqares2[z]:
                if d in drts:
                    if b not in murder:
                        if distanceB(b.X, b.Y - 10, d.X + 5, d.Y + 5, 20 + b.siz + d.siz):
                            d.special(b)
                            if d.dmg > b.armr:
                                b.hploss(d.dmg - b.armr)
                            d.H -= 1
                            if d.H < 1:
                                if d.P[0] > 0:
                                    d.xplod()
                                d.kill()
                                drts.remove(d)
                                del d
                                rel = 0
                elif d in drts2:
                    if b not in murder:
                        if distanceB(b.X, b.Y + b.R, d.X, d.Y, 25 + b.siz):
                            d.H -= 1
                            if b.armr < d.dmg:
                                b.hploss(d.dmg - b.armr)
                            if d.H < 1:
                                if d.P[0] > 0:
                                    xplosions.append(explode(d.x, d.y, d.P[2], d.P[0]))
                                    for c in bloons:
                                        if c.armr < d.P[1]:
                                            if distanceB(c.X, c.Y, d.X + 5, d.Y + 50, 100+d.P[0] + c.siz):
                                                c.hploss(d.P[1] - c.armr)
                                if d in blns:
                                    blns.remove(d)
                                for i in sqaresa:
                                    if d in i:
                                        i.remove(d)
                                drts2.remove(d)
                                d.kill()
                                del d
    moida()
    for e in factories:
        if (ti - e.C) > e.c:
            if not len(e.spikeX) < 4:
                e.C = ti
                elo = random.randint(0, len(e.spikeX) - 2)
                cl = random.uniform(0, 1)
                spikX = (1 - cl) * e.spikeX[elo] + e.spikeX[elo + 1] * cl
                spikY = (1 - cl) * e.spikeY[elo] + e.spikeY[elo + 1] * cl
                drtnew = Drt2(int(spikX), int(spikY), e.ID, e.H, e.LS + ti, e.f, e.F, e.tracpos, e.P, e.Dmg)

                for d in range(int(1 + (
                        min((int((drtnew.X + drtnew.ss[0]) // sqaresize), maxsqare)) - int(drtnew.X // sqaresize)))):
                    for i in range(
                            int(1 + (min(int(drtnew.Y + drtnew.ss[1] // sqaresize), 11) - int(drtnew.Y // sqaresize)))):
                        sqaresa[int((drtnew.X + d * sqaresize) // sqaresize + (
                                drtnew.Y + i * sqaresize) // sqaresize * maxsqare) - 1].append(drtnew)
                drts2.append(drtnew)

                # sqaresa[int((drtnew.X + drtnew.ss[0]) // sqaresize + (drtnew.Y + drtnew.ss[1]) // sqaresize * maxsqare)].append(drtnew)
                # if drtnew not in sqaresa[int(drtnew.X // sqaresize + drtnew.Y // sqaresize * maxsqare)]:
                #     sqaresa[int(drtnew.X // sqaresize + drtnew.Y // sqaresize * maxsqare)].append(drtnew)
                # if drtnew not in sqaresa[int((drtnew.X + drtnew.ss[0]) // sqaresize + drtnew.Y // sqaresize * maxsqare)]:
                #     sqaresa[int((drtnew.X + drtnew.ss[0]) // sqaresize + drtnew.Y // sqaresize * maxsqare)].append(drtnew)
                # if drtnew not in sqaresa[int(drtnew.X // sqaresize + (drtnew.Y + drtnew.ss[1]) // sqaresize * maxsqare)]:
                #     sqaresa[int(drtnew.X // sqaresize + (drtnew.Y + drtnew.ss[1]) // sqaresize * maxsqare)].append(drtnew)
                # drts2.append(drtnew)
    for e in druidart:
        if e.D[0] + e.D[1] < ti:
            drts.append(e)
            druidart.remove(e)
    for b in druids:
        if (ti - b.C) > b.c:
            for e in bloons:
                if distanceB(e.X, e.Y, b.X + 67, b.Y + 60, 250 + e.siz):
                    pliesX = 15
                    pliesY = 20
                    b.C = ti
                    xS = (e.X) - (b.X + pliesX)
                    yS = (e.Y) - (b.Y + pliesY)
                    if xS == 0:
                        spdx = b.DS
                        spdy = 0
                    else:
                        spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                        if xS < 0:
                            spdx *= -1
                        spdy = spdx * yS / xS
                    druiddart = druidball(b.X + pliesX, b.Y + pliesY, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE, b.dmg,
                                          b.bounce, [e for e in b.pierce])
                    druiddart.D = [ti, b.D]
                    drts.append(druiddart)
                    break


    for b in drtmonks:
        if (ti - b.C) > b.c:
            rel = 0
            for e in bloons:
                if distanceB(e.X, e.Y, b.X + 67, b.Y + 60, b.rang + e.siz):
                    if b.LS == -10:
                        pliesX = 10
                        pliesY = 70
                    else:
                        pliesX = 15
                        pliesY = 20
                        if e.X > b.X:
                            if b.rot > 0:
                                b.I = TL[b.rot]
                                b.rot *= -1

                        elif b.rot < 0:
                            b.rot *= -1
                            b.I = TL[b.rot - 1]
                    b.C = ti
                    xS = (e.X) - (b.X + pliesX)
                    yS = (e.Y) - (b.Y + pliesY)
                    if xS == 0:
                        spdx = b.DS
                        spdy = 0
                    else:
                        spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                        if xS < 0:
                            spdx *= -1
                        spdy = spdx * yS / xS

                    drts.append(Drt(b.X + pliesX, b.Y + pliesY, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE, b.dmg, 0,
                                    [e for e in b.SPX]))
                    if b.LS > 0:
                        if b.F > 0:
                            drts.append(
                                Drt(b.X + pliesX - spdx, b.Y + pliesY - spdy, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE,
                                    b.dmg, 0, [e for e in b.SPX]))
                    rel += b.Q
                    if rel == 1:
                        break
    for b in gunners:
        if (ti - b.C) > b.c:
            XX = pygame.mouse.get_pos()
            pliesX = -12
            pliesY = 0
            b.C = ti
            xS = (XX[0]) - (b.X + pliesX)
            yS = (XX[1]) - (b.Y + pliesY)
            if xS == 0:
                spdx = b.DS
                spdy = 0
            else:
                spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                if xS < 0:
                    spdx *= -1
                spdy = spdx * yS / xS

            if spdx == 0:
                if spdy < 0:
                    b.IB = pygame.transform.rotate(b.I, -90)
                else:
                    b.IB = pygame.transform.rotate(b.I, 90)
            elif spdx > 0:
                b.IB = pygame.transform.rotate(b.I, -math.atan(spdy / spdx) * 180 / math.pi)
            else:
                b.IB = pygame.transform.rotate(b.I, 180 - math.atan(spdy / spdx) * 180 / math.pi)
            ss = pygame.Surface.get_size(b.IB)
            b.EX = int(ss[0] / 2)
            b.EY = int(ss[1] / 2)

            if b.F > 0:
                nspd = b.DS / 10
                nespd = spdx / -nspd
                newspd = spdy / nspd
                pliesX = 5
                pliesY = 5
                pliesX *= newspd
                pliesY *= nespd
                drts.append(Drt(b.X + pliesX, b.Y + pliesY, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE, b.dmg))
                if b.F > 1:
                    drts.append(Drt(b.X - pliesX, b.Y - pliesY, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE, b.dmg))
                    if b.F > 2:
                        pliesX /= 2
                        pliesY /= 2
                        newspd = random.randint(1, 10)
                        if newspd > 9:
                            newspd = 150
                            nespd = bomb
                        else:
                            newspd = 0
                            nespd = b.ID
                        drts.append(Drt(b.X + pliesX, b.Y + pliesY, spdx, spdy, nespd, b.H, 0, 0,
                                        [b.P[0] + newspd, b.P[1] + 3, 1], b.SPE, b.dmg))
                        drts.append(Drt(b.X - pliesX, b.Y - pliesY, spdx, spdy, nespd, b.H, 0, 0,
                                        [b.P[0] + newspd, b.P[1] + 1, 1], b.SPE, b.dmg))
                        drts.append(
                            Drt(b.X, b.Y, spdx, spdy, nespd, b.H, 0, 0, [b.P[0] + newspd, b.P[1] + 1, 1], b.SPE, b.dmg))

            drts.append(Drt(b.X, b.Y, spdx, spdy, b.ID, b.H, 0, 0, b.P, b.SPE, b.dmg))
    sqares = [[g for g in e] for e in sqaresb]
    sqares2 = [[g for g in e] for e in sqaresa]
    for b in enginers:
        if (ti - b.C) > b.c:
            b.C = ti
            drtmonks.append(drtmonkey(b.X + random.randint(-150, 200), b.Y + random.randint(-150, 200), b.MI, b.f, b.F
                                      , b.DS, b.H, b.MC, b.ID, b.LS * 2 + ti, b.P, b.SPE))
        elif b.f > 0:
            if random.randint(1, 2) == 2:
                pass
            elif (ti - b.C) == int(b.c / 2):
                for e in bloons:
                    xS = (e.X) - (b.X + 10)
                    yS = (e.Y) - (b.Y + 60)
                    if xS == 0:
                        spdx = b.DS
                        spdy = 0
                    else:
                        spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                        if xS < 0:
                            spdx *= -1
                        spdy = spdx * yS / xS

                    drts.append(Drt(b.X + 10, b.Y + 60, spdx, spdy, loadify('spanner'), 10, 0, 0, [0, 0], b.SPE))
                    break

    screen.blit(btdmap, (0, 0))
    for e in images:
        screen.blit(e.I, (e.x, e.y))
    for b in leafs:
        rel = 0
        for e in bloons:
            if e.ID>-10:
                if distanceB(e.X, e.Y, b.X + 67, b.Y + 60, b.rang + e.siz):
                    if b.LS == -10:
                        pliesX = 10
                        pliesY = 70
                    else:
                        pliesX = 15
                        pliesY = 20
                        if e.X > b.X:
                            if b.rot > 0:
                                b.I = TL[b.rot]
                                b.rot *= -1

                        elif b.rot < 0:
                            b.rot *= -1
                            b.I = TL[b.rot - 1]
                    xS = (e.X) - (b.X + pliesX)
                    yS = (e.Y) - (b.Y + pliesY)
                    if xS == 0:
                        spdx = b.DS
                        spdy = 0
                    else:
                        spdx = b.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                        if xS < 0:
                            spdx *= -1
                        spdy = spdx * yS / xS
                    e.X+=spdx*b.blow
                    e.Y+=spdy*b.blow
                    if not w>e.X>0:
                        e.X=max(min(e.X,w),0)
                        if b.power >= 1:
                            e.hploss(b.power)

                    if not h>e.Y>0:
                        e.Y=max(min(e.Y,h),0)
                        if b.power>=1:
                            e.hploss(b.power)
                    e.SY=0
                    rel += b.Q
                    if rel==b.Q:
                        if spdx == 0:
                            if spdy < 0:
                                b.I = pygame.transform.rotate(b.i, 0)
                            else:
                                b.I = pygame.transform.rotate(b.i, 180)
                        elif spdx > 0:
                            b.I = pygame.transform.rotate(b.i, -math.atan(spdy / spdx) * 180 / math.pi + 90)
                        else:
                            b.I = pygame.transform.rotate(b.i, 180 - math.atan(spdy / spdx) * 180 / math.pi + 90)
                        b.ss = pygame.Surface.get_size(b.I)
                    if rel == 1:
                        break
    blnM()

    drtM()
    drtmonk()
    engeneer()
    Factory()
    bloon()
    drt()
    hpshow(10, 10)
    screen.blit(loadify('select'), (40, 780))
    screen.blit(monksel[select], (50, 800))
    screen.blit(panelloon, (w, scroll))
    for b in range(len(bloonprices)):
        v = len(bloonprices) - b
        if int((121 * v) / 118) > locked:
            screen.blit(lock, (w, int((118 * (v - 1) + scroll + 13))))
        else:
            break
    screen.blit(bloonamount, (w, h - 200))
    bwee = finter.render(str(bloonumba), True, (0, 0, 0))
    screen.blit(bwee, (w + 60, h - 150))
    if XX[0] > w + 40:
        if XX[1] < h - 200:
            clickpos = XX[1] - scroll
            if 118 * len(bloonprices) + 13 > clickpos > 12:
                growmaybe = 0
                if XX[0] > w + 140:
                    if int((clickpos - 13) / 118) < 11 and not int((clickpos - 13) / 118) ==9:
                        growmaybe = 1
                screen.blit(board, (XX[0] - 300, XX[1]))
                bwee = flint.render(str(bloonprices[int((clickpos - 13) / 118)][growmaybe][0] * bloonumba), True,
                                    (0, 0, 0))
                screen.blit(bwee, (XX[0] - 198, XX[1] + 25))
                bwee = flint.render(str(bloonprices[int((clickpos - 13) / 118)][growmaybe][1] * bloonumba), True,
                                    (0, 0, 0))
                screen.blit(bwee, (XX[0] - 162, XX[1] + 62))
    pygame.display.update()
    for e in bloondelay:
        if e.X<ti:
            bloons.append(e)
            e.lists.append(bloons)
            bloondelay.remove(e)
            e.X=blntrac[0]
            e.x =blntrac[0]
        else:
            break
    ti += 1
    for e in drtmonks:
        if e.LS == ti:
            e.kill()
            drtmonks.remove(e)
            drtmunks.remove(e)
            del e

    for e in drts2:
        if e.LS == ti:
            if e.CR > 1:
                blns.append(e)
                e.n = blntrac
                e.SX = 0
                e.SY = 0
                e.S = 3
                e.ID = 99
            else:
                for b in sqaresa:
                    if e in b:
                        b.remove(e)
                drts2.remove(e)
                e.kill()
                del e

    for e in growbloon:
        if ti % (e.r * 3) == 0:
            e.grow()

    for e in mines:
        if distanceB(e.X, e.Y, e.LS[0], e.LS[1], 10):
            e.S = 0
            e.s = 0
            mines.remove(e)






