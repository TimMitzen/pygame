import pygame

from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
#tkinter is a gui libarie

pygame.init() #starts pygame
vec = pygame.math.Vector2 # for two dimensional creates x and y
HEIGHT = 1000#height and width of the program
WIDTH = 1000
ACC= 0.3 #acceleration
FRIC = -0.10#friction
FPS = 60
FPS_CLOCK = pygame.time.Clock()#for frames per second
COUNT = 0

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))#area of game
pygame.display.set_caption("Game")#name of game


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect(center= (350, 350))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))


        #get rect will return a rectangle object of the same dimensions as the image so if the image is 500 by 200 it returns the same
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("Background.png")
        self.bgY = 0
        self.bgX = 0

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

background = Background()
ground = Ground()
#creating the background


#self.bgy and self.bgx are going for scrolling backgrounds
#render is to display the background
#blit drows the background with two tuples aka self.bgx ang self.bgy

while True:
    #will run when the close window button is clicked
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #for event that occur upon click the mouse(left)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        #Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            pass

    background.render()#order of rendering matters
    ground.render()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)






