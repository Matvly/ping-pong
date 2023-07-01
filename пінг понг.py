from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height,):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.blit(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)        
ball = Player('tennis_ball.png', 200, 200, 4, 50, 50) 

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 LOSE', 1, (180, 0, 0))
lose2 = font.render('Player 1 LOSE', 1, (180, 0, 0))

speed_x = 3
speed_y = 3




