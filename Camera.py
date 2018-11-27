import pygame as pg
from settings import *

class Camera:
    def __init__(self,width,height):
        self.camera = pg.Rect(0,0,width,height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x +int(WIDTH/2)
        y = -target.rect.x + int(HEIGHT/2)
        y=min(0,y)
        x = min(0,x)
        x=max(-(self.width-WIDTH),x)
        y=max(-(self.height-HEIGHT),y)
        self.camera = pg.Rect(x,y,self.width,self.height)

