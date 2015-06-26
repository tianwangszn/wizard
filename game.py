#coding:utf-8
#!/usr/bin/env python

import pygame
import os
from pygame.locals import *
from sys import exit

def imageLoad(name):
    """ Function for loading an image. Makes sure the game is compatible across multiple OS'es, as it
    uses the os.path.join function to get he full filename. It then tries to load the image,
    and raises an exception if it can't, so the user will know specifically what's going if the image loading
    does not work. """
    
    fullname = os.path.join('data/image/', name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    
    return image, image.get_rect()



#background_image_filename = 'data/image/backgrounds.jpg'

pygame.init()

screen = pygame.display.set_mode((1280,720),0,32)
background, backgroundRect = imageLoad('backgrounds.jpg')
pygame.display.set_caption("Wizard!")
my_font = pygame.font.SysFont("arial",16)
my_font2 = pygame.font.SysFont("arial",14)
name_surface = my_font.render("Please choose the number of player :",True,(0,0,0))
player_name = my_font2.render("PC    NPC1    NPC2    NPC3    NPC4    NPC5",True,(0,0,0))
pockerback, pockerbackRect= imageLoad('back1.jpg')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    
    screen.blit(background,backgroundRect)
    screen.blit(name_surface,(10,600))
    screen.blit(player_name,(10,100))
    for i in range(5):
        screen.blit(pockerback,(500+20*i,650))
    pygame.display.update()
    
    
    
    
    
    
