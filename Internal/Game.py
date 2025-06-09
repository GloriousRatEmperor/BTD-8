


class Game():
    def __init__(self,map,screen):
        self.enginers = []
        self.screen=screen
        self.map=map
        self.monks=[]
        self.time=0
    def addEngineer(self,engineer):
        self.enginers.add(engineer)
    def removeEngineer(self,engineer):
        self.enginers.remove(engineer)

    def update(self):
        for e in self.enginers:
            e.updateDraw()
        for b in self.enginers:
            b.update(self.time)

