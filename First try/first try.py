import pygame
import random
from sys import exit
pygame.init()
screen= pygame.display.set_mode((600,400))
icon = pygame.image.load('fart.png')
pygame.display.set_caption('fart')
pygame.display.set_icon(icon)
Clock = pygame.time.Clock()
test_font=pygame.font.Font('Pixeltype.ttf',50)
background_surface = pygame.image.load('background.png').convert()
ground_surface = pygame.image.load('ground.jpg').convert()
score_surface = test_font.render("Score: "+str(0), None, "black")
score_rect = score_surface.get_rect(midbottom=(300,70))
fart_monster_surface= pygame.image.load('fart monster4.png').convert_alpha()
fart_monster_rect = fart_monster_surface.get_rect(topleft=(500,250))
player_surface=pygame.image.load('kakarino2.png').convert_alpha()
player_rect = player_surface.get_rect(topleft=(0,240))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    x1 = random.randrange(4,5)
    x2 = random.randrange(0,4)
    fart_monster_rect.x -= x1
    fart_monster_rect.x += x2
    player_rect.x += 1
    screen.blit(background_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(score_surface,score_rect)
    if fart_monster_rect.left < -100:
        fart_monster_rect.left = 600
    screen.blit(fart_monster_surface,fart_monster_rect )
    screen.blit(player_surface,player_rect)
    pygame.display.update()
    Clock.tick(60)
