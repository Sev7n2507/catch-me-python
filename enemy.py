import pygame
from player import *
import math


from random import randrange
class Enemy : 
    def __init__(self, ecran, player):
        self.player = player
        self.ecran = ecran
        self.ecran_largeur = self.ecran.get_width()
        self.ecran_hauteur = self.ecran.get_height()
        self.taille = 20
        self.pos = [randrange(self.ecran_largeur - self.taille), randrange(self.ecran_hauteur - self.taille)]
        self.vit = 0.1
        self.vivant = 1
    def deplacement( self, dirx, diry):
            if dirx > 0:
                if self.pos[0] + dirx*self.vit + self.taille//2 < self.ecran_largeur:
                    self.pos[0] += dirx*self.vit
                #else :
                    #self.pos[0] = self.ecran_largeur - self.taille//2
                    
            if dirx < 0:
                if self.pos[0] + dirx*self.vit + self.taille//2 > 0:
                    self.pos[0] += dirx*self.vit
                #else :
                    #self.pos[0] = 0 + self.taille//2

            if diry > 0:
                if self.pos[1] + diry*self.vit + self.taille//2 < self.ecran_hauteur:
                    self.pos[1] += diry*self.vit
                #else :
                    #self.pos[1] = self.ecran_hauteur - self.taille//2
                    
            if diry < 0:
                if self.pos[1] + diry*self.vit + self.taille//2 > 0:
                    self.pos[1] += diry*self.vit
                #else :
                    #self.pos[1] = 0 + self.taille//2
    def draw(self):
        pygame.draw.circle(self.ecran, (250, 250,0), self.pos, self.taille) 
           
    def follow(self):
        ep = (self.player.pos[0] - self.pos[0], self.player.pos[1] - self.pos[1])
        d = math.sqrt(math.pow(ep[0], 2) + math.pow(ep[1], 2))
        ep = (ep[0] / d, ep[1] / d)
        self.deplacement(ep[0], ep[1])
        if d < self.taille :
            return True
        return False
        