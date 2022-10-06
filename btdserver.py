
import time
import random
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
import pygame
import math
countdown=-1
nextround=0
mapchosen=0
class player_channel(Channel):
    def __init__(self, conn=None, addr=(), server=None, map=None):
        super().__init__(conn=conn, addr=addr, server=server, map=map)
        self.server=server

    def conn(self):
        if self.server is not None:
            self.server.join(self)

    def dis(self):
        if self.server is not None:
            self.server.leave(self)

    def Network(self, data):
        print(data)

    def Network_join(self, data):
        self.conn()

    def Network_start(self,data):
        global players
        if mapchosen==0:
            newplayer = player()
            players.append(newplayer)
            self.Send({"action": "gitplayer", "id": len(players)})
        else:
            self.Send({"action": "gitplayer", "id": 100000})

    def Network_send(self, data):
        for channel in self.server.all_channels:
            if channel is not self:
                channel.Send({"action": "ugotbloonsmon", "takedis":data["what"]})

    def Network_mapchoose(self, data):
        global mapchosen
        if mapchosen==0:
            mapchosen=1
            for channel in self.server.all_channels:
                channel.Send({"action": "mapchosen", "info": data["what"]})

    def Network_dead(self, data):
        global players
        for e in players:
            print(e.ID,data["what"])
            if e.ID==data["what"]:
                players.remove(e)
                print(1)
        if nextround==len(players):
            rnd(0)
    def Network_ready(self,data):
        global nextround
        nextround+=1
        if nextround==len(players):
            rnd(0)
class cw_server(Server):
    channelClass = player_channel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_channels=[]

    def Connected(self, channel, addr):
        self.all_channels.append(channel)
    def tick(self, dt=0):
        self.Pump()



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


class timer(object):
    def __init__(self,ID):
        self.T="hu ha"
        self.ID=ID

f=1
updates=[]
rn=5
roundsize=0
blnpower=[1,1.8,2.5,3.3,4,7,13,11,11,15,17,17,30,40,15,30,60]
def rnd(b):
    global rn,players,nextround,ch,blnpower,roundsize
    if b==0:
        roundsize=min(600,rn*random.randint(4,120))
        nextround = 0
        rn+=1
    ch = 5
    regrow = random.choice([0, 1])
    if rn > 55:
        ch = random.randint(10, 16)
        if ch > 12:
            if ch>14:
                ch+=1
            regrow = 0
        else:
            ch=5

    elif rn > 50:
        ch = random.randint(10, 15)
        if ch > 12:
            if ch==15:
                ch+=1
            regrow = 0
        else:
            ch=5

    elif rn > 40:
        ch = random.randint(10, 14)
        if ch > 12:
            if ch==14:
                ch+=2
            regrow = 0
        else:
            ch=5

    if regrow == 1:
        regrow =random.randint(150, 250)

    if ch == 5:
        if rn > 30:
            ch = random.randint(9, 14)
            if ch>12:
                regrow=0
                if ch==14:
                    ch+=2
        elif rn > 25:
            ch = random.randint(2, 11)
        elif rn > 19:
            ch = random.randint(1, 9)
        elif rn > 14:
            ch = random.randint(1, 6)
        else:
            ch = random.randint(1, 3)
            #[howmany, which, regrow (random.randint(50,350) is standard)]
    for channel in srvr.all_channels:
        sendamount=min(int(rn**2/5 / int(ch*blnpower[ch-1] / 5 + 1+b)),50)
        channel.Send({"action": "ugotbloonsmon", "takedis": [sendamount, ch-1, regrow, roundsize/sendamount]})
    if random.randint(int(rn / 3), rn) > 10 + b * 2:
        rnd(b + 1)



with open("ip.txt") as ip:
    srvr = cw_server(localaddr=(ip.read(), 5071))
while True:
    srvr.tick()
    time.sleep(0.001)