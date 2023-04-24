import pygame
import character
import room

pygame.init()
window = pygame.display.set_mode((500, 500))
ch = character.Character(50, 50)
ro = room.Room()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        ch.move_left()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        ch.move_right()
    if key[pygame.K_UP] or key[pygame.K_w]:
        ch.move_up()
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        ch.move_down()
    if key[pygame.K_q]:
        run = False
    character.Character.update(ch)
    pygame.draw.rect(window, (31, 14, 65), ch.rect)
    pygame.draw.rect(window, (0, 255, 0), ro.rect1)
    pygame.draw.rect(window, (0, 255, 0), ro.rect2)
    pygame.draw.rect(window, (0, 255, 0), ro.rect3)
    pygame.draw.rect(window, (0, 255, 0), ro.rect4)
    pygame.display.flip()


pygame.quit()
exit()