import pygame
import random
from pygame.locals import*
pygame.init()



screenW, screenH = 375,700
screen = pygame.display.set_mode((screenW, screenH))
FPS = 60
FramePerSec = pygame.time.Clock()
framecount = 0
score = 0
gameover = False
font = pygame.font.SysFont("Comic Sans MS", 60)
font1 = pygame.font.SysFont("Comic Sans MS", 30)
pygame.display.set_caption("Tile Game")



#Bottom Block Class
class Block():
    def __init__ (self,x,y,width,height,screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.width,self.height])

block = (Block(400,660,85,40,screen))



#Lines seperating Block class movement
class Line():
    def __init__ (self,spos,epos,width,screen):
        self.spos = spos
        self.epos = epos
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.line(self.screen,(255,255,255),self.spos,self.epos,self.width)

linearray = []
def genline():
    for x in range(5):
        linearray.append(Line((372,0),(372,700),4,screen))
        linearray.append(Line((279,0),(279,700),4,screen))
        linearray.append(Line((186,0),(186,700),4,screen))
        linearray.append(Line((93,0),(93,700),4,screen))
        linearray.append(Line((0,0),(0,700),4,screen))
genline()



#Target for Block Class
class Target():
    def __init__ (self,x,y,width,height,screen,falling):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.speed_y = 10
        self.falling = falling
        self.hit = True

    targetarray = []
    def gentarget():
        for x in range(10):
            Target.targetarray.append(Target(0,-85,85,40,screen,False))
            Target.targetarray.append(Target(98,-85,85,40,screen,False))
            Target.targetarray.append(Target(191,-85,85,40,screen,False))
            Target.targetarray.append(Target(284,-85,85,40,screen,False))

    def draw(self):
        pygame.draw.rect(self.screen,(0,0,51),[self.x,self.y,self.width,self.height])

    def update(self):
        self.y += self.speed_y

    def pause(self):
        self.draw()
        self.resetposition()

        if self.falling == True:
            self.update()

    def collision(self):
        global score
        if block.x == self.x and self.y + self.height >= block.y:
            self.y = screenH * -1
            score +=1
            
    def resetposition(self):
        if self.y >= screenH:
            self.hit = False
            self.falling = False
        else:
            self.collision()
            self.hit = True

Target.gentarget()



#Bottom outline squares for block
def drawsquare():
    y = 660
    c = (30, 30, 30)
    pygame.draw.rect(screen,c,[5,y,block.width,block.height])
    pygame.draw.rect(screen,c,[98,y,block.width,block.height])
    pygame.draw.rect(screen,c,[191,y,block.width,block.height])
    pygame.draw.rect(screen,c,[284,y,block.width,block.height])



#While Loop
while True:

    framecount += 1

    #Block Movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                block.x = 5
            if event.key == pygame.K_g:
                block.x = 98
            if event.key == pygame.K_h:
                block.x = 191
            if event.key == pygame.K_j:
                block.x = 284
            if event.key == pygame.K_SPACE:
                gameover = False

    if gameover == False: 
        
        #Drawing/Screen Update
        screen.fill((102,0,51))
        drawsquare()

        #Calling Target Functions
        for target in Target.targetarray:
            target.pause()

        #Drawing block for a second
        block.draw()
        block.x = 400
        
        #Gaps of falling targets
        if framecount % 10 == 0:
            randomTarget = random.randrange(0,len(Target.targetarray) -1)
            while Target.targetarray[randomTarget].falling == True:
                randomTarget = random.randrange(0,len(Target.targetarray) -1)
            Target.targetarray[randomTarget].falling = True

        #Calling Line Function
        for line in linearray:
            line.draw()

        #Score text
        label = font.render(str(score), 1, (255,255,255))
        screen.blit(label, (169,100))

        #Calling Function
        for target in Target.targetarray:
            if not target.hit:
                gameover = True
                break


    else:
        #Drawing Gameover Screen
        screen.fill((0,0,0))
        label = font.render("Game Over", 1, (255,255,255))
        label1 = font1.render("Press Space To Restart", 1, (255,255,255))
        label2 = font1.render("Score:", 1,(255,255,255))
        screen.blit(label, (35,50))
        screen.blit(label1, (30,500))
        screen.blit(label2, (30,400))

        def reset():
            global score
            score = 0
            block.x = 400
            for target in Target.targetarray:
<<<<<<< HEAD
                target.falling = False
        reset()

        screen.blit(label1, (25,500))
        screen.blit(label2, (260,400))
        screen.blit(label3, (90,400))
        for target in Target.targetarray:
            target.y-=50
=======
                target.y = -85
        reset()

>>>>>>> parent of 14fd172 (Update new.py)

    pygame.display.update()
    FramePerSec.tick(FPS)