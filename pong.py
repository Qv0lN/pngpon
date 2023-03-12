from pygame import *
from random import randint
font.init()

window = display.set_mode((700, 500))

display.set_caption('pong')

background = transform.scale(image.load('fon.png'),(700,500))

game = True

f = font.Font(None, 40)

txt1 = f.render('PONG',True,(255,255,255))

clock = time.Clock()
FPS = 60

class game_sprite(sprite.Sprite):
    def __init__(self, picture, speed , x, y,w,h):
	     super().__init__()
	     self.image = transform.scale(image.load(picture),(w,h))
	     self.speed = speed
	     self.rect = self.image.get_rect()
	     self.rect.x = x
	     self.rect.y = y 
    def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))
class Player(game_sprite):
     def move_me(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_w] and self.rect.y > 0:
               self.rect.y-=self.speed
          if keys_pressed[K_s] and self.rect.y < 410:
               self.rect.y+=self.speed
     def move_me_2(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_o] and self.rect.y > 0:
               self.rect.y-=self.speed
          if keys_pressed[K_l] and self.rect.y < 410:
               self.rect.y+=self.speed

class ball(game_sprite):
    pass

Rocket_1 = Player('r_1.png',5,20,250,30,90)

Rocket_2 = Player('r_2.png',5,650,250,30,90)

Ball = ball('ball.png',5,340,240,30,30)

while game:
    for e in event.get():
          if e.type == QUIT:
               game = False
    window.blit(background,(0,0))
    Rocket_1.reset()
    Rocket_2.reset()
    Ball.reset()


    Rocket_1.move_me()
    Rocket_2.move_me_2()

    txt1 = f.render('PONG',True,(255,255,255))
    window.blit(txt1,(310,0))


    clock.tick(FPS)

    display.update()