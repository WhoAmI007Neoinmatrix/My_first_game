import pygame
pygame.init()

def move_x(x, speed, size, keys, w_window):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if x > 0:
            x-=speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if x < (w_window - size):
            x += speed
    return x

def move_y(y, speed, size, keys, h_window):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if y > 0:
            y -= speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if y < h_window-size:
            y += speed
    return y