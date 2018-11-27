import pygame as pg
from settings import *
import Vector
vec = Vector.Vec2d

class Ball(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load('Assets/ball2.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(100,80)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def ball_jump(self):
       # self.rect.y -= 1
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
       # self.rect.y += 1
        if hits:
            self.vel.y = -BALL_JUMP
    
    def side_collsion(self,direction):
       # if direction == 'l':
        pass

    def update(self):
        self.acc = vec(0,BALL_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -BALL_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = BALL_ACC
        if keys[pg.K_UP]:
            self.ball_jump()

        self.acc.x += self.vel.x*BALL_FRICTION

        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class Wall(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height))
        self.image.fill(BACKGROUND_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


class Spikes(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Assets/spike.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class Platform_base(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
