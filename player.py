import pygame 


class Player : 
    def __init__(self, ecran):
        self.ecran = ecran
        self.ecran_largeur = self.ecran.get_width()
        self.ecran_hauteur = self.ecran.get_height()
        self.pos = [400,400]
        self.vit = 10
        self.vivant = 1
        self.taille = 20
    def deplacement( self, dirx, diry):
        if dirx > 0:
            if self.pos[0] + dirx*self.vit + self.taille//2 < self.ecran_largeur:
                self.pos[0] += dirx*self.vit
            else :
                self.pos[0] = self.ecran_largeur - self.taille//2
                
        if dirx < 0:
            if self.pos[0] + dirx*self.vit + self.taille//2 > 0:
                self.pos[0] += dirx*self.vit
            else :
                self.pos[0] = 0 + self.taille//2

        if diry > 0:
            if self.pos[1] + diry*self.vit + self.taille//2 < self.ecran_hauteur:
                self.pos[1] += diry*self.vit
            else :
                self.pos[1] = self.ecran_hauteur - self.taille//2
                
        if diry < 0:
            if self.pos[1] + diry*self.vit + self.taille//2 > 0:
                self.pos[1] += diry*self.vit
            else :
                self.pos[1] = 0 + self.taille//2
        
        
    def draw(self):
       pygame.draw.circle(self.ecran, (250,0,0), self.pos, self.taille) 
       

        
        
        