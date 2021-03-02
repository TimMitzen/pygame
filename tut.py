import pygame

from pygame.locals import *

import random
from tkinter import filedialog
from tkinter import *

# tkinter is a gui libary

pygame.init()  # starts pygame
vec = pygame.math.Vector2  # for two dimensional creates x and y
HEIGHT = 350  # height and width of the program
WIDTH = 700
ACC = 0.5 #acceleration
FRIC = -0.9  # friction
FPS = 60
FPS_CLOCK = pygame.time.Clock()  # for frames per second
COUNT = 0

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))  # area of game
pygame.display.set_caption("Game")  # name of game
attack_ani_R = [pygame.image.load('Player_Sprite_R.png'), pygame.image.load("Player_Attack_R.png"),
                pygame.image.load("Player_Attack2_R.png"), pygame.image.load("Player_Attack2_R.png"),
                pygame.image.load('Player_Attack3_R.png'), pygame.image.load("Player_Attack3_R.png"),
                pygame.image.load("Player_Attack4_R.png"), pygame.image.load("Player_Attack4_R.png"),
                pygame.image.load("Player_Attack5_R.png"), pygame.image.load("Player_Attack5_R.png"),
                pygame.image.load("Player_Sprite_R.png")]
attack_ani_L = [pygame.image.load('Player_Sprite_L.png'), pygame.image.load('Player_Attack_L.png'),
                pygame.image.load('Player_Attack2_L.png'), pygame.image.load('Player_Attack2_L.png'),
                pygame.image.load('Player_Attack3_L.png'),
                pygame.image.load('Player_Attack3_L.png'),
                pygame.image.load("Player_Attack4_L.png"),
                pygame.image.load("Player_Attack4_L.png"),
                pygame.image.load("Player_Attack5_L.png"),
                pygame.image.load("Player_Attack5_L.png"),
                pygame.image.load('Player_Sprite_L.png')]
run_animation_L = [pygame.image.load("Player_Sprite_L.png"), pygame.image.load('Player_Sprite2_L.png'),
                   pygame.image.load("Player_Sprite3_L.png"),pygame.image.load('Player_Sprite4_L.png'),
                   pygame.image.load("Player_Sprite5_L.png"), pygame.image.load("Player_Sprite6_L.png"),
                   pygame.image.load("Player_Sprite_L.png")]
run_animation_R = [pygame.image.load("Player_Sprite_R.png"), pygame.image.load('Player_Sprite2_R.png'),
                   pygame.image.load("Player_Sprite3_R.png"), pygame.image.load("Player_Sprite4_R.png"),
                   pygame.image.load("Player_Sprite5_R.png"), pygame.image.load('Player_Sprite6_R.png'),
                   pygame.image.load("Player_Sprite_R.png")]


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("Background.png")
        self.bgY = 0
        self.bgX = 0

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgX))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect(center=(350, 350))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))

        # get rect will return a rectangle object of the same dimensions as the image so if the image is 500 by 200 it returns the same


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player_Sprite_R.png')  # for the picture of the char
        self.rect = self.image.get_rect()
        self.jumping = False  # so player doesnt fall off screen
        self.running = False
        self.move_frame = 0
        # position and direction of char
        self.vx = 0
        self.pos = vec((340, 249))
        self.vel = vec(0, 0)  # veocity of char
        self.acc = vec(0, 0)  # acceleration of player
        self.direction = 'RIGHT'
        self.attacking = False
        self.attacking_frame = 0

    def move(self):#moves the char
        # keeps a constant acceleration
        self.acc = vec(0, 0.5)
        if abs(self.vel.x) > 0.2:
            self.running = True
        else:
            self.running = False
        pressed_keys = pygame.key.get_pressed()  # for current key presses

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            # formula to calculate velocity
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # updates the new position

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos

    def gravity_check(self):
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def jump(self): # jump
        self.rect.x += 1
        # checks to see if player is on the ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)

        self.rect.x -= 1
        # if touching the ground and not jumping
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def correction(self):
        if self.attacking_frame ==1:
            self.pos.x -= 20
        if self.attacking_frame == 10:
            self.pos.x += 20

    def attack(self):#  attack
        if self.attacking_frame > 10:
            self.attacking_frame = 0
            self.attacking = False
        if self.direction == "RIGHT":
            self.image = attack_ani_R[self.attacking_frame]
        if self.direction == "LEFT":
            self.correction()
            self.image = attack_ani_L[self.attacking_frame]
        self.attacking_frame += 1

    def update(self):
        if self.move_frame > 6:
            self.move_frame = 0
            return
        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_animation_R[self.move_frame]
                self.direction = "RIGHT"
            else:

                self.image = run_animation_L[self.move_frame]
                self.direction = 'LEFT'
            self.move_frame += 1
        if abs(self.vel.x) < 0.3 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_animation_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_animation_L[self.move_frame]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))


background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
player = Player()
# creating the background

#


# self.bgy and self.bgx are going for scrolling backgrounds
# render is to display the background
# blit drows the background with two tuples aka self.bgx ang self.bgy

while True:#game loop
    # will run when the close window button is clicked
    player.gravity_check()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # for event that occur upon click the mouse(left)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True

    background.render()  # order of rendering matters
    ground.render()
    player.move()
    player.update()
    if player.attacking:
        player.attack()
    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
