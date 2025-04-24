import pygame
import random

enemy_size_x = [20, 40, 60, 80, 100]
enemy_size_y = [20, 40, 60, 80, 100]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, w_window, h_window, speed_enemy, enemy_cubes):
        pygame.sprite.Sprite.__init__(self)
        self.x = 400
        self.speed_enemy = speed_enemy
        self.size_x = random.choice(enemy_size_x)
        self.size_y = random.choice(enemy_size_y)
        self.y_coord = random.randint(0, h_window-self.size_y)
        self.color = (255, 0, 0)
        self.image = pygame.Surface([self.size_x, self.size_y])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(left=w_window, top=self.y_coord)
        self.passed = False
        self.score_ch = True
        self.add(enemy_cubes)

    def update(self, *args):
        self.rect.x -= self.speed_enemy

        if self.rect.right <= 0 or args[0]==args[1]:
            self.kill()




