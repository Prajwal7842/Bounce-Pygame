import pygame as pg
import random
from settings import *
from sprites import *
from os import path
import math
from Camera import *
from buttons import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.display_screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.pause = False
	self.flag = 0

    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.spikes = pg.sprite.Group()
        self.bases = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ball = Ball(self)
        self.all_sprites.add(self.ball)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.platforms.add(p)
            self.all_sprites.add(p)
        for wall in WALL_LIST:
            w = Wall(*wall)
            self.walls.add(w)
            self.all_sprites.add(w)
        for spike in SPIKES_LIST:
            s = Spikes(*spike)
            self.spikes.add(s)
            self.all_sprites.add(s)
        for base in BASE_LIST:
            b = Platform_base(*base)
            self.bases.add(b)
            self.all_sprites.add(b)

        self.camera = Camera(WIDTH*6,HEIGHT)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
	    if self.ball.pos.x>4460:
		self.flag=1
		self.show_go_screen()
    def update(self):
        self.all_sprites.update()
        if self.ball.vel.y > 0:
            hits = pg.sprite.spritecollide(self.ball, self.platforms, False)
            if hits:
                self.ball.pos.y = hits[0].rect.top
                self.ball.vel.y = 0
        #if self.ball.vel.y > 0:
        hits = pg.sprite.spritecollide(self.ball, self.bases, False)
        if hits:
                self.ball.pos.y = hits[0].rect.bottom+40
                self.ball.vel.y = 0
        if self.ball.vel.x > 0:
            hits = pg.sprite.spritecollide(self.ball, self.walls, False)
            if hits:
                self.ball.pos.x = hits[0].rect.left-15
                self.ball.vel.x = 0
        elif self.ball.vel.x < 0:
            hits = pg.sprite.spritecollide(self.ball, self.walls, False)
            if hits:
                self.ball.pos.x = hits[0].rect.right+15
                self.ball.vel.x = 0
        hits = pg.sprite.spritecollide(self.ball, self.spikes, False)
        if hits:
		self.show_go_screen()

        self.camera.update(self.ball)
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.pause = True
                    self.pause_game()
                    
                
    def draw(self):
        self.display_screen.fill(BACKGROUND_COLOR)
        for sprite in self.all_sprites:
            self.display_screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.update()
        
    
    def show_start_screen(self):
	waiting = True
        while waiting:
            self.display_screen.fill(BACKGROUND_COLOR)
            text = Button(self,TITLE,400,100,0,0,BACKGROUND_COLOR,BACKGROUND_COLOR,90)
            text.create_button()
            play = Button(self,"PLAY",170,200,120,50,GREEN,DARK_GREEN,20,self.new)
            play.create_button()
            instruction = Button(self,'INSTRUCTIONS',320,200,150,50,BRIGHT_ORANGE,ORANGE,20,self.show_instruction)
            instruction.create_button() 
            end = Button(self,"QUIT",500,200,120,50,RED,BRICKRED,20,self.quitgame)
            end.create_button()
            for event in pg.event.get():
                if event.type == pg.QUIT:
			pg.quit()
			quit()
            pg.display.update()
    def pause_game(self): 
        while self.pause:    
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quitgame()
            play = Button(self,"RESUME",170,200,120,50,GREEN,DARK_GREEN,20,self.unpause)
            play.create_button()
            end = Button(self,"QUIT",500,200,120,50,RED,BRICKRED,20,self.quitgame)
            end.create_button()
            menu = Button(self,"MENU",340,200,120,50,BRIGHT_ORANGE,ORANGE,20,self.show_start_screen)
            menu.create_button()
            pg.display.update()
            self.clock.tick(60)

    def unpause(self):
        self.pause=False

            
    def show_go_screen(self):
        waiting = True
        while waiting:
            self.display_screen.fill(BACKGROUND_COLOR)
	    if self.flag==1:
		win = Button(self,"YOU WIN",330,120,0,0,BACKGROUND_COLOR,BACKGROUND_COLOR,100)
		win.create_button()
	    else:
		win = Button(self,"YOU LOSE",330,120,0,0,BACKGROUND_COLOR,BACKGROUND_COLOR,100)
		win.create_button()
            restart = Button(self,"RESTART",170,250,120,50,GREEN,DARK_GREEN,20,self.new)
            restart.create_button()
            menu = Button(self,"MENU",320,250,150,50,BRIGHT_ORANGE,ORANGE,20,self.show_start_screen)
            menu.create_button() 
            end = Button(self,"QUIT",500,250,120,50,RED,BRICKRED,20,self.quitgame)
            end.create_button()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            pg.display.update()

    def quitgame(self):
        pg.quit()
        quit()

    def show_instruction(self):
	waiting = True
	while waiting:
		self.display_screen.fill(BACKGROUND_COLOR)
		back = Button(self,"BACK",30,30,120,50,GREEN,DARK_GREEN,20,self.show_start_screen)
		back.create_button()
		left = Button(self,"Press Left arrow key <- to move left",300,120,0,0,BACKGROUND_COLOR,BACKGROUND_COLOR,40)
		left.create_button()
		right = Button(self,"Press Right arrow key -> to move right",300,200,0,0,BACKGROUND_COLOR,BACKGROUND_COLOR,40)
		right.create_button()
		jump = Button(self,"Press Upper arrow to jump.",300,280,0,0,BACKGROUND_COLOR,BACKGROUND_COLOR,40)
		jump.create_button()
		for event in pg.event.get():
            		if event.type == pg.QUIT:
                   	 	pg.quit()
				quit()
            	pg.display.update()


if __name__ == '__main__':
	g = Game()
	g.show_start_screen()
	while g.running:
	    g.new()
	    g.show_go_screen()
	pg.quit()

