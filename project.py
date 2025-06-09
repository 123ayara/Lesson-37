import pygame
import random
pygame.init()
WIDTH, HEIGHT=800, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Zombies")
background=pygame.image.load("background.jpg")
player_img=pygame.image.load("R.png")
enemy_img=pygame.image.load("zombie.png")
player_img=pygame.transform.scale(player_img, (50, 50))
enemy_img=pygame.transform.scale(enemy_img, (50, 50))
player_rect=player_img.get_rect()
player_rect.topleft=(WIDTH//2, HEIGHT//2)
player_speed=5
enemies = []
for _ in range(7):
    x=random.randint(0, WIDTH - 50)
    y=random.randint(0, HEIGHT - 50)
    rect =enemy_img.get_rect(topleft=(x, y))
    enemies.append(rect)
score=0
font=pygame.font.SysFont(None, 36)
clock=pygame.time.Clock()
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x-=player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x+=player_speed
    if keys[pygame.K_UP]:
        player_rect.y-=player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y+=player_speed
    for enemy in enemies[:]:
        if player_rect.colliderect(enemy):
            enemies.remove(enemy)
            score+=1
    screen.blit(background, (0, 0))
    screen.blit(player_img, player_rect)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    score_text=font.render(f"score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
pygame.quit()