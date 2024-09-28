import pygame

pygame.init()
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
Playerimage= "images/PP.jpg"

Player = pygame.image.load(Playerimage)
Player = pygame.transform.scale(Player, (100, 100))

Playerposition = Player.get_rect()
Playerposition.y = WINDOWS_HEIGHT/2
Playerposition.x = WINDOWS_WIDTH/2
while running:
    screen.blit(Backround, Backround.get_rect())
    # screen blit takes (image, (x, y))
    screen.blit(Pipe,(0,4))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
        if pressed[pygame.K_SPACE]:
            Playerposition.y -= 45
    Playerposition.y += 3
    screen.blit(Player, Playerposition)
    pygame.display.update()

