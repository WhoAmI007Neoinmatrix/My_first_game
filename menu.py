import pygame
pygame.init()

def print_score(score, color, sc):
    shrift_sys = pygame.font.SysFont(None, 48)
    sc_text = shrift_sys.render(f"SCORE: {score}", 1, color)
    pos_text = sc_text.get_rect(topleft = (5, 5))
    return sc.blit(sc_text, pos_text)

def get_high_score():
    with open("High_score.txt", "r") as file:
        return int(file.read())


def print_high_score(high_score, w_game, color, sc):
    shrift_sys = pygame.font.SysFont(None, 48)
    sc_text = shrift_sys.render(f"HIGH SCORE: {high_score}", 1, color)
    pos_text = sc_text.get_rect(topright = (w_game-5, +5))
    return sc.blit(sc_text, pos_text)

def check_high_score(high_score, score):
    if score > high_score:
        return score
    else:
        return high_score

def save_high_score(high_score):
    with open("High_score.txt", "r+") as file:
        old_score = int(file.read())
        if high_score > old_score:
            file.seek(0)
            file.write(str(high_score))


def print_systaine(w_game, h_game, game_state, GAME_START, GAME_OVER, score, color, sc):
    shrift_sys = pygame.font.SysFont(None, 48)
    if game_state == GAME_START:
        text_lines = ["PRESS SPACE TO PLAY"]
    elif game_state == GAME_OVER and score <= get_high_score():
        text_lines = ["GAME OVER", f"YOUR SCORE: {score}", "PRESS SPACE TO PLAY AGAIN"]
    elif game_state == GAME_OVER and score > get_high_score():
        text_lines = ["GAME OVER", f"NEW HIGH SCORE: {score}", "PRESS SPACE TO PLAY AGAIN"]


    y_offset = -shrift_sys.get_height()
    for line in text_lines:
        sc_text = shrift_sys.render(line, 1, color)
        pos_text = sc_text.get_rect(center = (w_game//2, h_game//2 + y_offset))
        y_offset += shrift_sys.get_height()
        sc.blit(sc_text, pos_text)
