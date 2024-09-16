import pygame
import random


pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

player_image = pygame.image.load("assets/player.png")  
player_image = pygame.transform.scale(player_image, (40, 40))  

enemy_image = pygame.image.load("assets/enemy.png")  
enemy_image = pygame.transform.scale(enemy_image, (30, 30))  

player_width = 40
player_height = 40
player = pygame.Rect(169, 359, player_width, player_height)
player_speed = 5

life = 3
points = 0
gamestate = "start"

enemies = []
bullets = []
bullet_fired = False  

font = pygame.font.Font(None, 36)

def create_enemy():
    enemy = pygame.Rect(random.randint(50, screen_width - 50), 0, 30, 30)
    enemies.append(enemy)

def create_bullet():
    bullet = pygame.Rect(player.x + player_width // 2 - 5, player.y, 5, 10)
    bullets.append(bullet)

def show_menu():
    screen.fill(black)
    title_text = font.render("Space Shooter", True, white)
    screen.blit(title_text, (100, 100))
    instructions_text = font.render("Press UP to Start", True, white)
    screen.blit(instructions_text, (50, 200))
    pygame.display.flip()

def play():
    global life, points, gamestate, bullet_fired

    screen.fill(black)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += player_speed

    if keys[pygame.K_SPACE] and not bullet_fired:
        create_bullet()
        bullet_fired = True  

    if not keys[pygame.K_SPACE]:
        bullet_fired = False

    for enemy in enemies[:]:
        enemy.y += 4
        if enemy.y > screen_height:
            enemies.remove(enemy)
            life -= 1
            if life <= 0:
                gamestate = "game_over"

    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                points += 10
                break

    screen.blit(player_image, (player.x, player.y))

    for enemy in enemies:
        screen.blit(enemy_image, (enemy.x, enemy.y))

    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)

    life_text = font.render(f"Life: {life}", True, white)
    points_text = font.render(f"Points: {points}", True, white)
    screen.blit(life_text, (10, 10))
    screen.blit(points_text, (250, 10))

    pygame.display.flip()

def game_over():
    screen.fill(black)
    game_over_text = font.render("Game Over!", True, red)
    restart_text = font.render("Press R to Restart", True, white)
    screen.blit(game_over_text, (100, 150))
    screen.blit(restart_text, (50, 200))
    pygame.display.flip()

def restart():
    global life, points, enemies, bullets, gamestate
    life = 3
    points = 0
    enemies = []
    bullets = []
    gamestate = "start"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gamestate == "start":
        show_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            gamestate = "play"
    elif gamestate == "play":
        if random.randint(1, 60) == 1:
            create_enemy()
        play()
    elif gamestate == "game_over":
        game_over()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            restart()

    pygame.time.delay(30)

pygame.quit()
