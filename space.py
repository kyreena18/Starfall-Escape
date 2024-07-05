import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

# Load and scale the rocket image
ROCKET_IMG = pygame.image.load("rocket.png").convert_alpha()
ROCKET = pygame.transform.scale(ROCKET_IMG, (40, 60))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))
    WIN.blit(ROCKET, (player.x, player.y))  # Blit the rocket image at player's position
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()
