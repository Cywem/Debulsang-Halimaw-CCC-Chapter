import pygame
import spritesheet

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()
screen = pygame.display.set_mode((800,600))
running = True
###########################################################################################

BG = (50, 50, 50)
BLACK = (0, 0, 0)

# ANIMATION
my_spritesheet = pygame.image.load('trainer_sheet.png').convert_alpha()
trainer_sheet = spritesheet.Spritesheet(my_spritesheet)

#animation
animation_list  = []
animation_steps = 5
last_update = pygame.time.get_ticks()
animation_cd = 250
frame = 0

for x in  range(animation_steps):
    animation_list.append(trainer_sheet.get_sprite(x, 128, 128, 2, BLACK))

while running:
    screen.fill(BG)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cd:
        frame += 1
        last_update =  current_time
        if frame >= len(animation_list):
            frame = 0

    #show frames
    screen.blit(animation_list[frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()