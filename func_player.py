import pygame
pygame.init()

def move_x(x, speed, keys, w_window):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if x >= 10:
            x-=speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if x <= (w_window - 30):
            x += speed
    return x

def move_y(y, speed, keys, h_window):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if y >= 10:
            y -= speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if y <= h_window-30:
            y += speed
    return y