import pygame
import time
from flask import Flask, request
import jsonpickle
import random
import pygame
import math
countdown=-1
class tile(pygame.sprite.Sprite):
    def __init__(self, X, Y, I):
        self.X = X
        self.Y = Y
        self.I = I
        self.s = [100,100]
playersID=0
moobs=[]
moobID=0

def distanceC(eneX, eneY, bulX, bulY):
    distance = math.sqrt((math.pow(eneX - bulX, 2)) + (math.pow(eneY - bulY, 2)))
    return distance
class moob(object):
    def __init__(self):
        global moobID
        moobID+=1
        self.ID=moobID
        self.X=-20000 + 200 * random.randint(0, 200)
        self.Y=-20000 + 200 * random.randint(0, 200)
        self.difficulty=int((distanceC(self.X,self.Y,0,0))//500)
        self.difficulty=self.difficulty*self.difficulty/50
        if self.difficulty<0.5:
            self.difficulty=0.5
        self.enemies = min(10,max(int(self.difficulty*0.3),2))
class player(object):
    def __init__(self):
        global playersID
        self.updates=[]
        playersID+=1
        self.ID=playersID
        self.X=0
        self.XP = [0,10,1]
        self.Y=0
        self.dead=0
        self.spell = 0
        self.physical = 0
        self.H = [500, 500]
players=[]
shops=[]
shopID = 0
class shop(object):
    def __init__(self):
        global shopID
        shopID+=1
        self.ID=shopID
        self.X=-20000 + 200 * random.randint(1, 199)
        self.Y=-20000 + 200 * random.randint(1, 199)
        self.type=random.randint(0,2)
        if random.randint(0,10)<10:
            if self.type==2:
                self.type=0
for e in range(1000):
    shops.append(shop())

for e in range(500):
    moobs.append(moob())


class timer(object):
    def __init__(self,ID):
        self.T="hu ha"
        self.ID=ID

app = Flask(__name__)

f=1
updates=[]
rn=5
def rnd(b):
    global rn,players,nextround
    if b==0:
        nextround = 0
    regrow = random.choice([0, 1])
    if regrow == 1:
        regrow = random.randint(50, 350)
    spc = random.randint(1, 50)
    ch = 5
    if rn > 40:
        ch = random.randint(9, 13)
        if ch == 1:
            regrow = 0
        else:
            ch = 5
    if ch == 5:
        if rn > 20:
            ch = random.randint(1, 11)
            if rn > 25 and ch == 1:
                ch = 12
                regrow = 0
            elif ch == 7:
                spc += 10
        elif rn > 10:
            ch = random.randint(1, 6)
        else:
            ch = random.randint(1, 3)
            #[howmany, which, regrow (random.randint(50,350) is standard)]
    for e in players:
        e.updates.append([0,[int(rn / int(ch / 2 + 1)),ch,regrow,spc]])
    if random.randint(int(rn / 3), rn) > 10 + b * 2:
        rnd(b + 1, [])


@app.route('/anynew', methods = ['POST'])
def Anynew():
    update = jsonpickle.decode(request.get_data())
    for e in players:
        if e.ID==update:
            wheiz=e.updates
            e.updates = []
            return jsonpickle.encode(wheiz)

@app.route('/start')
def start():
    global players
    if len(players)<2:
        newplayer = player()
        players.append(newplayer)
        return jsonpickle.encode(newplayer)
    else:
        print(players)
        return jsonpickle.encode("There are already 2 players")
@app.route('/sendbloon', methods = ['POST'])
def sendbloons():
    global players
    update = jsonpickle.decode(request.get_data())
    for e in players:
        if not e.ID==update[0]:
            e.updates.append([0,update[1]])
    return jsonpickle.encode("ayay sir")
nextround=0
@app.route('/sendready', methods = ['POST'])
def sendstuff():
    global nextround
    nextround+=1
    if nextround==2:
        rnd(0)
    return jsonpickle.encode("ayay sir")

@app.route('/MyUpdates', methods = ['POST'])
def giveupdate():
    global players
    update = jsonpickle.decode(request.get_data())
    for e in players:
        if e.ID==update:
            dododoo=[e.ID]
            return jsonpickle.encode(dododoo)
    print('clientnotfounderror')
    return jsonpickle.encode([])

@app.route('/players', methods = ['GET'])
def playerget():
    global players
    return jsonpickle.encode(players)

@app.route('/mobbos')
def mobboser():
    global moobs
    return jsonpickle.encode(moobs)

app.run(host='0.0.0.0', port=5000, debug=False)