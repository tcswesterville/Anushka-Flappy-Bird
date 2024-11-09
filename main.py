import pygame

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

Pipeimage= "images/pipe 4 CF.png"
Pipe = pygame.image.load(Pipeimage)
Playerimage= "images/FlappyBlue.png"

PipeList = []

Player = pygame.image.load(Playerimage)  
Player = pygame.transform.scale(Player, (100, 100))
Pipeupsidedown = pygame.transform.flip(Pipe,False, True)

Playerposition = Player.get_rect()
Pipeposition = Pipe.get_rect()
Playerposition.y = WINDOWS_HEIGHT/2
Playerposition.x = WINDOWS_WIDTH/2
Pipeposition.x = WINDOWS_HEIGHT/1   
Pipeposition.y = WINDOWS_WIDTH/1.6    
PipeList.append(Pipeposition)

gameoverfont=pygame.font.Font("DancingScript-Regular.ttf", 40)
gameovertext = gameoverfont.render("Game Over! ;)", True ,(0,0,0) , (255,255,255))


while running:
    for sigmapipe in PipeList: 
        sigmapipe.x-=1
    pygame.time.Clock().tick(60)
    screen.blit(Backround, Backround.get_rect())
    # screen blit takes (image, (x, y))
    screen.blit(Pipeupsidedown,(Pipeposition))

 
# Colision Code
    for EachPipe in PipeList:
       if Playerposition.colliderect(EachPipe): 
            running = False

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
    pygame.display.update()
     
