from random import randrange
from typing_extensions import Self
import pygame
import pygame_menu
from pygame.locals import *



windowsWidth=2500
windowsHeight=350

         
class Ennemi:
	def __init__(self, attack,die,idle,x,y,hp):
		self.attack = attack
		self.die = die  
		self.idle = idle
		self.currentHP=hp
		self.maxHP=hp
		self.currentLVL=1
		self.x = x
		self.y = y  
		self.currentImg=self.idle[0]
		self.state = self.idle
		self.currentFrame=0
		self.damage=1	
	def drawHPBar(self,x,y,width,color):
		left=x
		top=y
		height=5
		filled=0
		pygame.draw.rect(surface, color, [left, top, width, height], filled)  
         
class Perso:
	def __init__(self, move, attack,hurt,die,idle,x):
		self.move = move
		self.attack = attack
		self.hurt = hurt
		self.die = die  
		self.idle = idle
		self.currentHP=10
		self.maxHP=10
		self.currentLVL=1
		self.damage=10	
  
		self.x = x
		self.y = 280

		self.currentImg=self.idle[0]
		self.state = self.idle
		self.currentFrame=0
  
	def walkRight(self):
		self.x = self.x+30
		if(self.x>windowsWidth):
			self.x=0
	def resetPosition(self):
		self.x = 0
  
	def drawHPBar(self,x,y,width,color):
		left=x
		top=y
		height=5
		filled=0
		pygame.draw.rect(surface, color, [left, top, width, height], filled)  
  
class Texte:
	def Update(self,texte,fenetre,x,y):
		police = pygame.font.Font(None,15)
		texte = police.render(texte,True,pygame.Color("#000000"))
		rectTexte = texte.get_rect()
		rectTexte.center = fenetre.get_rect().topleft
		rectTexte.bottom+=y
		rectTexte.left+=x
		fenetre.blit(texte,rectTexte)
 
pygame.init()
surface = pygame.display.set_mode((windowsWidth,windowsHeight))


def start_the_game():
	pygame.init()
	fenetre = pygame.display.set_mode((windowsWidth,windowsHeight))
	fenetre.fill((177, 181, 176))
 	
	move=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/walk/walk5.png").convert_alpha()]
	attack=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack5.png").convert_alpha()]
	hurt=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/hurt/hurt1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/hurt/hurt2.png").convert_alpha()]
	die=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/die5.png").convert_alpha()]
	idle=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/idle4.png").convert_alpha()]
    
	attackEnnemi=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack4.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/attack/attack5.png").convert_alpha()]
	dieEnnemi=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/monsterDie1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/monsterDie2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/monsterDie3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/die/monsterDie4.png").convert_alpha()]
	idleEnnemi=[pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/monsterIdle1.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/monsterIdle2.png").convert_alpha(), pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/monsterIdle3.png").convert_alpha(),pygame.image.load("/Users/rmadery/Desktop/Pygame/images/idle/monsterIdle4.png").convert_alpha()]
    
	perso = Perso(move,attack,hurt,die,idle,0)
	monster = Ennemi(attackEnnemi,dieEnnemi,idleEnnemi,windowsWidth-300,45,500)


	hp=Texte()
	lvl=Texte()

	pygame.display.flip()
 
	die=False
	continuer = 1
	while continuer:
		pygame.key.set_repeat(400, 30)
		for event in pygame.event.get():  
			if event.type == QUIT:  
				continuer = 0   
			if (perso.x ==0 and perso.currentHP<perso.maxHP):
				perso.currentHP+=1
			if (perso.currentFrame <len(perso.state)):
				perso.currentImg=perso.state[perso.currentFrame]
				perso.currentFrame+=1
			else:
				perso.currentFrame=0
			if (monster.currentFrame <len(monster.state)):
				monster.currentImg=monster.state[monster.currentFrame]
				monster.currentFrame+=1	
			else:
				if(die==True):
					monster.state=monster.idle
					die=False
				monster.currentFrame=0
			
			keys = pygame.key.get_pressed()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					perso.state=perso.idle
					perso.resetPosition()
				if event.key == pygame.K_RIGHT:
					if(perso.x>=windowsWidth-350):
						perso.state=perso.attack
						monster.currentHP-=perso.damage
						rand=randrange(10) 
						if(rand==0):
							perso.currentHP-=monster.damage
							if(perso.currentHP<=0):
								perso.currentHP=perso.maxHP
								perso.state=perso.die
						if(monster.currentHP<=0):
							monster.currentHP=monster.maxHP
							die=True
							monster.state=monster.die

					else: 
						perso.state=perso.move
						perso.walkRight()
				if event.key == pygame.K_a:
					perso.state=perso.attack
     
			
			#perso.walk()


#150 150hp
#30    100hp
		fenetre.fill((177, 181, 176))
		fenetre.blit(perso.currentImg, (perso.x, perso.y)) 
		fenetre.blit(monster.currentImg, (monster.x, monster.y))   
  

  
		perso.drawHPBar(perso.x+20,perso.y-5,(perso.currentHP*60)/10,[36,135,11])
		lvl.Update(texte=str("LvL : "+str(perso.currentLVL)),fenetre=fenetre,x=perso.x+50,y=perso.y-20)
		hp.Update(texte=str("HP : "+str(perso.currentHP)+"/"+str(perso.maxHP)),fenetre=fenetre,x=perso.x+50,y=perso.y-10)
 
		lvl.Update(texte=str("LvL : "+str(monster.currentLVL)),fenetre=fenetre,x=monster.x+560,y=monster.y-20)
		hp.Update(texte=str("HP : "+str(monster.currentHP)+"/"+str(monster.maxHP)),fenetre=fenetre,x=monster.x+110,y=monster.y-10)
		monster.drawHPBar(monster.x+80,perso.y-240,(monster.currentHP*100)/150,[170, 32, 32])
		pygame.event.pump()
		pygame.time.delay(150) 
		pygame.display.flip()
		pygame.display.update()

start_the_game()

