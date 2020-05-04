import pygame

pygame.image.load("greenhillzone.png")
pygame.image.load("FondSonic.png")
pygame.image.load("sonic_spritesheet.png")

RUNNING = True
 
def events_main():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
 
def events_keyboard():
    pressed = pygame.key.get_pressed()
 
    if pressed[pygame.K_DOWN]:
        ## Faire action
     
    if pressed[pygame.K_UP]:
        ## Faire action
 
 
def events_mouse():
    mouse = pygame.mouse.get_pressed()
    position = pygame.mouse.get_pos()
 
    if mouse[0]:# Clique Gauche
        ## Faire action
     
    if mouse[2]: ## Clique droite
        ## Faire action
 
 
while RUNNING:
    events_main()
 
    events_keyboard()
 
    events_mouse()
