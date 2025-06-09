import random

import pygame
from Internal.Game import *

class Engineer(pygame.sprite.Sprite):
    def __init__(self, X, Y, I, f, F, DS, H, c, MI, MC, ID, LS, P, SPE,game):
        super(Engineer, self).__init__()
        self.game=game
        game.monks.append(self)
        self.SPE = SPE
        self.price = 69
        self.MID = 2
        self.locked = [10, 10]
        self.ID = ID
        self.MC = MC
        self.MI = MI
        self.LS = LS
        self.ID = ID
        self.H = H
        self.c = c
        self.DS = DS
        self.C = game.time
        self.I = I
        self.f = f
        self.F = F
        self.X = X
        self.Y = Y
        self.XX = X
        self.YY = Y
        self.P = P
    def updateDraw(s):
        s.screen.blit(s.I, (s.X, s.Y))
    def update(s,dt):
        if (dt - s.C) > s.c:
                s.C = dt
                s.game.addDrtmonk(drtmonkey(s.X + random.randint(-150, 200), s.Y + random.randint(-150, 200), s.MI, s.f, s.F
                                          , s.DS, s.H, s.MC, s.ID, s.LS * 2 + dt, s.P, s.SPE))
            elif s.f > 0:
            if random.randint(1, 2) == 2:
                pass
            elif (dt - s.C) == int(s.c / 2):
                for e in bloons:
                    xS = (e.X) - (s.X + 10)
                    yS = (e.Y) - (s.Y + 60)
                    if xS == 0:
                        spdx = s.DS
                        spdy = 0
                    else:
                        spdx = s.DS / math.sqrt(yS ** 2 / xS ** 2 + 1)
                        if xS < 0:
                            spdx *= -1
                        spdy = spdx * yS / xS

                    drts.append(Drt(s.X + 10, s.Y + 60, spdx, spdy, span, 10, 0, 0, [0, 0], s.SPE))
                    break

