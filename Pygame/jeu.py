from typing_extensions import Self
import pygame
import pygame_menu
from pygame.locals import *


nombre_sprite_cote = 4
taille_sprite = 45
cote_fenetre = nombre_sprite_cote * taille_sprite





class Perso:
	def __init__(self, move, attack,hurt,die,idle):
		self.move = move
		self.attack = attack
		self.hurt = hurt
		self.die = die  
		self.idle = idle    
  
		self.x = 0
		self.y = 0

		self.currentImg=self.idle[0]
		self.state = self.move
		self.currentFrame=0
  
	def walk(self):
		self.x = self.x+1




pygame.init()
surface = pygame.display.set_mode((960,540))

def start_the_game():
	pygame.init()
	fenetre = pygame.display.set_mode((960,540))
	
	move=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk5.png").convert_alpha()]
	attack=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack5.png").convert_alpha()]
	hurt=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/hurt/hurt1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/hurt/hurt2.png").convert_alpha()]
	die=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die5.png").convert_alpha()]
	idle=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle4.png").convert_alpha()]
    
	fond = pygame.image.load("/Users/rmadery/Desktop/Pygame/images/background.png").convert()
	fenetre.blit(fond, (0,0))

	perso = Perso(move,attack,hurt,die,idle)
	pygame.display.flip()

	continuer = 1
	while continuer:
		
		pygame.key.set_repeat(400, 30)
		for event in pygame.event.get():  
			if event.type == QUIT:  
				continuer = 0   

			if (perso.currentFrame + 1<len(perso.state)):
				perso.currentImg=perso.state[perso.currentFrame +1]
				perso.currentFrame+=1
			else:
				perso.currentFrame=0
		fenetre.blit(fond, (0,0))	
		fenetre.blit(perso.currentImg, (perso.x, perso.y)) 
		pygame.event.pump()
		pygame.time.delay(80) 
		pygame.display.flip()
start_the_game()


