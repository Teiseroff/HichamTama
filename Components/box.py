

import numpy as np


class Box() :

    def __init__(self) :
        self.x = None
        self.y = None
        self.isFree = True
        self.contains = None

    def setX(self,x) :
        self.x = x

    def setY(self,y) :
        self.x = y

    def setFree(self, bool) :
        self.isFree = bool

    def setContains(self,piece) :
        self.contains = piece

    def getContains(self) :
        return self.contains

    def getX(self) :
        return self.x

    def getY(self) :
        return self.y

    
