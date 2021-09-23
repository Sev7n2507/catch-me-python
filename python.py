from player import *
from enemy import *
import pygame 

module_charge = pygame.init()
print (module_charge)


#ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
ecran = pygame.display.set_mode((800,800))

pygame.display.set_caption("Catch me 3000")

background = pygame.image.load('./catch-me-python/assets/background.jpg')
image = pygame.image.load("./catch-me-python/assets/catch-me.png")
pygame.display.set_icon(image)
print(image)

loop = True
p = Player(ecran)
e = Enemy(ecran,p)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 54)


while loop:
    
    
    
    ecran.blit(background, (0,0))
    e.draw()
    p.draw()    
    
    
    for event in pygame.event.get():
        #event input clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
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
            
    pygame.display.flip()        
    
    if e.follow() :
        
  
       
            
        #gameover = font.render("Press R to Respawn", False, (255, 255, 255))
        #rect = gameover.get_rect()
        #rect.center = ecran.get_rect().center
        #ecran.blit(gameover, rect)
        

        ecran.blit(background, (0,0))
        e.draw()
        p.draw() 
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
        
        #restart = input('do you want to restart Y/N?')
        #if restart == 'N':
        #    break
        #elif restart == 'Y':
        
        #    continue
     
        
    
    
    
    
    
       
pygame.quit()


