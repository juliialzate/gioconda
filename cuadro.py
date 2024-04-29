import pygame
from main import * 

imagen1 = pygame.image.load("gioconda1.png")
imagen2 = pygame.image.load("gioconda2.png")
imagen3 = pygame.image.load("gioconda3.png")
imagen4 = pygame.image.load("gioconda4.png")
imagen5 = pygame.image.load("gioconda5.png")
imagen6 = pygame.image.load("gioconda6.png")
imagen7 = pygame.image.load("gioconda7.png")
imagen8 = pygame.image.load("gioconda8.png")
imagen9 = pygame.image.load("gioconda9.png")
    
    
matriz_inicial = [[imagen1, imagen4, imagen7]
                  [imagen2, imagen5, imagen8]
                  [imagen3, imagen6, imagen9]]

matriz_final = [[imagen1, imagen4, imagen7]
                  [imagen2, imagen5, imagen8]
                  [imagen3, imagen6, imagen9]]

for i in range (len(matriz_inicial)):
    for j in range (len(matriz_final)):
        resultado = matriz_inicial[i][j]

class Cuadrado:
    def dibujar(self):
        self.screen.fill(red)



    

