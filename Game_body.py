import pygame

pygame.init()
import func_player
from func_obstacle import Enemy
import menu

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

w_game = 650
h_game = 500

EVENT = pygame.USEREVENT
EVENT_1 = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT, 100)
pygame.time.set_timer(EVENT_1, 300)

#game rect
sc = pygame.display.set_mode((w_game, h_game), pygame.RESIZABLE)
sc_x, sc_y = sc.get_size()
pygame.display.set_caption("Best cube")
sc.fill(BLACK)

#procecced rect
w_window = 600
h_window = 400
surf_window = pygame.Surface((w_window, h_window))
surf_window.fill(WHITE)
sc.blit(surf_window, ((sc_x-w_window)/2 ,(sc_y-h_window)/2))


clock = pygame.time.Clock()
FPS = 60



#start position and player
x = w_window // 6
y = h_window // 2
player_speed = 5
player_size = 20
player_rect = pygame.Rect(x, y, player_size, player_size)

#enemy
enemy_speed = 4

#Create enemy object
def generate_obstacle(enemy_cubes):
    return Enemy(w_window, h_window, enemy_speed, enemy_cubes)

#group enemy
obstacle = pygame.sprite.Group()

#score
game_score = 0
high_score = menu.get_high_score()

#game state
GAME_START = 0
GAME_PLAY = 1
GAME_OVER = 2

game_state = GAME_START


#проверка на столкновение
def conflict_check(player_rect):
    global game_state, GAME_OVER
    for enemy in obstacle:
        if enemy.passed == False:
            if player_rect.colliderect(enemy.rect):
                enemy.passed = True
                game_state = GAME_OVER

def score_check(player_rect):
    global game_score
    for enemy in obstacle:
        if player_rect.x >= (enemy.rect.x + enemy.size_x) and  enemy.passed == False and enemy.score_ch:
            game_score += 1
            enemy.score_ch = False



while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] and game_state == GAME_OVER:
            menu.save_high_score(high_score)
            exit()
        elif event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            exit()
        elif keys[pygame.K_SPACE] and game_state != GAME_PLAY:
            game_state = GAME_PLAY
            menu.save_high_score(high_score)
            game_score = 0
            player_rect.x = x
            player_rect.y = y


        #if event.type == EVENT:
            #generate_obstacle(obstacle)
        if event.type == EVENT_1 and game_state == GAME_PLAY:
            generate_obstacle(obstacle)

    if game_state == GAME_PLAY:
    #определяем положение игрока
        player_rect.x = func_player.move_x(player_rect.x, player_speed, player_size, keys, w_window)
        player_rect.y = func_player.move_y(player_rect.y, player_speed, player_size, keys, h_window)
    #проверка столкновений и зачёт очков за обход препятствия
        conflict_check(player_rect)
        score_check(player_rect)

    sc.fill(BLACK)#рисуем чёрный фон
    surf_window.fill(WHITE)#рисуем игровое поле


    if game_state == GAME_PLAY:
        pygame.draw.rect(surf_window, BLUE, player_rect)  # рисуем игрока
        obstacle.draw(surf_window)#рисуем препятствия

    sc.blit(surf_window, ((sc_x - w_window) / 2, (sc_y - h_window) / 2))

    if game_state == GAME_PLAY:
        menu.print_score(game_score, WHITE, sc)#рисуем счёт
        obstacle.update(game_state, GAME_OVER)  # обновляем положение препятствий
        high_score = menu.check_high_score(high_score, game_score)

    menu.print_high_score(high_score, w_game, WHITE, sc)

    if game_state == GAME_START or game_state == GAME_OVER:
        menu.print_systaine(w_game, h_game, game_state, GAME_START, GAME_OVER, game_score, BLACK, sc)
        obstacle.update(game_state, GAME_OVER)





    pygame.display.update()
    clock.tick(FPS)


