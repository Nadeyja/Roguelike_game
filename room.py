import pygame


class Room(object):
    walls = []

    def __init__(self, walls=walls):
        self.rect1 = pygame.Rect(0, 0, 1, 500)
        self.rect2 = pygame.Rect(499, 0, 1, 500)
        self.rect3 = pygame.Rect(0, 499, 500, 1)
        self.rect4 = pygame.Rect(0, 0, 500, 1)
        walls.append(self.rect1)
        walls.append(self.rect2)
        walls.append(self.rect3)
        walls.append(self.rect4)
