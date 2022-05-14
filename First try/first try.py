import pygame
import random
from sys import exit
def time_score():
    time = pygame.time.get_ticks()//1000
    return time
##def points_score():
    
pygame.init()
screen= pygame.display.set_mode((600,400))
icon = pygame.image.load('fart.png')
pygame.display.set_caption('fart')
pygame.display.set_icon(icon)
Clock = pygame.time.Clock()
game_active = True
#fonts
score_font=pygame.font.Font('Pixeltype.ttf',35)
gameover_font=pygame.font.Font('Pixeltype.ttf',50)
#background
background_surface = pygame.image.load('background.png').convert()
#ground
ground_surface = pygame.image.load('ground.jpg').convert()
#score

#gameover
gameover_surface = gameover_font.render('Game Over', None, "red")
gameover_rect = gameover_surface.get_rect(midbottom=(300,70))
#fart_monster
fart_monster_surface= pygame.image.load('fart monster2.png').convert_alpha()
fart_monster_rect = fart_monster_surface.get_rect(topleft=(500,260))
#player
player_surface=pygame.image.load('kakarino2.png').convert_alpha()
player_rect = player_surface.get_rect(topleft=(0,310))
player_gravity=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and player_rect.bottom == 310 :  
                   player_gravity=-11
            
        else:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_active=True
                fart_monster_rect.x=500
                player_rect.x=0
    if game_active:
##        print(fart_monster_rect.top)
        #backgorund   
        screen.blit(background_surface,(0,0))
        
        #ground
        screen.blit(ground_surface,(0,300))
        
        #score
        score_surface = score_font.render("Score: "+str(time_score()), None, "black")
        score_rect = score_surface.get_rect(topleft=(3,0))
        screen.blit(score_surface,score_rect)
        #monster
        x1 = random.randrange(5,6)
        x2 = random.randrange(0,5)
        fart_monster_rect.x -= x1
        fart_monster_rect.x += x2
        if fart_monster_rect.left < -100:
            fart_monster_rect.left = 500
        screen.blit(fart_monster_surface,fart_monster_rect )
        #pygame.draw.rect(screen,'red',fart_monster_rect,1)

        #player
        player_gravity+=0.4
        player_rect.y+=player_gravity
        if player_rect.bottom >= 310:
            player_rect.bottom=310
        screen.blit(player_surface,player_rect)
        if event.type == pygame.KEYDOWN:
           print(player_rect.bottom)
           if event.key == pygame.K_RIGHT :
                    if player_rect.bottom < 310 :
                       player_rect.x += 4
                    else :
                        player_rect.x += 3
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :  
                   if player_rect.bottom < 310 :
                       player_rect.x -= 4
                   else:
                       player_rect.x -= 3
        #pygame.draw.rect(screen,'red',player_rect,1)
        
        #collision
        if fart_monster_rect.colliderect(player_rect):
            screen.blit(gameover_surface,gameover_rect)
            game_active=False
        else:
            pass

    #game
    pygame.display.update()
    Clock.tick(60)
