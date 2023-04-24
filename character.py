import pygame
import room


class Character(object):
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 20, 20)

    def update(self):
        self.rect.update(self.x, self.y, 20, 20)

    def move_left(self):
        if self.rect.colliderect(room.Room.walls[0]):
            pass
        else:
            self.x -= 0.1

    def move_right(self):
        if self.rect.colliderect(room.Room.walls[1]):
            pass
        else:
            self.x += 0.1

    def move_down(self):
        if self.rect.colliderect(room.Room.walls[2]):
            pass
        else:
            self.y += 0.1

    def move_up(self):
        if self.rect.colliderect(room.Room.walls[3]):
            pass
        else:
            self.y -= 0.1
