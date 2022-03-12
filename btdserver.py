
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
        if len(players)<2:
            newplayer = player()
            players.append(newplayer)
            self.Send({"action": "gitplayer", "id": len(players)})
        else:
            self.Send({"action": "gitplayer", "id": 10})

    def Network_send(self, data):
        for channel in self.server.all_channels:
            if channel is not self:
                channel.Send({"action": "ugotbloonsmon", "takedis":data["what"]})

    def Network_mapchoose(self, data):
        global mapchosen
        if len(players)==2 and mapchosen==0:
            mapchosen=1
            print(12)
            for channel in self.server.all_channels:
                print(25)
                channel.Send({"action": "mapchosen", "info": data["what"]})
        else:
            print([len(players)==2, mapchosen])

    def Network_ready(self,data):
        global nextround
        nextround+=1
        if nextround==2:
            rnd(0)
class cw_server(Server):
    channelClass = player_channel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_channels=[]

    def Connected(self, channel, addr):
        if len(self.all_channels)==2:
            channel.Send({"action": "gitplayer", "id": 10})
        else:
            self.all_channels.append(channel)

    def join(self, channel):
        pass

    def leave(self, channel):
        pass

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
blnpower=[1,1.8,2.5,3.3,4,7,13,11,11,15,20,30,40]
def rnd(b):
    global rn,players,nextround,ch,blnpower,roundsize
    if b==0:
        roundsize=min(1500,rn*random.randint(4,120))
        nextround = 0
        rn+=1
    ch = 5
    regrow = random.choice([0, 1])
    if rn > 60:
        ch = random.randint(9, 13)
        if ch == 13:
            regrow = 0
        else:
            ch=5
    if regrow == 1:
        regrow =random.randint(150, 250)

    if ch == 5:
        if rn > 40:
            ch = random.randint(1, 12)
            if ch==12:
                regrow=0
        if rn > 30:
            ch = random.randint(1, 11)
        elif rn > 20:
            print(3)
            ch = random.randint(1, 9)
        elif rn > 15:
            print(2)
            ch = random.randint(1, 6)
        else:
            print(1)
            ch = random.randint(1, 3)
            #[howmany, which, regrow (random.randint(50,350) is standard)]
    for channel in srvr.all_channels:
        sendamount=min(int(rn**2/5 / int(ch*blnpower[ch-1] / 5 + 1+b)),50+b)
        channel.Send({"action": "ugotbloonsmon", "takedis": [sendamount, ch-1, regrow, roundsize/sendamount]})
    if random.randint(int(rn / 3), rn) > 10 + b * 2:
        rnd(b + 1)

#
# @app.route('/anynew', methods = ['POST'])
# def Anynew():
#     update = jsonpickle.decode(request.get_data())
#     for e in players:
#         if e.ID==update:
#             wheiz=e.updates
#             e.updates = []
#             return jsonpickle.encode(wheiz)
#
# @app.route('/start')
# def start():
#     global players
#     if len(players)<2:
#         newplayer = player()
#         players.append(newplayer)
#         return jsonpickle.encode(newplayer)
#     else:
#         print(players)
#         return jsonpickle.encode("There are already 2 players")
# @app.route('/sendbloon', methods = ['POST'])
# def sendbloons():
#     global players
#     update = jsonpickle.decode(request.get_data())
#     for e in players:
#         if not e.ID==update[0]:
#             e.updates.append([0,update[1]])
#     return jsonpickle.encode("ayay sir")
# @app.route('/sendready', methods = ['POST'])
# def sendstuff():
#     global nextround
#     nextround+=1
#     if nextround==2:
#         rnd(0)
#     return jsonpickle.encode("ayay sir")
#
# @app.route('/MyUpdates', methods = ['POST'])
# def giveupdate():
#     global players
#     update = jsonpickle.decode(request.get_data())
#     for e in players:
#         if e.ID==update:
#             dododoo=[e.ID]
#             return jsonpickle.encode(dododoo)
#     print('clientnotfounderror')
#     return jsonpickle.encode([])
#
# @app.route('/players', methods = ['GET'])
# def playerget():
#     global players
#     return jsonpickle.encode(players)
#
# @app.route('/mobbos')
# def mobboser():
#     global moobs
#     return jsonpickle.encode(moobs)

with open("ip.txt") as ip:
    srvr = cw_server(localaddr=(ip.read(), 5071))
while True:
    srvr.tick()
    time.sleep(0.001)