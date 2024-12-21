import pygame
from random import randint

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Sounds/YPIL.mp3")
pygame.mixer.music.play(-1)
WINDOWS_HEIGHT=800
WINDOWS_WIDTH=800

clock=pygame.time.Clock()

screen=pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
pygame.display.set_caption("Cursed Flappy")

running=True
Backroundimage= "images/dont worry abt it.jpg"
Backround=pygame.image.load(Backroundimage)

score = 0  

Playerimage= "images/FlappyBlue.png"

PipeList = []

Player = pygame.image.load(Playerimage)  
Player = pygame.transform.scale(Player, (100, 100))
Playerposition = Player.get_rect()
Playerposition.y = WINDOWS_HEIGHT/2
Playerposition.x = WINDOWS_WIDTH/2


gameoverfont=pygame.font.Font("DancingScript-Regular.ttf", 40)
gameovertext = gameoverfont.render("Game Over! ;)", True ,(0,0,0) , (255,255,255))

class Pipe:
    def __init__(self):
        gap = 450  
        random_pipe_length = randint(100, WINDOWS_HEIGHT- gap-100)
        pipe_image = pygame.image.load("images/pipe 4 CF.png")
        scale_pipe_image = pygame.transform.scale(pipe_image,(50, random_pipe_length))

        self.top_pipe_image = pygame.transform.flip(scale_pipe_image, False, True)

        bottom_pipe_height = WINDOWS_HEIGHT - random_pipe_length - gap
        self.bottom_pipe_image = scale_pipe_image

        self.top_pipe = self.top_pipe_image.get_rect()
        self.bottom_pipe = self.bottom_pipe_image.get_rect()

        self.top_pipe.y = 0
        self.bottom_pipe.y = WINDOWS_HEIGHT - bottom_pipe_height

        self.top_pipe.x = WINDOWS_WIDTH
        self.bottom_pipe.x = WINDOWS_WIDTH

        self.made_next_pipe = False
        self.add_score = False
        PipeList.append(self)


        
       

    def move_pipe(self):
        self.bottom_pipe.x -= 3
        self.top_pipe.x -= 3

        if Playerposition.colliderect(self.top_pipe) or Playerposition.colliderect(self.bottom_pipe):
            pygame.quit()

        if self.bottom_pipe.x < WINDOWS_WIDTH / 2 and not self.made_next_pipe:
            new_pipe = Pipe()
            PipeList.append(new_pipe)
            self.made_next_pipe = True
        if self.bottom_pipe.x < 0:
            PipeList.remove(self)
        
        if Playerposition.x > self.bottom_pipe.x and not self.add_score:
            global score 
            score += 1
            print (score)

            self.add_score = True  



        

first_pipe = Pipe()

while running:  
    pygame.time.Clock().tick(60)
    screen.blit(Backround, Backround.get_rect())
    # screen blit takes (image, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
        if pressed[pygame.K_SPACE]:
            Playerposition.y -= 80
    Playerposition.y += 5
    screen.blit(Player, Playerposition)

    for pipe in PipeList:
        screen.blit(pipe.top_pipe_image, pipe.top_pipe)
        screen.blit(pipe.bottom_pipe_image, pipe.bottom_pipe)
        pipe.move_pipe()
    pygame.display.update()
     
