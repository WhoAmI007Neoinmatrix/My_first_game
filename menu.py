import pygame
pygame.init()

def print_score(score, color, sc):
    shrift_sys = pygame.font.SysFont(None, 48)
    sc_text = shrift_sys.render(f"SCORE: {score}", 1, color)
    pos_text = sc_text.get_rect(topleft = (0, 0))
    return sc.blit(sc_text, pos_text)

