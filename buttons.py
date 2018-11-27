import pygame as pg
from settings import *

class Button:
    def __init__(self,game,message,x,y,w,h,ac,ic,font_size,action=None):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.message=message
        self.active_color=ac
        self.inactive_color=ic
        self.action=action
        self.game=game
        self.font_size=font_size
    def create_button(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if (self.x+self.width>mouse[0]>self.x) and (self.y+self.height>mouse[1]>self.y):
            pg.draw.rect(self.game.display_screen,self.active_color,(self.x,self.y,self.width,self.height))
            if click[0]==1 and self.action!=None:
                self.action()
        else:
            pg.draw.rect(self.game.display_screen,self.inactive_color,(self.x,self.y,self.width,self.height))

        smallText = pg.font.SysFont('comicsansms',self.font_size)
        textSurf, textRect = self.text_objects(smallText)
        textRect.center = ((self.x+(self.width/2)),(self.y+(self.height/2)))
        self.game.display_screen.blit(textSurf, textRect)
    def text_objects(self,font):
        textSurface = font.render(self.message,True,BLACK)
        return textSurface, textSurface.get_rect()

