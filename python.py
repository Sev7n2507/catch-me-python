from player import *
from enemy import *
import pygame 
from random import *

module_charge = pygame.init()
print (module_charge)


#ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
ecran = pygame.display.set_mode((800,800))

pygame.display.set_caption("Catch me 3000")

background = pygame.image.load('./catch-me-python/assets/background.jpg')
image = pygame.image.load("./catch-me-python/assets/catch-me.png")

pygame.display.set_icon(image)
print(image)

pygame.key.set_repeat(1, 10)
loop = True
font = pygame.font.SysFont(None, 54)
game =True

while game:
    if loop:
        p = Player(ecran)
        enemies = [Enemy(ecran,p), Enemy(ecran,p), Enemy(ecran,p),Enemy(ecran,p),Enemy(ecran,p),Enemy(ecran,p),Enemy(ecran,p)]
        clock = pygame.time.Clock()

    while loop:
        
        
        
        ecran.blit(background, (0,0))
        for e in enemies :
            if e.follow() :
                loop = False
            e.draw()
        p.draw()  
        
      
        
        
        for event in pygame.event.get():
            #event input clavier
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                    game = False
                if event.key == pygame.K_q :
                    p.deplacement(-1, 0)
                if event.key == pygame.K_d :
                    p.deplacement(1, 0)
                if event.key == pygame.K_z :
                        p.deplacement(0, -1)
                if event.key == pygame.K_s :
                    p.deplacement(0, 1)
            if event.type == pygame.QUIT:
                loop = False
                game = False
                
        pygame.display.flip()        
        
        
    gameover = font.render("Press R to Respawn", False, (255, 255, 255))
    rect = gameover.get_rect()
    rect.center = ecran.get_rect().center
    ecran.blit(gameover, rect)
    pygame.display.flip()
    
    for event in pygame.event.get():
            #event input clavier
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    
                    loop = True       

           
            
        
            
    
    
    
    
    
       
pygame.quit()


