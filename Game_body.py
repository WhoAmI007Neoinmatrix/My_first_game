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

pygame.time.set_timer(EVENT, 500)
pygame.time.set_timer(EVENT_1, 1000)

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
player_speed = 10
size = 20
player_rect = pygame.Rect(x, y, size, size)

#enemy
enemy_speed = 2

#Create enemy object
def generate_obstacle(enemy_cubes):
    return Enemy(w_window, h_window, enemy_speed, enemy_cubes)

#group enemy
obstacle = pygame.sprite.Group()
generate_obstacle(obstacle)

#score
game_score = 0

#проверка на столкновение
def conflict_check(player_rect):
    global game_score
    for enemy in obstacle:
        if enemy.passed == False:
            if player_rect.colliderect(enemy.rect):
                enemy.passed = True
                game_score -= 1

def score_check(player_rect):
    global game_score
    for enemy in obstacle:
        if player_rect.x >= (enemy.rect.x + enemy.size_x) and  enemy.passed == False and enemy.score_ch:
            game_score += 1
            enemy.score_ch = False



while True:
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            exit()
        elif keys[pygame.K_ESCAPE]:
            exit()

        #if event.type == EVENT:
            #generate_obstacle(obstacle)
        if event.type == EVENT_1:
            generate_obstacle(obstacle)





    #определяем положение игрока
    player_rect.x = func_player.move_x(player_rect.x, player_speed, keys, w_window)
    player_rect.y = func_player.move_y(player_rect.y, player_speed, keys, h_window)

    #проверка столкновений и зачёт очков за обход препятствия
    conflict_check(player_rect)
    score_check(player_rect)


    sc.fill(BLACK)#рисуем чёрный фон
    surf_window.fill(WHITE)#рисуем игровое поле
    pygame.draw.rect(surf_window, BLUE, player_rect)#рисуем игрока
    obstacle.draw(surf_window)#рисуем препятствия
    sc.blit(surf_window, ((sc_x - w_window) / 2, (sc_y - h_window) / 2))

    menu.print_score(game_score, WHITE, sc)#рисуем счёт

    pygame.display.update()
    clock.tick(FPS)

    obstacle.update()#обновляем положение препятствий
